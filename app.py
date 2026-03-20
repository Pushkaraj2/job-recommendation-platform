import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# DATA CONFIG
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

skill_icons = {
    'Python': '🐍', 'SQL': '🗄️', 'Java': '☕', 'Machine Learning': '🤖', 'Data Analysis': '📊', 
    'HTML': '🌐', 'CSS': '🎨', 'React': '⚛️', 'AWS': '☁️', 'Docker': '🐳', 'Kubernetes': '☸️', 
    'Tableau': '📉', 'JavaScript': '📜', 'TypeScript': '📘', 'Flutter': '📱', 'Kotlin': '🤖',
    'Swift': '🍎', 'Figma': '🖌️', 'Selenium': '🔍', 'Terraform': '🏗️', 'Azure': '☁️', 
    'Solidity': '⛓️', 'Node.js': '🟢', 'Pandas': '🐼', 'TensorFlow': '🧠', 'PyTorch': '🔥', 'PostgreSQL': '🐘'
}

# Initialization
st.set_page_config(page_title="Job recommendation 🧙‍♂️", layout="wide")
jobs = pd.read_csv('jobs.csv')
jobs['combined'] = jobs['required_skills'] + " " + jobs['experience_level'] + " " + jobs['education_required']

vectorizer = TfidfVectorizer(ngram_range=(1, 2))
tfidf_matrix = vectorizer.fit_transform(jobs['combined'])
all_skills = sorted(list(set([skill for sublist in roles_tech.values() for skill in sublist])))

# UI layout
st.title("💼 Intelligent Job Recommendation Platform")
tab1, tab2 = st.tabs(["🧙‍♂️ Find Jobs", "⚙️ Methodology"])

with tab1:
    with st.form("search_form"):
        col1, col2, col3 = st.columns(3)
        with col1: selected_skills = st.multiselect("Select your skills:", all_skills)
        with col2: edu = st.selectbox("Education", ['Bachelors', 'Masters', 'PhD'])
        with col3: exp = st.select_slider("Experience", ['Entry', 'Mid', 'Senior'])
        submitted = st.form_submit_button("Search Matching Roles")

    if submitted:
        if not selected_skills:
            st.warning("Please select at least one skill!")
        else:
            skills_str = ", ".join(selected_skills)
            user_vec = vectorizer.transform([f"{skills_str} {exp} {edu}"])
            scores = cosine_similarity(user_vec, tfidf_matrix).flatten()
            top_indices = scores.argsort()[-5:][::-1]

            st.success("Top recommendations based on your profile:")
            for i in top_indices:
                job = jobs.iloc[i]
                skill_list = [f"{skill_icons.get(s.strip(), '⚡')} {s}" for s in job['required_skills'].split(', ')]
                
                with st.expander(f"📍 {job['job_title']} ({int(scores[i]*100)}% Match)"):
                    st.write(f"**Required:** {' | '.join(skill_list)}")
                    st.write(f"**Level:** {job['experience_level']} | **Education:** {job['education_required']}")
                    st.progress(float(scores[i]))

with tab2:
    st.header("Behind the Engine")
    st.markdown("""
    This project demonstrates an end-to-end Machine Learning pipeline:
    1. **Data Engineering:** Automated synthetic data generation for diverse industry roles.
    2. **Vectorization:** Using `TF-IDF` to convert unstructured text into high-dimensional numerical space.
    3. **Similarity Analysis:** Using `Cosine Similarity` to rank job relevancy for specific candidate profiles.
    """)
    st.markdown("""
    This project was built by **Team no: 25**
    1. You can also view the code for the project using the given link: 
       https://github.com/Pushkaraj2/job-recommendation-platform
    """)# You can comment out this line or remove it completely...