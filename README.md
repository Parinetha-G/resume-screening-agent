# AI Resume Screening Agent
## Live Demo

https://resume-screening-agent-ppnejfjqbb5jpn49avyb8u.streamlit.app/

## Overview

The AI Resume Screening Agent is an intelligent application that helps recruiters evaluate resumes against a job description. It uses Natural Language Processing (NLP) to calculate a similarity score and a Large Language Model (Groq Llama) to generate detailed resume analysis and hiring recommendations.

This project was developed as part of the **Rooman AI Challenge**.

---

## Features

- Upload a Job Description (.txt)
- Upload one or more Resume PDFs
- Extract text from PDF resumes
- Calculate resume-job similarity using Sentence Transformers
- Generate AI-powered resume analysis
- Rank resumes based on similarity score
- Download results as a CSV file
- Interactive Streamlit web interface

---

## Technologies Used

- Python 3.x
- Streamlit
- Sentence Transformers
- Hugging Face
- Groq API (Llama Model)
- PyPDF2
- Pandas
- python-dotenv

---

## Project Structure

```
resume-screening-agent/
│
├── data/
│   ├── resumes/
│   └── job_description/
│
├── utils/
│   ├── parser.py
│   ├── similarity.py
│   └── llm.py
│
├── app.py
├── streamlit_app.py
├── test_ai.py
├── test_similarity.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

## Installation

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd resume-screening-agent
```

### 2. Create a virtual environment

Windows

```bash
py -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configure API Key

Create a file named `.env`

Add your Groq API Key

```env
GROQ_API_KEY=your_api_key_here
```

---

## Run the Application

```bash
streamlit run streamlit_app.py
```

The application will open in your browser.

---

## How It Works

1. Upload the Job Description.
2. Upload one or more resumes.
3. Click **Analyze**.
4. The application:
   - Extracts text from resumes.
   - Calculates semantic similarity.
   - Uses Groq Llama to analyze each resume.
   - Ranks candidates by score.
5. Download the results as a CSV file.

---

## Sample Output

| Resume | Score | Recommendation |
|---------|------:|----------------|
| Resume1.pdf | 91.25 | Shortlist |
| Resume2.pdf | 82.60 | Maybe |
| Resume3.pdf | 67.80 | Reject |

---

## Future Improvements

- Support DOCX resumes
- Skill extraction dashboard
- Interview question generation
- Resume keyword highlighting
- Database integration
- Authentication for recruiters

---

## Author

**Parinetha**

Developed for the Rooman AI Challenge.