# PDF Metadata Extractor using LLM and Streamlit

This app extracts structured metadata from research papers using a PDF upload, LangChain, Groq (llama-3.3-70b-versatile), and displays the result as JSON.

## Features
- Upload any PDF
- Extracts title, authors, abstracts, keywords, affiliations, references
- Uses Groq's LLaMA 3.1 model with LangChain
- Displays and downloads output as JSON

## Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py

## Libraies that have used

| Tool / Library         | Why It’s Used                                                                 |
|------------------------|--------------------------------------------------------------------------------|
| `pdfplumber`           | Extracts structured text from PDF files                                       |
| `streamlit`            | Builds the UI for file upload and JSON display                                |
| `langchain`            | Manages LLM prompts, chains, and pipeline flow                                |
| `langchain-groq`       | Connects LangChain to Groq’s LLaMA 3 models                                   |
| `ChatGroq`             | Runs the LLM inference (LLaMA 3.1)                                             |
| `PromptTemplate`       | Dynamically inserts PDF content into your JSON extraction prompt              |
| `dotenv`               | Loads API key securely from a `.env` file                                     |
| `yaml`                 | Reads config settings (e.g., prompt path, output path) from `config.yaml`     |
| `json` (stdlib)        | Parses and saves the LLM response as structured JSON                          |
| `tempfile`             | Temporarily stores uploaded PDFs in Streamlit before processing               |



