from utils.config_utils import load_config
from extract_pdf import PDFProcessor
from extract_agent import TextExtractor


if __name__ == "__main__":


    pdf = PDFProcessor("input.pdf")
    text = pdf.extract_pdf_text()

    extractor = TextExtractor((load_config()))
    metadata = extractor.extract(text)
    extractor.save_output(metadata)
