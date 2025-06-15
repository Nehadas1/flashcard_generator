# AI Flashcard Generator

A Streamlit-powered app that converts educational content into intelligent, structured flashcards using LLMs (Groq + LLaMA 3). Supports PDF, TXT, and direct text input — perfect for students, educators, and learners!

### Deployed URL: [Live on Stremlit cloud](https://flashcardgenerator-pkffzizv4czmrjyryhhnmn.streamlit.app/)

---

## Features

Upload content in `.txt`, `.pdf`, or paste directly  
Automatically generate **15 flashcards** using an LLM  
Includes:
    - Q&A format  
    - Difficulty level (Easy, Medium, Hard)  
    - Section/chapter heading  
    - Multi-language support (English, Hindi, German, etc.)  
 Editable flashcards before export  
 Export to `.csv` and `.txt` formats  
 Built with **Streamlit** and **Groq API (LLaMA 3)**

---

##  How to Run Locally

1. Clone the Repository

    git clone https://github.com/Nehadas1/flashcard_generator.git
    cd flashcard-generator

2. Install Dependencies

    Make sure Python 3.8+ is installed.

    pip install -r requirements.txt  

    Or install manually:

    pip install streamlit requests python-dotenv pymupdf

3. Set Up Environment Variables

    Create a .env file in the project root:

    GROQ_API_KEY=your_groq_api_key_here

4. Run the App

    streamlit run app.py

Folder Structure

    flashcard-generator/
    ├── app.py
    ├── flashcard_generator.py
    ├── utils.py
    ├── .env
    ├── requirements.txt
    └── README.md

 Sample Flashcard Output

    Section: Introduction to Machine Learning  
    Q: What is supervised learning?  
    A: Supervised learning is a type of machine learning where the model is trained on labeled data. The goal is to predict outcomes based on input features using known outputs.  
    Difficulty: Medium

 Export Formats

    CSV — Structured tabular format

    TXT — Markdown-style Q&A pairs

Powered By

    Groq API

    Streamlit

    PyMuPDF


 Author

    Made by Neha Das 


