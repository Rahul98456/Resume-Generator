import streamlit as st
from resume_generator import generate_resume
from utils import clean_resume_text
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set up Google API Key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Streamlit App
st.title("SmartResume Generator")
st.write("Welcome to the SmartResume Generator! Enter your details below to create a customized resume.")

# Input fields for user details
name = st.text_input("Enter your name:", key="name_input")  # Unique key
job_title = st.text_input("Enter your desired job title:", key="job_title_input")  # Unique key

# Button to generate resume
if st.button("Generate Resume"):
    if name and job_title:
        # Generate the resume
        resume_text = generate_resume(name, job_title)
        
        # Clean the resume text
        cleaned_resume = clean_resume_text(resume_text)
        
        # Display the generated resume
        st.subheader("Generated Resume:")
        st.write(cleaned_resume)
        
        # Option to download the resume
        st.download_button(
            label="Download Resume",
            data=cleaned_resume,
            file_name=f"{name}_Resume.txt",
            mime="text/plain"
        )
    else:
        st.error("Please enter your name and job title.")