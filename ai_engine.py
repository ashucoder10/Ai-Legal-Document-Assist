import os
import cohere
from dotenv import load_dotenv

load_dotenv()
print(os.getenv("CO_API_KEY"))
co = cohere.ClientV2(
    os.getenv("CO_API_KEY")
)
def ask_pdf(question, pdf_text):

    prompt = f"""
You are an AI Legal Document Assistant.

Document:
{pdf_text}

Question:
{question}

Answer ONLY from the document.

If the answer is not available in the document, reply:
This information is not available in the uploaded document.
"""

    try:

        response = co.chat(
            model="command-a-03-2025",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.message.content[0].text

    except Exception as e:
        return f"AI Error: {e}"