import fitz

def extract_text(pdf_path: str) -> str:
    pdf = fitz.open(pdf_path)

    text = ""

    for page in pdf:
        text += page.get_text()

    return text