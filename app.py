import streamlit as st
import json
import tempfile
from extract_pdf import PDFProcessor
from extract_agent import TextExtractor
from utils.config_utils import load_config

st.set_page_config(page_title="PDF Metadata Extractor", layout="wide")
st.title("📄 Research Paper Metadata Extractor")

uploaded_file = st.file_uploader("Upload a research paper (PDF)", type=["pdf"])

if uploaded_file:
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        pdf_path = tmp.name

    pdf_processor = PDFProcessor(pdf_path)
    text = pdf_processor.extract_pdf_text()

    if not text:
        st.error("Failed to extract text from PDF.")
    else:
 
        config = load_config()
        extractor = TextExtractor(config)
        metadata = extractor.extract(text)


        if metadata:
            st.subheader("📦 Extracted Metadata (JSON)")
            st.json(metadata)

            st.download_button(
                label="Download JSON",
                data=json.dumps(metadata, indent=2),
                file_name="metadata.json",
                mime="application/json"
            )
        else:
            st.warning("No metadata extracted.")
