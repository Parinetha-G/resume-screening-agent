from utils.parser import read_pdf, read_txt
from utils.similarity import calculate_similarity

# Read resume
resume = read_pdf("data/resumes/sample_resume_1.pdf")

# Read Job Description
jd = read_txt("data/job_description/software_engineer_jd.txt")

score = calculate_similarity(resume, jd)

print(f"Resume Match Score: {score}%")