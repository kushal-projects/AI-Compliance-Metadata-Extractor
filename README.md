
# 🏦 AI Compliance Metadata Extractor

**AI-powered tool for extracting structured metadata from compliance policy documents (PDF or TXT) using the power of LLMs — no API needed!**

![Demo Screenshot](https://raw.githubusercontent.com/kushal-projects/AI-Compliance-Metadata-Extractor/main/assets/demo.png)

---

## 📌 Scope

Organizations often have hundreds of compliance documents spread across teams and formats. Manually tracking key metadata like **policy names**, **owners**, and **last updated dates** is inefficient and error-prone.

> This tool solves that by **automatically extracting compliance metadata using a open-source large language model - TinyLlama**, enabling fast policy cataloging, audits, and reporting.

---
## 🎯 Why This Matters

✅ **Time-saving**: Automates a manual, repetitive task  
✅ **Risk-reduction**: Improves compliance audit readiness  
✅ **Privacy-focused**: No need to send data to third-party APIs  
✅ **Deployable**: Ready for integration in enterprise workflows  

---

## 🚀 What This Does

- 🗃️ **Takes PDF or plain text** files of compliance policies
- 🔍 **Extracts metadata** fields like:
 Policy name, author, version, dates
  - Responsible department, contact person
  - Table of contents
- 🧠 Uses a lightweight **open-source LLM** (no API keys)
- 🎛️ User-friendly **Gradio App Interface**
- 📄 Outputs results in structured JSON and .txt formats

---


## 🛠 Tech Stack

| Tool | Role |
|------|------|
| ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white) | 🐍 Core programming language |
| ![TinyLlama](https://huggingface.co/datasets/huggingface/brand-assets/resolve/main/llama-logo.svg) | 🤖 Compliance metadata extractor |
| ![Pdfplumber](https://img.shields.io/badge/-pdfplumber-343541?style=flat&logo=adobe-acrobat-reader&logoColor=EC1C24) | 🧾 PDF text extraction |
| ![Gradio](https://img.shields.io/badge/-Gradio-FF4C4C?style=flat&logo=gradio&logoColor=white) | 🎛 User interface for file input/output |
| ![Hugging Face Transformers](https://img.shields.io/badge/-Transformers-FFD21F?style=flat&logo=huggingface&logoColor=black) | 📦 Model loading and tokenizer support |
| ![PyTorch](https://img.shields.io/badge/-PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white) | 🧠 LLM backend for inference |


---
## 📦 How to Run Locally

1. **Clone the repo**
git clone https://github.com/yourusername/compliance-metadata-extractor.git
cd compliance-metadata-extractor

2. **Install dependencies**
pip install -r requirements.txt


3. **Run the app**
python app.py
text
- The app will open in your browser at `http://127.0.0.1:7860`
- Or use `share=True` in `app.py` to get a public link

## ⚠️ Limitations

- ❌ The current setup struggles with **very large PDF or text files**, potentially leading to memory overload or timeouts errors.
- ❌ Model may misclassify or omit metadata in complex or unstructured documents.
- 🧠 TinyLlama is a lightweight model optimized for simplicity and speed—not for deep semantic understanding.
- 📄 Currently supports only **English-language** PDFs.
- 🛠 Metadata fields are hardcoded; adding new types requires manual updates to the extraction pipeline.
- 🔐 Sensitive keys or tokens must be manually redacted before pushing to public platforms.

---

## 🚀 Scope for Improvement

- ⚡ Integrate **powerful open-source LLMs** like:
  - 🔹 **Mistral-7B** – A robust and fast model for complex text understanding.
  - 🔹 **Mixtral** – A sparse mixture-of-experts model great for multitask comprehension.
  - 🔹 **Phi-2** by Microsoft – Small yet surprisingly accurate for task-specific compliance QA.
- 🌍 Add multilingual support for international compliance policies.
- 📊 Build an interactive **dashboard** to visualize extracted metadata and trends.
- 🤖 Use **retrieval-augmented generation (RAG)** for context-aware extraction.
- 🔧 Modularize the architecture to switch between LLMs and tailor pipelines by domain.
- ☁️ Add cloud deployment (e.g., with Hugging Face Hub + Inference API) for scalable, on-demand usage.

---

## 👨‍💻 Author

**Kushal**  
AI/ML & Data Science Enthusiast  
Focused on building real-world AI applications with language models and automation.

---

## 📬 Contact

- 📧 Email: [your.email@example.com]
- 🐦 Twitter: [@yourhandle]
- 💼 LinkedIn: [linkedin.com/in/yourprofile]
- 🌐 Portfolio: [yourwebsite.dev]

---


