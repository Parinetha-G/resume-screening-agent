import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

# Load local .env (for running on your laptop)
load_dotenv()

# Use Streamlit Secrets if available, otherwise use .env
api_key = st.secrets.get("GROQ_API_KEY", os.getenv("GROQ_API_KEY"))

client = Groq(api_key=api_key)


def analyze_resume(resume_text, jd_text, score):
    prompt = f"""
You are an expert HR recruiter.

Job Description:
{jd_text}

Resume:
{resume_text}

Similarity Score:
{score:.2f}%

Analyze the resume and provide:

1. Overall Recommendation (Shortlist / Maybe / Reject)
2. Matching Skills
3. Missing Skills
4. Strengths
5. Weaknesses
6. A short explanation for your decision.
"""

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an experienced HR recruiter."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
    )

    return completion.choices[0].message.content