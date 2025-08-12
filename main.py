import os
import streamlit as st
from dotenv import load_dotenv
from helper import extract_all_resumes, extract_job_description
from langchain.chat_models import AzureChatOpenAI

# Load .env values
load_dotenv()

st.title("📄 Resume Ranker using Azure OpenAI")

# File uploaders
jd_file = st.file_uploader("Upload Job Description PDF (name it job_description.pdf)", type="pdf")
resume_files = st.file_uploader("Upload up to 10 Resume PDFs", type="pdf", accept_multiple_files=True)

if jd_file and resume_files:
    # Save JD
    jd_path = os.path.join("resumes", "job_description.pdf")
    with open(jd_path, "wb") as f:
        f.write(jd_file.getbuffer())

    # Save resumes
    for file in resume_files:
        save_path = os.path.join("resumes", file.name)
        with open(save_path, "wb") as f:
            f.write(file.getbuffer())

    st.success("✅ All files uploaded!")

    # Extract text
    st.info("📄 Extracting text from resumes and JD...")
    jd_text = extract_job_description("resumes")
    resume_dict = extract_all_resumes("resumes")

    # Azure Chat LLM setup
    llm = AzureChatOpenAI(
        azure_endpoint=os.getenv("AZUREOPENAI_API_BASE"),
        openai_api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        openai_api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
        model_name="gpt-4o",
        temperature=0.3,
        validate_base_url=False
    )

    results = []
    for name, resume_text in resume_dict.items():
        prompt = f"""
        You are an expert recruiter.
        Compare this resume to the job description and score it out of 100.
        
        Job Description:
        {jd_text}

        Resume:
        {resume_text}

        Reply ONLY with:
        - Resume: <filename>
        - Score: <score out of 100>
        - Reason: <brief justification>
        """
        response = llm.invoke(prompt)
        results.append((name, response.content))

    # Sort and show results
    st.subheader("📊 Ranked Resumes")
    for name, result in sorted(results, key=lambda x: int(''.join(filter(str.isdigit, x[1]))), reverse=True):
        st.markdown(f"**{name}**")
        st.write(result)
        st.markdown("---")
