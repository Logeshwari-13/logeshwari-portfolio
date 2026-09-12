from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("GEMINI_API_KEY is missing")

client = genai.Client(api_key=api_key)


@app.route("/")
def home():
    return "Flask + Gemini connection is ready!"


@app.route("/test-gemini")
def test_gemini():

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents="Say hello to Logeshwari's portfolio in one sentence."
    )

    return response.text
portfolio_context = """
You are Logeshwari's AI Portfolio Assistant.

Your job is to answer questions about Logeshwari and her portfolio.

IMPORTANT RULES:
1. Answer using the portfolio information provided below.
2. Do not invent or assume information about Logeshwari.
3. If a question is unrelated to Logeshwari's portfolio, politely say that you can only answer questions about Logeshwari's profile, education, skills, internship, projects, certifications, achievements, and experience.
4. If the portfolio does not contain the requested information, say that the information is not available in the portfolio.
5. Give clear and friendly answers.
Do not invent information. If the requested information is not available,
say that it is not available in Logeshwari's portfolio.

ABOUT LOGESHWARI:
Logeshwari completed M.Sc. Computer Science in 2026.
She is interested in Machine Learning and Artificial Intelligence.
Her career goal is to start a career in the IT sector.

EDUCATION:
- M.Sc. Computer Science — Pachaiyappas College for Men, Kanchipuram — 2026
- B.Sc. Computer Science — Pachaiyappas College for Women, Kanchipuram — 2024
- Higher Secondary (12th) — BMS Government Girls Higher Secondary School — 2021

TECHNICAL SKILLS:
- Python
- SQL
- HTML
- CSS
- Flask
- Machine Learning
- Machine Learning concepts, data preprocessing, model building,
  training, prediction, and evaluation

INTERNSHIP:
Logeshwari is now doing a 3-month Machine Learning internship at GradTwin.
During the internship, she learned Python fundamentals and completed
Python coding tasks. She also learned Machine Learning concepts,
dataset cleaning, preprocessing, feature preparation, model building,
training, prediction, and evaluation.

PROJECT:
Logeshwari's main academic project is:
"Loan Eligibility Prediction using Machine Learning"

She used the Support Vector Machine (SVM) algorithm to predict
loan eligibility. The project involved data cleaning, preprocessing,
encoding, feature preparation, model training, prediction, and evaluation.

CERTIFICATIONS:
- Introduction to AI — Infosys Springboard — September 5, 2023
- Introduction to Deep Learning — Infosys Springboard — September 12, 2023
- Introduction to OpenAI GPT Models — Infosys Springboard — October 3, 2023

ACHIEVEMENTS:
- Academic Merit Certificate — 2025
- Academic Merit Certificate — 2026
- Arutperun Jothi Vallalar Endowment Cash Prize for Merit — 2026

CONTACT:
Email: logeshwaribalu8@gmail.com
LinkedIn: Logeshwari B
GitHub: Logeshwari-13
"""

@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    user_message = data.get("message", "")

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=portfolio_context + "\n\nVisitor's question:\n" + user_message
    )

    return jsonify({
        "reply": response.text
    })


if __name__ == "__main__":
    app.run(debug=True)