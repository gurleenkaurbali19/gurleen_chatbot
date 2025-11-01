import streamlit as st
from chatbot import get_answer

# Suggested questions
suggested_questions = [
    "Who are you?",
    "Tell me about your Article Summarization project.",
    "What skills do you have?",
    "What certifications do you hold?",
    "Where did you study?",
    "Where can I view your portfolio?",
    "What experience do you have?"
]

# Page config
st.set_page_config(page_title="Gurleen's Chatbot", page_icon="💬")

# Modern UI Styling
st.markdown("""
    <style>
        body {
            background-color: #f0f4f8;
            font-family: 'Segoe UI', sans-serif;
        }
        .main {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 12px;
        }

        /* Chat bubbles */
        .stChatMessage.user {
            background-color: #d9fdd3; /* soft green */
            color: #111;
            border: 1px solid #b3e6a1;
            border-radius: 12px;
            padding: 12px 14px;
            margin: 6px 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }
        .stChatMessage.assistant {
            background-color: #f2f2f2; /* soft gray */
            color: #000;
            border: 1px solid #ddd;
            border-radius: 12px;
            padding: 12px 14px;
            margin: 6px 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }

        /* Input styling */
        .stTextInput>div>div>input {
            border-radius: 12px;
            padding: 10px;
            border: 1px solid #00796b;
        }

        /* Button styling */
        .stButton>button {
            background: linear-gradient(90deg, #00796b, #009688);
            color: white;
            border-radius: 20px;
            font-weight: 600;
            font-size: 0.9rem;
            padding: 8px 18px;
            margin: 5px 5px 10px 0;
            transition: 0.3s ease;
            border: none;
        }
        .stButton>button:hover {
            background: linear-gradient(90deg, #004d40, #00695c);
        }

        /* Intro */
        .intro {
            text-align: center;
            font-size: 1.1em;
            color: #444;
            margin-bottom: 25px;
        }

        /* Chat container */
        .chat-container {
            max-height: 500px;
            overflow-y: auto;
            padding-right: 10px;
            margin-bottom: 20px;
        }

        /* Typing animation */
        .typing-indicator {
            font-style: italic;
            color: #888;
            animation: blink 1.5s steps(1) infinite;
        }
        @keyframes blink {
            0%, 100% { opacity: 0 }
            50% { opacity: 1 }
        }
    </style>
""", unsafe_allow_html=True)

# Title and intro
st.title("💬 Gurleen's Personal Chatbot")
st.markdown(
    '<div class="intro">👋 Ask me anything about <strong>Gurleen</strong> — her projects, education, skills, certifications and more.</div>',
    unsafe_allow_html=True
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant",
        "content": "Hi! I'm Gurleen's assistant. You can ask me anything about her projects, skills, education, or trainings! 😊"
    }]

# Suggested Questions
st.markdown("#### 💡 Quick Questions")
cols = st.columns(2)
for i, question in enumerate(suggested_questions):
    if cols[i % 2].button(question, key=f"suggested_{i}"):
        st.session_state.messages.append({"role": "user", "content": question})
        response = get_answer(question)
        st.session_state.messages.append({"role": "assistant", "content": "🤖 " + response})
        st.rerun()

# Chat History Section
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for msg in st.session_state.messages:
    avatar = "🧑‍💻" if msg["role"] == "user" else "🤖"
    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])
st.markdown('</div>', unsafe_allow_html=True)

# Chat Input
prompt = st.chat_input("Type your question about Gurleen here...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Typing..."):
            response = get_answer(prompt)
        st.session_state.messages.append({"role": "assistant", "content":response})
    st.rerun()
