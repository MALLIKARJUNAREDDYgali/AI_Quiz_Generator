import os
import json
import streamlit as st
import requests
from dotenv import load_dotenv

from backend.utils import generate_prompt

# Load .env
load_dotenv()
API_URL = os.getenv("EURI_API_URL")
API_KEY = os.getenv("EURI_API_KEY")
MODEL = os.getenv("EURI_MODEL")

st.set_page_config(page_title="AI Quiz Generator", page_icon="🧠")

st.title("🧠 AI Quiz Generator")
st.caption("Generate, take, and evaluate quizzes with AI.")

# Initialize session state
if "quiz_data" not in st.session_state:
    st.session_state.quiz_data = None
if "user_answers" not in st.session_state:
    st.session_state.user_answers = {}
if "score" not in st.session_state:
    st.session_state.score = None

# Step 1: Select topic and question type
with st.form("quiz_setup"):
    st.subheader("1️⃣ Choose your quiz topic and type")
    topic = st.text_input("Topic", placeholder="e.g. Java, Photosynthesis, World War II")
    question_type = st.selectbox("Question Type", ["MCQ", "Short Answer"])
    submitted = st.form_submit_button("Generate Quiz")

    if submitted:
        if not topic:
            st.error("Please enter a topic.")
        else:
            with st.spinner("Generating quiz questions..."):
                prompt = generate_prompt(topic, question_type)

                headers = {
                    "Authorization": f"Bearer {API_KEY}",
                    "Content-Type": "application/json"
                }

                payload = {
                    "model": MODEL,
                    "messages": [
                        {"role": "user", "content": prompt}
                    ]
                }

                try:
                    res = requests.post(API_URL, headers=headers, json=payload)
                    res.raise_for_status()
                    data = res.json()
                    content = data['choices'][0]['message']['content']

                    # Parse JSON
                    quiz = json.loads(content)
                    st.session_state.quiz_data = quiz
                    st.session_state.user_answers = {}
                    st.session_state.score = None

                    st.success("Quiz generated! Scroll down to take it.")

                except Exception as e:
                    st.error(f"Error generating quiz: {e}")

# Step 2: Display quiz if loaded
if st.session_state.quiz_data:
    st.subheader("2️⃣ Take the Quiz")

    with st.form("quiz_form"):
        for idx, item in enumerate(st.session_state.quiz_data):
            q_key = f"q_{idx}"
            st.markdown(f"**{idx+1}. {item['question']}**")
            if "options" in item:
                st.session_state.user_answers[q_key] = st.radio(
                    f"Select answer:", 
                    options=item['options'],
                    key=q_key
                )
            else:
                st.session_state.user_answers[q_key] = st.text_input(
                    "Your answer:", 
                    key=q_key
                )

        submitted_answers = st.form_submit_button("Submit Answers")

    # Step 3: Evaluate
    if submitted_answers:
        score = 0
        results = []
        for idx, item in enumerate(st.session_state.quiz_data):
            q_key = f"q_{idx}"
            correct = item['answer'].strip().lower()
            user_ans = st.session_state.user_answers.get(q_key, "").strip().lower()

            is_correct = user_ans == correct
            if is_correct:
                score += 1

            results.append({
                "question": item['question'],
                "your_answer": user_ans,
                "correct_answer": correct,
                "explanation": item.get("explanation", ""),
                "is_correct": is_correct
            })

        st.session_state.score = score

        st.subheader("3️⃣ Results")
        st.markdown(f"**Score: {score} / {len(st.session_state.quiz_data)}**")

        for r in results:
            if r["is_correct"]:
                st.success(f"✅ {r['question']}\n\nYour answer: {r['your_answer']}")
            else:
                st.error(f"❌ {r['question']}\n\nYour answer: {r['your_answer']}\n\nCorrect answer: {r['correct_answer']}\n\nExplanation: {r['explanation']}")

