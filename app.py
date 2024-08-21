from pathlib import Path
import streamlit as st
from PIL import Image
import requests
import json

# --- PATH SETTINGS---
current_dir=Path(__file__).parent if "__file__" in locals() else Path.cwd
css_file= current_dir/"styles"/"main.css"
resume_file=current_dir/"assets"/"Resume (3).pdf"
profile_pic=current_dir/"assets"/"profile-pic.png"



# --- General settings---
PAGE_TITLE="Digital Resume | Sakshi Jain"
PAGE_ICON=":wave:"
NAME="Sakshi Jain"
DESCRIPTION= """
Data Science Engineer
"""
EMAIL="sakshisanghi0001@gmail.com"
SOCIAL_MEDIA={
    "LinkedIn":"https://www.linkedin.com/in/sakshi-jain-509728226/",
    "Github" : "https://github.com/shithead999",
    "Kaggle":"https://www.kaggle.com/sakshijain27",
    "Medium":"https://medium.com/@sakshisanghi0001"
}
PROJECTS ={
    "🏆" "Genetic Algorithm -Solved Shakespeare's monkey example":"https://github.com/shithead999/genetic_algorithm",
    "🏆" "Movie Recommendation System -Recommends movie on the trained dataset":"https://bit.ly/3VdGEIX",
    "🏆" "Sentimental Analysis -Sentimental Analysis on Amazon food review":"https://www.kaggle.com/code/sakshijain27/sentimental-analysis-on-amazon-food-reviews"
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC----
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)
with open(resume_file,"rb") as pdf_file:
    PDFbyte=pdf_file.read()
profile_pic=Image.open(profile_pic)


#--HERO---
col1,col2=st.columns(2,gap="small")
with col1:
    st.image(profile_pic,width=210)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📃 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📧",EMAIL)

    #----Social Links---
    st.write("#")
    cols=st.columns(len(SOCIAL_MEDIA))
    for index,(platform,link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")



#--Experience and Qualification---
st.write("#")
st.subheader("Experience & Qualification")
st.write(
    """ 
- ✓ **Strong hands on experience and knowledge in Python and Excel**
- ✓ **Experienced in Data Analysis, Data Visualization, Data Cleaning, Data Modelling, Data Wrangling**
- ✓ **Good understanding of statistical principles and their respective application**
- ✓ **Experienced in extracting actionable insight from data**
- ✓ **Experienced in building Machine Learning models**
- ✓ **Excellent team-player and displaying stong sense of intiative on task**
     """

)


#---Skills---
st.write("#")
st.subheader("Skills")
st.write(
    """
    - 👩🏻‍💻Programming: Python,SQL,C/C++
    - 📚Libraries: Numpy, Pandas, Matplotlib, Seaborn, Scikit-learn, Tensorflow
    - 📊Data Visualisation: PowerBi, Ms Excel, Plotly
    - 📉Data Analysis
    - 🪧Modelling - Logestic Regression, linear regression, decision trees, gradient descent
    - 🎥Streamlit
    - 🗂️Git
    """
)


#--Work History---
st.write("#")
st.subheader("Work History")
st.write("----")

st.write("🎰","**Machine Learning Trainee** | Internshala ")
st.write("November 2022-January 2023")
st.write(
    """ 
   - Developed proficiency in creating Linear and Logistic regression models
   - Demonstrated expertise in implementing Dimensionality reduction techniques
   - Acquired knowledge and experience in utilizing Decision Tree algorithms
   - Gained valuable expertise in implementing Clustering methods
   - Successfully collaborated with team members to achieve project goals
   - Conducted thorough research and analysis to inform project decision-making processes
   - Displayed exceptional problem-solving skills and critical thinking abilities
   - Adapted quickly to changing project requirements and timelines.
    """
)


#--Projects---
st.write("#")
st.subheader("Projects")
st.write("----")
for project,link in PROJECTS.items():
    st.write(f"[{project}]({link})")


#--Blogs---
st.write("#")
st.subheader("Blogs")
st.write("----")

with open("blogs.json") as blogs_json:
    data = json.load(blogs_json)
col1,col2=st.columns(2,gap="small")
count=0
for post in data:
    title=post["title"]
    link=post["url"]
    publish_date=post["date"]
    thumbnail=post["thumbnail_url"]
    
    with col2 if count%2 else col1:
        st.write("#")
        st.image(thumbnail,width=300)
        st.header(title)
        st.write(f"Published on: {publish_date.split()[0]}")
        st.write(f"[Read more]({link})")
    count+=1
