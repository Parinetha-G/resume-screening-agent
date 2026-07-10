import os

from utils.parser import read_pdf, read_txt
from utils.similarity import calculate_similarity
from utils.llm import analyze_resume

# Read Job Description
jd = read_txt("data/job_description/software_engineer_jd.txt")

results = []

# Loop through all resumes
resume_folder = "data/resumes"

for file in os.listdir(resume_folder):

    if file.endswith(".pdf"):

        resume_path = os.path.join(resume_folder, file)

        print(f"\nAnalyzing {file}...")

        # Read Resume
        resume = read_pdf(resume_path)

        # Calculate Similarity
        score = calculate_similarity(resume, jd)

        # AI Analysis
        analysis = analyze_resume(resume, jd, score)

        # Save Result
        results.append({
            "resume": file,
            "score": score,
            "analysis": analysis
        })

# Sort by highest score
results = sorted(results, key=lambda x: x["score"], reverse=True)

print("\n" + "=" * 60)
print("RESUME SCREENING RESULTS")
print("=" * 60)

for i, result in enumerate(results, start=1):

    print(f"\nRank #{i}")
    print(f"Resume : {result['resume']}")
    print(f"Score  : {result['score']:.2f}%")

    print("\nAI Analysis")
    print(result["analysis"])

    print("-" * 60)