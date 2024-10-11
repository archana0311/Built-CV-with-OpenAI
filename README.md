# Built-CV-with-OpenAI

**A Model for CV enhancement based on JD's**

1. Objective:
To create a new model that processes the user-submitted CV and JD, utilizing an internal mechanism to call a Large Language Model (LLM) for creating an enhanced, ATS-compliant CV tailored to the Job Description. The project is built using Python, OpenAI API and Gradio.

2. Features:
The model shall take the CV and Job Description (JD) as input. The model shall internally call the LLM to generate enhanced sections of the CV, based on the analysis of the JD, ensuring relevance to the job role. Accepts both PDF and DOCX CV files. Aligning experiences and skills with the JD. Highlighting key qualifications and responsibilities as per the JD. Removing or minimizing less relevant details from the original CV (with user consent). The output of the model will be an enhanced, ATS-compliant CV that emphasizes the user’s relevant skills and experience tailored to the JD.

3. Installations:
Prerequisites Python 3.12: Make sure Python is installed on your system. Pip: Ensure you have pip for installing dependencies.
Clone the Repository: Install Dependencies: pip install -r requirements.txt Set up API keys: OPENAI_API_KEY
Run the Application: python main.py

4. Usage
Upload and Generate Upload Your CV: After launching the application, you'll be prompted to upload your CV in either PDF or DOCX format. Analyze and Generate: The system will analyze the CV, extract relevant details, and generate a professional HTML/CSS/JS portfolio. Preview and Download: The generated portfolio can be previewed on the web page. You can also download the HTML file for deployment.

5. File Formats
This project supports the following CV file formats:
PDF: Extracts text from PDF using pdfplumber. DOCX: Parses Microsoft Word .docx files using python-docx.

6. Key Libraries Used:
pdfplumber: For extracting text from PDF files.
python-docx: For reading and parsing DOCX files. 
Gradio: Provides a web interface for file upload, preview, and download.
OpenAI: Integrates with the OpenAI API to interact with the GPT model, enabling natural language processing and generating enhanced, tailored CVs based on the provided job descriptions.

7. Web Interface:
A Gradio-based interface is used for easy file upload and portfolio generation.

8. Contributing
We welcome contributions! To contribute: 1.Fork the repository. 2.Create a new feature branch: git checkout -b feature/your-feature 3.Commit your changes: git commit -m 'Add new feature' 4.Push to the branch: git push origin feature/your-feature
Open a pull request and explain your changes.

9. License
This project is licensed under the MIT License. See the LICENSE file for more detai

![Open your wings!!]

(bird.jpg)
