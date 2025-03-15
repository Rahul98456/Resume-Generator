def clean_resume_text(text):
    """
    Replaces placeholders in the resume text with user-friendly prompts.
    """
    cleaned_text = text.replace("[Your Email Address]", "example@example.com")
    cleaned_text = cleaned_text.replace("[Your Phone Number]", "+1234567890")
    cleaned_text = cleaned_text.replace("[Your LinkedIn URL (optional)]", "https://linkedin.com/in/yourprofile")
    cleaned_text = cleaned_text.replace("[Your University Name]", "Your University")
    cleaned_text = cleaned_text.replace("[Your Graduation Year]", "2023")
    return cleaned_text