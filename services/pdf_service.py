import pdfplumber

class PDFService:
    @staticmethod
    def extract_text(file_path: str) -> str:
        with pdfplumber.open(file_path) as pdf:
            return "\n".join(
                page.extract_text()
                for page in pdf.pages
                if page.extract_text()
            )
