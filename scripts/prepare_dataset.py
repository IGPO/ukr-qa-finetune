import fitz  # PyMuPDF
import re

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    pages = []
    for page in doc:
        text = page.get_text()
        text = clean_text(text)
        if len(text.strip()) > 50:
            pages.append(text.strip())
    return pages

def clean_text(text):
    # Удаляем лишние пробелы, номера страниц, формулы, мусор
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r'\s{2,}', ' ', text)
    text = re.sub(r'Рис\..*|Табл\..*', '', text)
    text = re.sub(r'[^\S\r\n]{2,}', ' ', text)
    return text.strip()

# Пример вызова
pages = extract_text_from_pdf("Disser_Popov.pdf")
for i, p in enumerate(pages[:3]):
    print(f"Page {i+1}:\n{p[:500]}...\n")
