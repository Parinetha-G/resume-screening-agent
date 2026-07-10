from utils.parser import read_pdf, read_txt
from utils.similarity import calculate_similarity
from utils.llm import analyze_resume

# Read Resume
resume = read_pdf("data/resumes/sample_resume_1.pdf")

# Read Job Description
jd = read_txt("data/job_description/software_engineer_jd.txt")

# Calculate Similarity
score = calculate_similarity(resume, jd)

print(f"Resume Match Score: {score:.2f}%\n")

# AI Analysis
analysis = analyze_resume(resume, jd, score)

print(analysis)