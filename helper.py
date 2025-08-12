import fitz  # PyMuPDF
import os

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        doc = fitz.open(pdf_path)
        for page in doc:
            text += page.get_text()
        doc.close()
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
    return text

def extract_all_resumes(resume_folder):
    resumes = {}
    for filename in os.listdir(resume_folder):
        if filename.lower().endswith(".pdf") and filename != "job_description.pdf":
            full_path = os.path.join(resume_folder, filename)
            text = extract_text_from_pdf(full_path)
            resumes[filename] = text
    return resumes

def extract_job_description(resume_folder):
    jd_path = os.path.join(resume_folder, "job_description.pdf")
    return extract_text_from_pdf(jd_path)
