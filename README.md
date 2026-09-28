<div align="center">

# ⚖️ AI Legal Document Assistant

**An intelligent, AI-powered web app to analyze, summarize, and chat with your PDF documents.**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Cohere](https://img.shields.io/badge/Cohere_AI-command--a-orange?style=for-the-badge)](https://cohere.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

</div>

---

## 📖 Overview

**AI Legal Document Assistant** is a Flask-based web application that lets you upload any PDF document and instantly interact with it using the power of **Cohere AI**. Whether it's a legal contract, a resume, a bill, or any other document — just upload it and start asking questions.

> Built with simplicity and practicality in mind. No cloud storage, no complex setup — just upload and ask.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📄 **PDF Chat** | Ask any question about your uploaded document and get accurate, context-aware answers |
| 📋 **Resume Analyzer** | Automatically extract name, skills, education, experience, and more from any resume |
| 🧾 **Bill / Receipt Reader** | Parse invoices and receipts to extract shop name, GST, total amount, and payment details |
| 📑 **Document Summary** | Get a structured summary with key points, dates, names, and conclusions |
| ↔️ **Adjust Document Size** | Rewrite the document in a short (~100 words), medium (~250 words), or detailed version |

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **AI Engine:** [Cohere AI](https://cohere.com) (`command-a-03-2025` model)
- **PDF Parsing:** PyPDF
- **Frontend:** Vanilla HTML, CSS, JavaScript
- **Environment:** `python-dotenv`

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- A free [Cohere API key](https://dashboard.cohere.com/)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ashucoder10/Ai-Legal-Document-Assist.git
   cd Ai-Legal-Document-Assist
   ```

2. **Install dependencies**
   ```bash
   pip install flask pypdf cohere python-dotenv
   ```

3. **Set up your API key**

   Create a `.env` file in the project root:
   ```env
   CO_API_KEY="your_cohere_api_key_here"
   ```

4. **Run the app**
   ```bash
   python app.py
   ```

5. **Open your browser** and go to `http://127.0.0.1:5000`

---

## 📁 Project Structure

```
Ai-Legal-Document-Assist/
│
├── app.py                 # Flask app & API routes
├── ai_engine.py           # Cohere AI integration
├── .env                   # API keys (not committed)
├── .gitignore
│
├── templates/
│   └── index.html         # Main UI template
│
├── static/
│   ├── index.css          # Styling
│   └── script.js          # Frontend logic
│
└── uploads/               # Temporary PDF storage (auto-created)
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Renders the main web UI |
| `POST` | `/upload` | Uploads and parses a PDF file |
| `POST` | `/chat` | Chat with the uploaded PDF |
| `POST` | `/resume` | Analyze a resume PDF |
| `POST` | `/receipt` | Extract data from a bill/receipt |
| `POST` | `/summary` | Summarize the uploaded document |
| `POST` | `/adjust-size` | Rewrite document in small/medium/large format |

---

## 💡 How It Works

```
User Uploads PDF
      │
      ▼
Text is Extracted (PyPDF)
      │
      ▼
Text is Split into Overlapping Chunks (1000 chars, 200 overlap)
      │
      ▼
User Asks a Question
      │
      ▼
Relevant Chunks are Found (keyword scoring)
      │
      ▼
Cohere AI generates an Answer from those Chunks
      │
      ▼
Answer is displayed in the Chat UI
```

---

## 🖼️ UI Preview

The app features a clean, sidebar-based chat interface inspired by modern AI assistants:

- **Left Sidebar** — Document upload + navigation buttons
- **Main Area** — Welcome screen with quick-action cards, live chat window
- **Input Bar** — Type your question and hit Enter or click Send

---

## ⚠️ Important Notes

- The `.env` file contains your API key — **never commit it** to version control.
- The `uploads/` folder stores PDFs temporarily during the session and is excluded from Git.
- The AI answers **strictly from the uploaded document** — it won't hallucinate information.

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Open an issue for bugs or feature requests
- Fork the repo and submit a pull request

---

## 👤 Author

**Ashu Mahour**
- GitHub: [@ashucoder10](https://github.com/ashucoder10)

---

<div align="center">

Made with ❤️ and ⚖️ | Powered by [Cohere AI](https://cohere.com)

</div>
