import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Page config
st.set_page_config(page_title="JobAI Pro", page_icon="💼", layout="wide")
# LOAD DATA
jobs = pd.read_csv('jobs.csv')
jobs['combined'] = jobs['required_skills'] + " " + jobs['experience_level'] + " " + jobs['education_required']

# ML ENGINE (Using ngram_range for smarter skill matching) 
vectorizer = TfidfVectorizer(ngram_range=(1, 2))
tfidf_matrix = vectorizer.fit_transform(jobs['combined'])

#Sidebar
st.sidebar.header("Project Metrics")
st.sidebar.metric("Total Jobs Indexed", len(jobs))
st.sidebar.info("Model: Content-Based Filtering using TF-IDF & Cosine Similarity.")

# Main UI 
st.title("💼 Intelligent Job Recommendation Platform")
tab1, tab2 = st.tabs(["🚀 Find Jobs", "⚙️ Methodology"])

with tab1:
    with st.form("profile_form"):
        col1, col2, col3 = st.columns(3)
        with col1: skills = st.text_input("Skills (e.g. Python, SQL)")
        with col2: edu = st.selectbox("Education", ['Bachelors', 'Masters', 'PhD'])
        with col3: exp = st.select_slider("Experience", ['Entry', 'Mid', 'Senior'])
        submitted = st.form_submit_button("Find Matches")

    if submitted:
        user_input = f"{skills} {exp} {edu}"
        user_vec = vectorizer.transform([user_input])
        scores = cosine_similarity(user_vec, tfidf_matrix).flatten()
        top_indices = scores.argsort()[-5:][::-1]

        for i in top_indices:
            job = jobs.iloc[i]
            # Calculating percentage match
            match_score = scores[i] * 100
            
            with st.expander(f"📍 {job['job_title']} ({match_score:.1f}% Match)"):
                st.write(f"**Required Skills:** {job['required_skills']}")
                st.write(f"**Experience Level:** {job['experience_level']}")
                #  progress bar 
                st.progress(scores[i])

with tab2:
    st.write("### How we engineered this:")
    st.markdown("- **Vectorization:** Used `TfidfVectorizer(ngram_range=(1,2))` to capture skill-phrases.")
    st.markdown("- **Similarity:** Used `cosine_similarity` to calculate vector distance.")
    st.markdown("- **Scalability:** The model is pre-computed, allowing for sub-millisecond recommendations.")
    st.markdown("Made by team no: 25") #can remove or change if necessary
    st.markdown("You can access or take a look at the project through the github like provided : https://github.com/Pushkaraj2/mlproj.git")# can be removed or changed if necessary...