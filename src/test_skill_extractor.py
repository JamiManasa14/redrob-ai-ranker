from read_jd import read_job_description
from skill_extractor import extract_skills

jd = read_job_description("data/job_description.docx")

skills = extract_skills(jd)

print("\nExtracted Skills\n")

for skill in skills:
    print(skill)