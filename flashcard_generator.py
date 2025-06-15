import os
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

def generate_flashcards(text, subject="General", language="English"):
    api_key = st.secrets["GROQ_API_KEY"]

    prompt = f"""
You are a helpful assistant. Generate exactly 10 to 15 flashcards from the text below.

Each flashcard must follow this format:
Q: <question>
A: <answer>
Difficulty: <Easy/Medium/Hard>
Category: <Definition/Concept/Application>
Importance: <High/Medium/Low>

Translate to: {language}
Subject: {subject}

Content:
{text}

Only return the flashcards. Do not include anything else.
"""

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama3-8b-8192",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 2048
    }

    response = requests.post(url, headers=headers, json=payload)
    result = response.json()

    if "choices" in result:
        return result["choices"][0]["message"]["content"].strip()
    else:
        return f" Groq API error: {result.get('error', 'Unknown response')}"