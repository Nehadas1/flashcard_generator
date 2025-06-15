import streamlit as st
import pandas as pd
import re
from utils import extract_text_from_pdf, extract_text_from_txt
from flashcard_generator import generate_flashcards

st.set_page_config(page_title="StudyBuddy AI", page_icon="📚", layout="centered")

st.markdown("""
# 🎓 StudyBuddy AI Flashcard Generator
Easily convert learning content into flashcards powered by LLMs!

Upload text or documents, select your preferences, and let StudyBuddy do the magic!
""")

# Sidebar 
with st.sidebar:
    st.header("🔧 Configuration")
    input_type = st.radio("📤 Select Input Type", ["Text", "TXT", "PDF"])
    subject = st.text_input("📖 Subject", placeholder="e.g., Physics, Literature")
    export_format = st.selectbox("📂 Export Format", ["None", "TXT", "CSV"])
    language = st.selectbox("🌍 Output Language", ["English", "Hindi", "German", "Spanish", "French"])

# Input area 
st.markdown("## ✏️ Input Area")
text = ""
if input_type == "Text":
    text = st.text_area("Paste your learning material below:", height=250)
else:
    uploaded_file = st.file_uploader(f"Upload your {input_type} file", type=[input_type.lower()])
    if uploaded_file:
        if input_type == "PDF":
            text = extract_text_from_pdf(uploaded_file)
        elif input_type == "TXT":
            text = extract_text_from_txt(uploaded_file)

# Generate flashcards
if st.button("🪄 Create Flashcards"):
    if not text.strip():
        st.warning("⚠️ Please enter or upload some text to generate flashcards.")
    else:
        with st.spinner("✨ Generating intelligent flashcards..."):
            flashcards = generate_flashcards(text, subject, language)
            st.success("🎉 Flashcards created successfully!")

            st.markdown("## 📘 Your Flashcards")
            flashcard_list = []

            # Extract Q&A pairs and meta info
            flashcard_blocks = re.findall(
                r"Q:\s*(.*?)\nA:\s*(.*?)\nDifficulty:\s*(.*?)\nCategory:\s*(.*?)\nImportance:\s*(.*?)(?:\n|$)",
                flashcards,
                flags=re.DOTALL
            )

            for q, a, d, c, i in flashcard_blocks:
                flashcard_list.append({
                    "Question": q.strip(),
                    "Answer": a.strip(),
                    "Difficulty": d.strip(),
                    "Category": c.strip(),
                    "Importance": i.strip()
                })

                with st.expander(f"📌 {q.strip()}"):
                    st.markdown(f"""
                    **💡 Answer:** {a.strip()}  
                    **📊 Difficulty:** `{d.strip()}`  
                    **📂 Category:** `{c.strip()}`  
                    **🔥 Importance:** `{i.strip()}`
                    """)

            st.markdown(f"🔢 **Total Flashcards Generated:** `{len(flashcard_list)}`")

            # Export 
            if export_format != "None" and flashcard_list:
                df = pd.DataFrame(flashcard_list)

                if export_format == "CSV":
                    csv = df.to_csv(index=False).encode("utf-8")
                    st.download_button("⬇️ Download CSV", csv, "flashcards.csv", "text/csv")

                elif export_format == "TXT":
                    txt = "\n\n".join([
                        f"Q: {row['Question']}\nA: {row['Answer']}\nDifficulty: {row['Difficulty']}\nCategory: {row['Category']}\nImportance: {row['Importance']}"
                        for _, row in df.iterrows()
                    ])
                    st.download_button("⬇️ Download TXT", txt.encode("utf-8"), "flashcards.txt", "text/plain")

            # Raw Output
            with st.expander("📄 Show Full Raw Output"):
                st.code(flashcards, language='markdown')
