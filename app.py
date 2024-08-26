from pathlib import Path
import streamlit as st
from PIL import Image
import json

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Resume (3).pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital Resume | Sakshi Jain"
PAGE_ICON = ":wave:"
NAME = "Sakshi Jain"
DESCRIPTION = """
Data Science Engineer with a strong foundation in AI and Machine Learning, skilled in Python, Data Analysis, and deploying scalable applications.
"""
EMAIL = "sakshisanghi0001@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/sakshi-jain-509728226/",
    "Github": "https://github.com/shithead999",
    "Kaggle": "https://www.kaggle.com/sakshijain27",
    "Medium": "https://medium.com/@sakshisanghi0001"
}
PROJECTS = {
    "🏆 Genetic Algorithm - Solved Shakespeare's monkey example": "https://github.com/shithead999/genetic_algorithm",
    "🏆 The Movie Library - Creates a list based on your preferences and suggests you the movies": "https://the-movie-library-b6b3.onrender.com/",
    "🏆 Movie Recommendation System - Recommends movies on the trained dataset": "https://bit.ly/3VdGEIX",
    "🏆 Sentiment Analysis - Analyzed Amazon food reviews": "https://www.kaggle.com/code/sakshijain27/sentimental-analysis-on-amazon-food-reviews"
}

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=210)  # Keep the original width
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/pdf"
    )
    st.write("📧", EMAIL)

# --- SOCIAL MEDIA LINKS ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- EXPERIENCE AND QUALIFICATIONS ---
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
    - 🎓 **Solid Academic Foundation:** Strong educational background in Artificial Intelligence and Data Science Engineering, with a focus on Machine Learning applications.
    - 📊 **Data Science Expertise:** Extensive experience in Data Analysis, Visualization, and Modeling, with a deep understanding of statistical principles and their practical applications.
    - 💡 **Machine Learning Proficiency:** Proven ability to design, develop, and deploy Machine Learning models for various applications, including predictive analytics, recommendation systems, and sentiment analysis.
    - 🔍 **Data-Driven Decision Making:** Adept at extracting actionable insights from complex datasets to inform business strategy and decision-making.
    - 🌐 **Web Development Skills:** Skilled in developing and deploying full-stack web applications using modern frameworks like Django and Flask.
    - 🤝 **Team Collaboration:** Strong team player with experience in working within cross-functional teams to achieve shared objectives.
    - 💼 **Professional Experience:** A track record of success in various internships and roles, showcasing adaptability and continuous learning.
    """
)

# --- SKILLS ---
st.write("#")
st.subheader("Skills")
st.write(
    """
    - 👩🏻‍💻 **Programming Languages:** Python, SQL, C/C++, MATLAB
    - 🛠️ **Libraries & Frameworks:** Numpy, Pandas, Matplotlib, Seaborn, Scikit-learn, TensorFlow, Keras, OpenCV
    - 📊 **Data Visualization Tools:** Power BI, MS Excel, Plotly, Matplotlib
    - 🧠 **Machine Learning & AI:** Supervised and Unsupervised Learning, Neural Networks, Deep Learning, NLP, Reinforcement Learning
    - 🗄️ **Database Management:** MySQL, PostgreSQL, MongoDB
    - 🖥️ **Web Development:** Django, Flask, HTML, CSS, JavaScript
    - 🛠️ **Development Tools:** Git, Docker, Kubernetes, Jenkins, JIRA, Azure DevOps
    - 📝 **Soft Skills:** Team Leadership, Communication, Problem-Solving, Time Management, Collaboration
    """
)

# --- WORK HISTORY ---
st.write("#")
st.subheader("Work History")
st.write("----")

st.write("### 📊 Associate Data Science Educator | Geekster")
st.write("**December 2023 - May 2024**")
st.write(
    """
    - Implemented advanced data scraping techniques using Selenium and BeautifulSoup, significantly improving the efficiency of information retrieval processes.
    - Led the design and development of student-focused applications, collaborating with cross-functional teams to ensure project success.
    - Conducted comprehensive data analysis, delivering insights that guided strategic decision-making and fostered external partnerships.
    - Enhanced data retrieval speeds by 30%.
    - Successfully launched 2 student-focused applications, impacting over 500 students.
    - Presented data-driven insights that led to 3 new collaborations with external partners.
    """
)

st.write("### 📈 Data Science Intern | Clarista")
st.write("**July 2023 - October 2023**")
st.write(
    """
    - Developed a real-time food notification application using Python, Django, and PostgreSQL, ensuring robust deployment with Docker and Kubernetes.
    - Analyzed data from 10,000 users, optimizing database performance and user interaction.
    - Trained and deployed advanced language models (Code Llama, Mistral 7B), creating custom APIs for seamless data interaction.
    - Created a regression model to predict critical temperatures, achieving high accuracy with an R2-score of up to 0.907 using Random Forest.
    - Deployed a scalable application serving over 5,000 daily active users.
    - Improved prediction accuracy in healthcare and environmental domains by up to 20%.
    - Contributed to the reduction of readmission rates by 15% in healthcare and optimized fault prediction in wastewater treatment.
    """
)

st.write("### 🎰 Machine Learning Trainee | Internshala")
st.write("**November 2022 - January 2023**")
st.write(
    """
    - Developed proficiency in creating Linear and Logistic regression models.
    - Demonstrated expertise in implementing Dimensionality reduction techniques.
    - Acquired knowledge and experience in utilizing Decision Tree algorithms.
    - Gained valuable expertise in implementing Clustering methods.
    - Successfully collaborated with team members to achieve project goals.
    - Conducted thorough research and analysis to inform project decision-making processes.
    - Displayed exceptional problem-solving skills and critical thinking abilities.
    - Adapted quickly to changing project requirements and timelines.
    """
)

# --- PROJECTS ---
st.write("#")
st.subheader("Projects")
st.write("----")
for project, link in PROJECTS.items():
    st.write(f"🔗 [{project}]({link})")

# --- BLOGS ---
st.write("#")
st.subheader("Blogs")
st.write("----")
with open("blogs.json") as blogs_json:
    data = json.load(blogs_json)
col1, col2 = st.columns(2, gap="small")
count = 0
for post in data:
    title = post["title"]
    link = post["url"]
    publish_date = post["date"]
    thumbnail = post["thumbnail_url"]

    with col2 if count % 2 else col1:
        st.image(thumbnail, width=300)
        st.header(title)
        st.write(f"Published on: {publish_date.split()[0]}")
        st.write(f"[Read more]({link})")
    count += 1
