import pandas as pd
import random

# Configuration
num_jobs = 100
num_candidates = 50
skills_pool = ['Python', 'SQL', 'Java', 'Machine Learning', 'Data Analysis', 
               'HTML', 'CSS', 'React', 'Cloud Computing', 'Project Management']
roles = ['Data Scientist', 'Software Engineer', 'Frontend Developer', 'Data Analyst', 'Project Manager']
education_levels = ['Bachelors', 'Masters', 'PhD']

# Create Data
jobs = pd.DataFrame([{
    'job_id': i + 1001,
    'job_title': random.choice(roles),
    'required_skills': ", ".join(random.sample(skills_pool, 3)),
    'experience_level': random.choice(['Entry', 'Mid', 'Senior']),
    'education_required': random.choice(education_levels)
} for i in range(num_jobs)])

candidates = pd.DataFrame([{
    'candidate_id': i + 1,
    'candidate_name': f"Candidate_{i+1}",
    'skills': ", ".join(random.sample(skills_pool, 3)),
    'experience_years': random.randint(0, 10),
    'education': random.choice(education_levels)
} for i in range(num_candidates)])

# Save
jobs.to_csv('jobs.csv', index=False)
candidates.to_csv('candidates.csv', index=False)
print("Data created: jobs.csv and candidates.csv")