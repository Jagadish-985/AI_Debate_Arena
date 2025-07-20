import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
import json

load_dotenv()
GENAI_API_KEY = os.getenv("GENAI_API_KEY")
genai.configure(api_key=GENAI_API_KEY)

st.set_page_config(
    page_title="AI Debate Arena",
    page_icon="",
    layout="wide"
)

DEBATE_PROMPT_TEMPLATE = """
You are 'The Contender', a master debater. Your tone is sharp, confident, and challenging.
- Forcefully argue the opposite position of the user.
- Debate topic: "{topic}"
- User's stance: {user_side}
- Your stance: Opposite of user.
- Never agree with the user. Identify logical fallacies in their arguments.
- Respond in under 80 words.
"""

ANALYZER_PROMPT = """
You are a world-class debate coach. Analyze the user's last statement.
Give analysis STRICTLY as JSON with keys: "rating", "strength", "suggestion".
Example: {"rating": 7, "strength": "The use of a real-world example was effective.", "suggestion": "Try to support your claim with a statistic."}
"""

analyzer_model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=ANALYZER_PROMPT
)

if "topic" not in st.session_state:
    st.session_state.topic = None
if "stance" not in st.session_state:
    st.session_state.stance = None
if "messages" not in st.session_state:
    st.session_state.messages = []
if "analysis" not in st.session_state:
    st.session_state.analysis = None

st.title("AI Debate Arena")
st.caption("Face off with 'The Contender' and receive live feedback. Let's begin!")

if not st.session_state.topic or not st.session_state.stance:
    with st.form("setup_form"):
        st.subheader("Setup Debate")
        topic = st.text_input("Enter your debate topic", placeholder="e.g., Should AI replace human jobs?")
        stance = st.selectbox("Choose your stance", ["Select", "For", "Against"])
        submitted = st.form_submit_button("Start Debate")

        if submitted:
            if not topic.strip() or stance == "Select":
                st.warning("Please enter a valid topic and choose a stance to continue.")
            else:
                st.session_state.topic = topic.strip()
                st.session_state.stance = stance
                st.rerun()
    st.stop()

debate_prompt = DEBATE_PROMPT_TEMPLATE.format(
    topic=st.session_state.topic,
    user_side=st.session_state.stance
)

debate_model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=debate_prompt
)

st.success(f"Debate Topic: **{st.session_state.topic}**")
st.info(f"Your Position: **{st.session_state.stance}** — The Contender will argue the opposite.")

col1, col2 = st.columns([2, 1], gap="medium")

with col1:
    st.subheader("Debate Arena")

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if user_input := st.chat_input("State your argument..."):
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        try:
            ai_response = debate_model.generate_content(user_input).text.strip()
            with st.chat_message("assistant"):
                st.markdown(ai_response)
            st.session_state.messages.append({"role": "assistant", "content": ai_response})

            analysis = analyzer_model.generate_content(user_input).text.strip()
            analysis_json = json.loads(analysis.replace("```json", "").replace("```", ""))
            st.session_state.analysis = analysis_json

        except Exception as e:
            st.error(f"Error: {e}")

with col2:
    st.subheader("Live Feedback")
    if st.session_state.analysis:
        a = st.session_state.analysis
        st.metric("Persuasiveness", f"{a.get('rating', 'N/A')}/10")
        st.success(f"Strength: {a.get('strength', '...')}")
        st.info(f"Suggestion: {a.get('suggestion', '...')}")
    else:
        st.caption("Make your first argument to receive feedback.")

st.divider()
if st.button("Reset Topic & Stance"):
    for key in ["topic", "stance", "messages", "analysis"]:
        st.session_state.pop(key, None)
    st.rerun()

st.caption("Built with ❤️ from Team TriVikram - B.Jagadish , Sanjeev Janardhan, Puneeth R V")
