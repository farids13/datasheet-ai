import PyPDF2

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() + "\n"
    except Exception as e:
        text = f"Error reading PDF: {str(e)}"
    return text

if __name__ == "__main__":
    pdf_path = "Pre-Event - AWS AI League Introduction.pdf"
    extracted_text = extract_text_from_pdf(pdf_path)
    print(extracted_text)
