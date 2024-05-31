from flask import Flask, request, jsonify, render_template
import re
import requests
import spacy
import fitz  # PyMuPDF

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")
SKILLS = ['Python', 'Java', 'C++', 'JavaScript', 'SQL', 'HTML', 'CSS', 'Machine Learning', 'JavaScript', 'NodeJS', 'ReactJS' , 'ExpressJS', 'Data Analysis', 'Project Management', 'Communication', 'Teamwork', 'Problem Solving', 'Data Science', 'Time Management', 'Leadership', 'Git', 'Docker', 'Kubernetes', 'AWS', 'Azure']

def extract_skills(text):
    doc = nlp(text)
    found_skills = []
    for skill in SKILLS:
        if skill.lower() in text.lower():
            found_skills.append(skill)
    return found_skills

def extract_text_from_pdf(file):
    pdf_document = fitz.open(stream=file, filetype="pdf")
    text = ""
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    return text

@app.route('/')
def index():
    return render_template('upload.html', skills=None)

@app.route('/extract_skills', methods=['POST'])
def extract_skills_route():
    if 'resume' in request.files:
        file = request.files['resume']
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400
        
        if file.filename.lower().endswith('.pdf'):
            text = extract_text_from_pdf(file.read())
        else:
            text = file.read().decode('utf-8')
        
        skills = extract_skills(text)
        return render_template('upload.html', skills=skills)

    else:
        return jsonify({"error": "No file or URL part"}), 400

if __name__ == '__main__':
    app.run(debug=True)
