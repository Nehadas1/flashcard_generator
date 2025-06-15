import fitz   # PyMuPDF

def extract_text_from_pdf(uploaded_file):
    try:
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        return text.strip() if text else " Could not extract readable text from the PDF."
    except Exception as e:
        return f" Error reading PDF: {str(e)}"

def extract_text_from_txt(uploaded_file):
    try:
        return uploaded_file.read().decode("utf-8")
    except Exception as e:
        return f" Error reading TXT: {str(e)}"
