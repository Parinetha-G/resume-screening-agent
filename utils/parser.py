import pdfplumber
from docx import Document

def read_pdf(file_path):
    text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

    return text


def read_docx(file_path):
    document = Document(file_path)

    text = ""

    for para in document.paragraphs:
        text += para.text + "\n"

    return text


def read_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()