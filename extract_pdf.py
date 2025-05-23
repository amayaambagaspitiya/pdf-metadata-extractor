import pdfplumber

class PDFProcessor:
    def __init__(self, path_pdf):
        self.path_pdf = path_pdf

    def extract_pdf_text(self):
        try:
            with pdfplumber.open(self.path_pdf) as pdf:
                return "\n\n".join([
                    page.extract_text()
                    for page in pdf.pages
                    if page.extract_text()
                ])
        except Exception as e:
            print(e)
