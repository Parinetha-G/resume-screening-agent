import streamlit as st
import pandas as pd
import tempfile
import os

from utils.parser import read_pdf, read_txt
from utils.similarity import calculate_similarity
from utils.llm import analyze_resume

st.set_page_config(page_title="Resume Screening Agent", layout="wide")

st.title("📄 AI Resume Screening Agent")
st.write("Upload a Job Description and one or more resumes.")

# Upload Job Description
jd_file = st.file_uploader(
    "Upload Job Description (.txt)",
    type=["txt"]
)

# Upload Resumes
resume_files = st.file_uploader(
    "Upload Resume(s) (.pdf)",
    type=["pdf"],
    accept_multiple_files=True
)

if st.button("Analyze"):

    if jd_file is None or len(resume_files) == 0:
        st.warning("Please upload a Job Description and at least one resume.")
    else:

        # Save JD temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".txt") as temp_jd:
            temp_jd.write(jd_file.read())
            jd_path = temp_jd.name

        jd_text = read_txt(jd_path)

        results = []

        for resume in resume_files:

            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_resume:
                temp_resume.write(resume.read())
                resume_path = temp_resume.name

            resume_text = read_pdf(resume_path)

            score = calculate_similarity(resume_text, jd_text)

            analysis = analyze_resume(resume_text, jd_text, score)

            results.append({
                "Resume": resume.name,
                "Score": round(score, 2),
                "Analysis": analysis
            })

        results.sort(key=lambda x: x["Score"], reverse=True)

        st.success("Analysis Completed!")

        df = pd.DataFrame(results)

        st.subheader("Resume Ranking")

        st.dataframe(df[["Resume", "Score"]])

        st.download_button(
            label="Download Results CSV",
            data=df.to_csv(index=False),
            file_name="results.csv",
            mime="text/csv"
        )

        st.subheader("Detailed Analysis")

        for result in results:

            with st.expander(result["Resume"]):

                st.write(f"### Match Score: {result['Score']}%")
                st.write(result["Analysis"])