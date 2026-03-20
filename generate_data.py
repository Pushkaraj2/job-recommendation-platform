import pandas as pd
import random

# The source of truth for your roles and skills
roles_tech = {
    'Data Scientist': ['Python', 'Machine Learning', 'SQL', 'Pandas', 'Statistics', 'TensorFlow', 'NLP'],
    'Frontend Developer': ['HTML', 'CSS', 'React', 'JavaScript', 'TypeScript', 'Tailwind', 'Redux'],
    'Backend Engineer': ['Java', 'Spring Boot', 'SQL', 'Docker', 'AWS', 'PostgreSQL', 'Microservices'],
    'Data Analyst': ['SQL', 'Excel', 'Tableau', 'Python', 'PowerBI', 'Pandas'],
    'DevOps Engineer': ['Docker', 'Kubernetes', 'AWS', 'Linux', 'Python', 'Terraform', 'CI/CD'],
    'Mobile Developer': ['Kotlin', 'Swift', 'Flutter', 'Dart', 'React Native', 'Android', 'iOS'],
    'Cloud Architect': ['AWS', 'Azure', 'Google Cloud', 'Terraform', 'Kubernetes', 'Networking'],
    'Cybersecurity Analyst': ['Network Security', 'Penetration Testing', 'Firewalls', 'Linux', 'Python', 'Encryption'],
    'UI/UX Designer': ['Figma', 'Adobe XD', 'Sketch', 'Prototyping', 'User Research', 'Wireframing'],
    'QA Engineer': ['Selenium', 'JUnit', 'Test Automation', 'Postman', 'Java', 'Python', 'Jenkins'],
    'AI/ML Engineer': ['PyTorch', 'TensorFlow', 'Python', 'Computer Vision', 'NLP', 'Deep Learning'],
    'Blockchain Developer': ['Solidity', 'Ethereum', 'Web3', 'Smart Contracts', 'Cryptography', 'Node.js']
}

jobs = []
for i in range(150):
    role = random.choice(list(roles_tech.keys()))
    # Select 3 unique skills from the role's stack
    skills = random.sample(roles_tech[role], min(3, len(roles_tech[role])))
    
    jobs.append({
        'job_id': i + 1001,
        'job_title': role,
        'required_skills': ", ".join(skills),
        'experience_level': random.choice(['Entry', 'Mid', 'Senior']),
        'education_required': random.choice(['Bachelors', 'Masters', 'PhD'])
    })

pd.DataFrame(jobs).to_csv('jobs.csv', index=False)
print("jobs.csv created successfully with 150 diverse roles.")