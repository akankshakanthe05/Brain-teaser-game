import streamlit as st
import random

st.title("🧠 Brain Teaser Game")

# Questions
questions = [
    {"q": "What has keys but can't open locks?", "options": ["Piano", "Map", "Clock", "River"], "ans": "Piano"},
    {"q": "What has hands but cannot clap?", "options": ["Monkey", "Clock", "Robot", "Chair"], "ans": "Clock"},
    {"q": "What comes once in a minute, twice in a moment, but never in a thousand years?", "options": ["Time", "Wind", "Water", "Letter M"], "ans": "Letter M"},
    {"q": "What gets wetter the more it dries?", "options": ["Sponge", "Rain", "Towel", "Cloud"], "ans": "Towel"}
]

# Session state
if "index" not in st.session_state:
    st.session_state.index = 0
    st.session_state.score = 0
    random.shuffle(questions)

# Current question
q = questions[st.session_state.index]

st.subheader(q["q"])

choice = st.radio("Choose answer:", q["options"])

if st.button("Submit"):
    if choice == q["ans"]:
        st.success("Correct!")
        st.session_state.score += 1
    else:
        st.error(f"Wrong! Correct answer is {q['ans']}")

    st.session_state.index += 1

# End
if st.session_state.index >= len(questions):
    st.write("🎯 Game Over")
    st.write(f"Score: {st.session_state.score}/{len(questions)}")