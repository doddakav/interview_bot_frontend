import streamlit as st
import requests

API_URL = st.secrets["api_url"]

st.title("🤖 AI Interview Bot")

with st.form("Chatbot"):

    topic = st.text_input(
        "Enter Topic"
    )

    level = st.selectbox(
        "Difficulty Level",
        ["Easy", "Medium", "Advanced"]
    )

    ways = st.multiselect(
        "Question Type",
        ["MCQ", "Theory", "Coding"]
    )

    submit = st.form_submit_button(
        "Generate Questions"
    )

if submit:

    response = requests.post(
        f"{API_URL}/generate-question",
        json={
            "topic": topic,
            "level": level,
            "ways": ways
        }
    )

    if response.status_code == 200:

        questions = response.json()["questions"]

        st.subheader("Generated Questions")

        st.write(questions)

    else:

        st.error("Unable to connect to backend")