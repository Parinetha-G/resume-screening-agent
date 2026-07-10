import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

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