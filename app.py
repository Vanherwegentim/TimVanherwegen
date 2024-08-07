import streamlit as st
from PIL import Image

# Set up the page configuration
st.set_page_config(
    page_title="Tim Vanherwegen - Machine Learning Engineer",
    page_icon=":computer:",
    layout="wide",
    initial_sidebar_state="auto",
)

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f5f5f5;
        padding: 20px;
        border-radius: 10px;

    }
    .header {
        background-color: #4CAF50;
        color: white;
        padding: 10px;
        text-align: center;
        border-radius: 10px;
        border-style: solid;

    }
    .section-title {
        color: #4CAF50;
        border-bottom: 2px solid #4CAF50;
        padding-bottom: 5px;
        margin-bottom: 10px;
    }
    .contact-info {
        background-color: #ffffff;
        padding: 10px;
        border-radius: 10px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    }
    .project, .experience {
        background-color: #ffffff;
        padding: 10px;
        border-radius: 10px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        margin-bottom: 10px;
    }
    .footer {
        text-align: center;
        padding: 10px;
        color: #777777;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header Section
st.markdown('<div class="header"><h1>Tim Vanherwegen</h1><h3>Machine Learning Engineer</h3></div>', unsafe_allow_html=True)

# About Me Section
st.markdown('<h2 class="section-title">About Me</h2>', unsafe_allow_html=True)

c1,c2,c3 = st.columns([1,2,1])
col1, col2 = c2.columns([0.5, 0.5])

with col1:
    image = Image.open("images/tim.jpg")  # Replace with the path to your image
    st.image(image, caption='Tim Vanherwegen', width=400)

with col2:
    st.write(
        """
        <div style='font-size: 18px; line-height: 1.6; color: #333333; font-family: Arial, sans-serif;'>
        I am a dedicated and passionate Machine Learning Engineer with a strong background in developing innovative solutions to complex problems. 
        With a keen interest in artificial intelligence and data science, I am always eager to learn new technologies and apply them in real-world scenarios.
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown(
    """
    <style>
    .section-title {
        color: #4CAF50;
        border-bottom: 2px solid #4CAF50;
        padding-bottom: 5px;
        font-size: 24px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)



# Skills Section
st.markdown('<h2 class="section-title">Skills</h2>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.subheader("Programming Languages")
    st.write(
        """
        - Python
        - Java
        - JavaScript
        - Java
        - C++
        - SQL
        """
    )
with col2:
    st.subheader("Technologies & Tools")
    st.write(
        """
        - TensorFlow / Keras
        - PyTorch
        - Scikit-Learn
        - Pandas / NumPy
        - Docker
        - Streamlit
        - Git / GitHub
        - NLP
        - OCR
        """
    )

# Experience Section
st.markdown('<h2 class="section-title">Experience</h2>', unsafe_allow_html=True)
st.markdown('<div class="experience"><h3>Fintrax - AI developer (One day/Week)</h3>', unsafe_allow_html=True)
st.write(
    """
    **Duration:** Sep 2023 - Juli 2024
    - Developed an LLM application to assist people with their financial decisions.
    - Used a knowledge base to provide the user with the best possible advice.
    """
)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div class="experience"><h3>Student Entrepreneur - Software Developer</h3>', unsafe_allow_html=True)
st.write(
    """
    **Duration:** Jan 2020 - June 2020
    - Created web applications for several small companies.
    - Worked on small Access projects for an engineering company.
    """
)
st.markdown('</div>', unsafe_allow_html=True)

# Intership Section
st.markdown('<h2 class="section-title">Interships</h2>', unsafe_allow_html=True)
st.markdown('<div class="experience"><h3>Nazka Mapps - Full Stack Developer</h3>', unsafe_allow_html=True)
st.write(
    """
    **Duration:** May 2021 - June 2021
    - Worked on a project to allow people to create their own custom maps
    - Used new technologies like react, node.js and mongoDB
    """
)
st.markdown('</div>', unsafe_allow_html=True)

# Projects Section
st.markdown('<h2 class="section-title">Projects</h2>', unsafe_allow_html=True)
st.write("Here are some of my notable projects. You can find more on my [GitHub](https://github.com/Vanherwegentim).")
st.markdown('<div class="project"><h3>Project 1: Awesome Heart Disease Predictor</h3>', unsafe_allow_html=True)
st.write(
    """
    - **Description:** Developed a machine learning model to predict people's heart disease risk and made an LLM available that can inform them of more information and offer them a way to reduce their risk based on their profile.
    - **Technologies Used:** Python, TensorFlow, Pandas, NumPy, Streamlit, Langchain
    - **Link:** [GitHub](https://github.com/Vanherwegentim/CanYouHelpPeopleWithTheirHeartDiseaseRisk)
    """
)
st.markdown('</div>', unsafe_allow_html=True)

# Education Section
st.markdown('<h2 class="section-title">Education</h2>', unsafe_allow_html=True)
st.write("### University KU Leuven")
st.write(
    """
    **Degree:** Master in Computer Science - Artificial Intelligence
    **Duration:** 2022 - 2024
    """
)

# Contact Information
st.markdown('<h2 class="section-title">Contact Information</h2>', unsafe_allow_html=True)
st.markdown('<div class="contact-info">', unsafe_allow_html=True)
st.write("Feel free to reach out to me via the following platforms:")
st.write(
    """
    - **Email:** [tim.vanherwegen.tv@gmail.com](mailto:tim.vanherwegen.tv@gmail.com)
    - **LinkedIn:** [https://www.linkedin.com/in/tim-vanherwegen-0988161a2/](https://www.linkedin.com/in/tim-vanherwegen-0988161a2/)
    - **GitHub:** [https://github.com/Vanherwegentim](https://github.com/Vanherwegentim)
    """
)
st.markdown('</div>', unsafe_allow_html=True)

# Footer Section
st.markdown('<div class="footer">© 2024 Tim Vanherwegen. All rights reserved.</div>', unsafe_allow_html=True)
