import io
from PyPDF2 import PdfReader

def extract_text_from_file(file_bytes, mime_type):
    if "pdf" in mime_type:
        reader = PdfReader(io.BytesIO(file_bytes))
        return "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
    elif "text" in mime_type:
        return file_bytes.decode("utf-8")
    else:
        return "❌ Неподдерживаемый формат файла."
