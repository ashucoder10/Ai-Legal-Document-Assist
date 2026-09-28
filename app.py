from flask import Flask, render_template, request, jsonify
import os
from pypdf import PdfReader
from ai_engine import ask_pdf

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Global Variables
pdf_text = ""
pdf_chunks = []


# Split PDF into Chunks
def split_text(text, chunk_size=1000, overlap=200):
    chunks = []

    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap

    return chunks


# Home
@app.route("/")
def home():
    return render_template("index.html")


# Upload PDF
@app.route("/upload", methods=["POST"])
def upload_file():

    global pdf_text
    global pdf_chunks

    if "file" not in request.files:
        return jsonify({"error": "No file uploaded."})

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "Please select a PDF."})

    if not file.filename.lower().endswith(".pdf"):
        return jsonify({"error": "Only PDF files are allowed."})

    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(file_path)

    pdf_text = ""

    reader = PdfReader(file_path)

    for page in reader.pages:
        text = page.extract_text()
        if text:
            pdf_text += text + "\n"

    pdf_chunks = split_text(pdf_text)

    print("=" * 60)
    print("PDF Uploaded Successfully")
    print("PDF Length:", len(pdf_text))
    print("Total Chunks:", len(pdf_chunks))
    print("=" * 60)

    return jsonify({
        "message": "PDF Uploaded Successfully",
        "text": pdf_text
    })


# Chat with PDF
@app.route("/chat", methods=["POST"])
def chat():

    global pdf_chunks

    if len(pdf_chunks) == 0:
        return jsonify({
            "reply": "Please upload a PDF first."
        })

    data = request.get_json()

    question = data.get("message", "").strip()

    if question == "":
        return jsonify({
            "reply": "Please enter a question."
        })

    relevant_chunks = []

    for chunk in pdf_chunks:

        score = 0

        for word in question.lower().split():

            if word in chunk.lower():
                score += 1

        if score > 0:
            relevant_chunks.append(chunk)

    if len(relevant_chunks) == 0:
        relevant_text = pdf_chunks[0]
    else:
        relevant_text = "\n\n".join(relevant_chunks[:3])

    try:
        answer = ask_pdf(question, relevant_text)
    except Exception as e:
        answer = f"AI Error: {e}"

    return jsonify({
        "reply": answer
    })


# Resume Reader
@app.route("/resume", methods=["POST"])
def resume():

    global pdf_chunks

    if len(pdf_chunks) == 0:
        return jsonify({
            "reply": "Please upload a resume first."
        })

    text = "\n".join(pdf_chunks)

    question = """
Analyze this resume and extract:

1. Full Name
2. Email
3. Phone Number
4. Skills
5. Education
6. Experience
7. Projects
8. Certifications
9. Strengths

If any field is missing, write 'Not Found'.
"""

    answer = ask_pdf(question, text)

    return jsonify({
        "reply": answer
    })


# Bill / Receipt Reader
@app.route("/receipt", methods=["POST"])
def receipt():

    global pdf_chunks

    if len(pdf_chunks) == 0:
        return jsonify({
            "reply": "Please upload a receipt first."
        })

    text = "\n".join(pdf_chunks)

    question = """
Analyze this bill or receipt and extract:

1. Shop Name
2. Date
3. Invoice Number
4. GST Number
5. Total Amount
6. Tax Amount
7. Payment Method

If any field is missing, write 'Not Found'.
"""

    answer = ask_pdf(question, text)

    return jsonify({
        "reply": answer
    })


# Document Summary
@app.route("/summary", methods=["POST"])
def summary():

    global pdf_chunks

    if len(pdf_chunks) == 0:
        return jsonify({
            "reply": "Please upload a document first."
        })

    text = "\n".join(pdf_chunks)

    question = """
Read the uploaded document and provide:

1. Short Summary
2. Key Points
3. Important Dates
4. Important Names
5. Important Numbers
6. Overall Conclusion
"""

    answer = ask_pdf(question, text)

    return jsonify({
        "reply": answer
    })


# Adjust Document Size
@app.route("/adjust-size", methods=["POST"])
def adjust_size():

    global pdf_chunks

    if len(pdf_chunks) == 0:
        return jsonify({
            "reply": "Please upload a document first."
        })

    data = request.get_json()

    size = data.get("size", "medium").lower()

    text = "\n".join(pdf_chunks)

    if size == "small":
        question = "Rewrite this document in about 100 words."

    elif size == "large":
        question = "Rewrite this document in detail while preserving all important information."

    else:
        question = "Rewrite this document in about 250 words."

    answer = ask_pdf(question, text)

    return jsonify({
        "reply": answer
    })


if __name__ == "__main__":
    app.run(debug=True)