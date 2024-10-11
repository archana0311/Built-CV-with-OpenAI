import os
import openai
import pdfplumber
from docx import Document
import gradio as gr

# Set up your OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Function to read CV file (PDF or DOCX)
def read_cv_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    cv_content = ""

    if ext == '.pdf':
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                cv_content += page.extract_text()
    elif ext == '.docx':
        doc = Document(file_path)
        for para in doc.paragraphs:
            cv_content += para.text + "\n"
    else:
        raise ValueError("Unsupported file format. Please use .pdf or .docx.")

    return cv_content.strip()

# Function to process the resume and job description using OpenAI API
def process_resume(md_resume, job_description):
    prompt = f"""
    I have a resume formatted in Markdown and a job description. \
    Please adapt my resume to better align with the job requirements while \
    maintaining a professional tone. Tailor my skills, experiences, and \
    achievements to highlight the most relevant points for the position. \
    Ensure that my resume still reflects my unique qualifications and strengths \
    but emphasizes the skills and experiences that match the job description.

    ### Here is my resume in Markdown:
    {md_resume}

    ### Here is the job description:
    {job_description}

    Please modify the resume to:
    - Use keywords and phrases from the job description.
    - Adjust the bullet points under each role to emphasize relevant skills and achievements.
    - Make sure my experiences are presented in a way that matches the required qualifications.
    - Maintain clarity, conciseness, and professionalism throughout.

    Return the updated resume in Markdown format.
    """
    
    # Make API call to OpenAI GPT model
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert CV enhancer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.25
    )
    
    # Extract the modified resume from response
    updated_resume = response['choices'][0]['message']['content']
    
    return updated_resume

# Gradio interface for file upload and processing
def process_cv_and_jd(cv_file, jd_text):
    # Read the CV file and extract the content
    cv_content = read_cv_file(cv_file.name)
    
    # Convert JD text (provided as plain text by the user)
    job_description = jd_text.strip()

    # Process the resume and job description
    enhanced_resume = process_resume(cv_content, job_description)
    
    # Return the enhanced CV
    return enhanced_resume

# Save the enhanced CV to a file
def save_to_file(enhanced_resume):
    output_file_path = "Enhanced_CV.md"
    with open(output_file_path, "w") as f:
        f.write(enhanced_resume)
    return output_file_path

# Gradio UI
def build_ui():
    with gr.Blocks() as demo:
        gr.Markdown("<h1>CV Enhancer Based on Job Description</h1>")
        gr.Markdown("<p>Upload your CV (PDF or DOCX) and provide the Job Description (JD) to get an enhanced ATS-compliant CV.</p>")
        
        with gr.Row():
            cv_file = gr.File(label="Upload CV (PDF or DOCX)")
            jd_text = gr.Textbox(label="Paste Job Description", lines=10, placeholder="Enter job description here...")
        
        result_box = gr.Textbox(label="Enhanced CV", lines=20)
        save_btn = gr.Button("Save Enhanced CV")
        
        # Button to process and display enhanced CV
        process_btn = gr.Button("Enhance CV")
        process_btn.click(process_cv_and_jd, inputs=[cv_file, jd_text], outputs=[result_box])
        
        # Button to save enhanced CV to a file
        save_btn.click(save_to_file, inputs=[result_box], outputs=[gr.File()])
    
    demo.launch()

if __name__ == "__main__":
    build_ui()
