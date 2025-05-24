import os
import json
import torch
import gradio as gr
from transformers import AutoTokenizer, AutoModelForCausalLM
import pdfplumber

os.environ["TRANSFORMERS_NO_TF"] = "1"

model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float32,
    device_map={"": "cpu"}
)

metadata_fields = [
    "policy_name", "author", "last_updated_date", "effective_date", "version",
    "responsible_department", "contact_person", "table_of_contents",
    "compliance_objective", "review_frequency", "regulatory_references"
]

def extract_metadata(file):
    try:
        if file is None:
            return "Please upload a .txt or .pdf file."
        filename = file if isinstance(file, str) else getattr(file, "name", None)
        ext = os.path.splitext(filename)[1].lower() if filename else ""
        document_text = ""
        if ext == ".pdf":
            with pdfplumber.open(file) as pdf:
                for i, page in enumerate(pdf.pages[:10]):
                    page_text = page.extract_text()
                    if page_text:
                        document_text += page_text + "\n"
            if not document_text.strip():
                return "No extractable text found in the PDF. If your PDF is scanned (image-only), please use OCR to convert it to text first."
        elif ext == ".txt":
            if isinstance(file, str):
                with open(file, "r", encoding="utf-8") as f:
                    document_text = f.read()
            else:
                document_text = file.read().decode("utf-8")
        else:
            return "Unsupported file type. Please upload a .txt or .pdf file."
        document_text = document_text[:3000]

        prompt = (
            "You are an AI assistant. Extract the following metadata fields from the compliance document and "
            "return them as a valid JSON object:\n\n"
            f"{', '.join(metadata_fields)}\n\n"
            f"Document:\n{document_text}\n\n"
            "JSON Output:"
        )

        inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=2048).to(model.device)
        with torch.no_grad():
            output = model.generate(**inputs, max_new_tokens=512, do_sample=False)
        generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

        start_index = generated_text.find("{")
        end_index = generated_text.rfind("}") + 1
        json_text = generated_text[start_index:end_index]

        try:
            metadata = json.loads(json_text)
        except Exception:
            metadata = {"error": "Failed to parse JSON", "raw_output": generated_text}

        return json.dumps(metadata, indent=4)

    except Exception as e:
        return f"Error: {str(e)}"

# Custom CSS for permanent black background and light text
custom_css = """
body, .gradio-container {
    background-color: #0d0d0d !important;
    color: #ffffff !important;
}
h1, h2, h3, label, p, span {
    color: #ffffff !important;
}
button, .svelte-1ipelgc, .svelte-13f8qtd {
    background-color: #2b2b2b !important;
    color: white !important;
}
input, textarea, .gr-box {
    background-color: #1a1a1a !important;
    color: white !important;
    border: 1px solid #444 !important;
}
"""

with gr.Blocks(css=custom_css, theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    # 🏦 AI-Powered Compliance Metadata Extractor - TinyLlama 1.1B

    **Instructions:**
    1. Upload a compliance policy text file (.txt) or PDF file (.pdf).  
    2. Click 'Submit' to extract metadata.  
    3. The extracted metadata will appear on the right. You can copy the JSON output.

    *Note: For best results, use a plain text or PDF file with clear policy sections. For large PDFs, only the first 10 pages will be processed. If your PDF is a scan/image, please use OCR first.*
    """)

    with gr.Row():
        with gr.Column():
            file_input = gr.File(
                label="Upload Compliance Policy (.txt or .pdf)",
                type="filepath",
                file_types=[".txt", ".pdf"]
            )
            submit_btn = gr.Button("Submit")
            gr.Examples(
                [[os.path.join(os.getcwd(), "sample.txt")],
                 [os.path.join(os.getcwd(), "Compliance_ACMEBANK.pdf")],
                 [os.path.join(os.getcwd(), "Compliance_Global.pdf")]],
                inputs=file_input,
                label="Example Compliance Policy"
            )
        with gr.Column():
            output_box = gr.Textbox(
                label="Extracted Metadata (JSON)",
                lines=30,
                show_copy_button=True
            )
    submit_btn.click(extract_metadata, inputs=file_input, outputs=output_box)

    gr.Markdown("""
    ---
    **Powered by [TinyLlama-1.1B-Chat-v1.0](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0) and Gradio.**
    """)

if __name__ == "__main__":
    demo.launch(share=True)