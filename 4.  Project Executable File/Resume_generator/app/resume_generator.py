import os
import google.generativeai as genai

# Set up Google API Key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Function to generate resume using Google Generative AI API
def generate_resume(name, job_title):
    """
    Generates a resume using Google's Gemini API.
    """
    # Create the model
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    # Create a chat session with the model
    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [
                    f"Create a professional resume for {name} applying for the role of {job_title}. \nThe resume should include the following sections:\n1. **Summary**: A concise overview of {name}'s professional background, highlighting key skills and achievements.\n2. **Skills**: A bullet-point list of technical skills (e.g., Python, Machine Learning) and soft skills (e.g., Communication, Teamwork).\n3. **Experience**: Detailed descriptions of previous job roles, including:\n   - Job Title\n   - Company Name\n   - Duration (Start Date - End Date)\n   - Key Responsibilities and Achievements (use bullet points)\n4. **Education**: Academic qualifications, including:\n   - Degree (e.g., Bachelor of Science in Computer Science)\n   - Institution (e.g., [Your University Name])\n   - Graduation Year (e.g., [Your Graduation Year])\n\nUse placeholders for personal details like:\n- Email: [Your Email Address]\n- Phone: [Your Phone Number]\n- LinkedIn: [Your LinkedIn URL (optional)]\n- University: [Your University Name]\n- Graduation Year: [Your Graduation Year]\n\nEnsure the resume is well-formatted, professional, and tailored for the {job_title} role.\n",
                ],
            },
            {
                "role": "model",
                "parts": [
                    "**John Doe**\n[Your Phone Number] | [Your Email Address] | [Your LinkedIn URL (optional)]\n\n**Summary**\n\nHighly motivated and results-oriented Software Engineer with [Number] years of experience in designing, developing, and implementing software solutions. Proven ability to collaborate effectively within agile teams to deliver high-quality, scalable, and maintainable applications.  Expertise in [mention 2-3 key technologies e.g., Python, Java, Cloud technologies] and a strong commitment to continuous learning and innovation.  Seeking a challenging Software Engineer role where I can leverage my skills and experience to contribute to the success of a dynamic organization.\n\n**Skills**\n\n**Technical Skills:**\n\n* Programming Languages: Python, Java, C++, JavaScript, SQL\n* Frameworks/Libraries: Spring Boot, React, Angular, Node.js, TensorFlow, PyTorch\n* Databases: MySQL, PostgreSQL, MongoDB, NoSQL\n* Cloud Platforms: AWS (EC2, S3, Lambda), Google Cloud Platform (GCP), Azure\n* DevOps: Docker, Kubernetes, CI/CD\n* Version Control: Git\n* Testing: Unit testing, Integration testing\n\n\n**Soft Skills:**\n\n* Communication (written and verbal)\n* Teamwork and Collaboration\n* Problem-solving and analytical thinking\n* Time management and organization\n* Adaptability and flexibility\n\n\n**Experience**\n\n**Software Engineer** | Acme Corporation | June 2020 – Present\n* Developed and maintained key features for a high-traffic web application using Python and Django, resulting in a 20% increase in user engagement.\n* Implemented a new microservice architecture using Spring Boot, improving scalability and reducing deployment time by 30%.\n* Contributed to the development of a machine learning model using TensorFlow, improving the accuracy of a key business process by 15%.\n* Collaborated with cross-functional teams (design, product, QA) to deliver high-quality software releases on time and within budget.\n* Mentored junior engineers, providing technical guidance and support.\n\n\n**Junior Software Developer** | Beta Solutions | June 2018 – June 2020\n* Developed and maintained several web applications using Java and Spring MVC.\n* Implemented unit and integration tests to ensure high software quality.\n* Assisted senior developers in designing and implementing new features.\n* Gained experience in Agile software development methodologies.\n\n\n**Education**\n\n**Bachelor of Science in Computer Science** | [Your University Name] | [Your Graduation Year]\n\n\n**Projects (Optional - Include if relevant and impressive)**\n\n* [Project Name]: [Brief Description and Technologies Used]\n* [Project Name]: [Brief Description and Technologies Used]\n\n\nThis resume uses placeholders.  Remember to replace the bracketed information with your own details and tailor the skills and experience sections to match the specific requirements of the job description you are applying for.  Quantify your achievements whenever possible to demonstrate your impact.\n",
                ],
            },
        ]
    )

    # Generate the resume
    response = chat_session.send_message(f"Create a professional resume for {name} applying for the role of {job_title}.")
    return response.text