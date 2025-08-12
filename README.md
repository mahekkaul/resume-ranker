Resume Ranker

📌 Overview
Resume Ranker is a Python-based tool that automatically scores and ranks resumes based on job description requirements.  
It uses Natural Language Processing (NLP) techniques to extract key skills, compare them against the job criteria, and assign a ranking score to each candidate.

This helps recruiters quickly shortlist the most relevant candidates without manually scanning each resume.


✨ Features
- Extracts text from PDF/DOCX resumes.
- Compares candidate skills to job requirements.
- Generates ranking scores for each candidate.
- Supports batch processing of multiple resumes.
- Outputs results in CSV/Excel format for easy review.


 🛠️ Tech Stack
- **Python** 3.x
- **Libraries:** `pandas`, `numpy`, `spacy`, `nltk`, `pdfplumber`, `python-docx`
- **File Formats Supported:** `.pdf`, `.docx`


📂 Project Structure
resume-ranker/
│── data/ # Sample resumes & job descriptions
│── output/ # Ranked results CSV/Excel
│── src/ # Main Python scripts
│ ├── extract_text.py
│ ├── rank_resumes.py
│ └── utils.py
│── requirements.txt # Dependencies
│── README.md # Project documentation
│── main.py # Main entry point


🚀 Installation & Usage:-

1️⃣ Clone the repository

git clone https://github.com/YOUR_USERNAME/resume-ranker.git
cd resume-ranker

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the project
python main.py --job "job_description.txt" --resumes "data/"


📊 Example Output
Candidate Name	Score	Matched Skills
John Doe	85%	Python, SQL, NLP
Jane Smith	72%	Java, Data Analysis

🤝 Contributing
Contributions, issues, and feature requests are welcome!

📄 License
This project is licensed under the MIT License.

👤 Author
Made with ❤️ by Mahek Kaul
