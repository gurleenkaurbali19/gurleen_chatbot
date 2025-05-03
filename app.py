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

# Modern CSS styling
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
        .stChatMessage {
            padding: 14px;
            border-radius: 12px;
            margin-bottom: 12px;
            box-shadow: 0 3px 6px rgba(0,0,0,0.1);
        }
        .stChatMessage.user {
            background-color: #e1f5fe;
        }
        .stChatMessage.assistant {
            background-color: #f0f0f0;
        }
        .stTextInput>div>div>input {
            border-radius: 12px;
            padding: 10px;
            border: 1px solid #00796b;
        }
        .stButton>button {
            background-color: #00796b;
            color: white;
            border-radius: 8px;
            font-weight: 600;
            padding: 8px 16px;
            margin: 5px 5px 10px 0;
            transition: 0.3s ease;
            border: none;
        }
        .stButton>button:hover {
            background-color: #004d40;
        }
        .intro {
            text-align: center;
            font-size: 1.1em;
            color: #444;
            margin-bottom: 20px;
        }
        .chat-container {
            max-height: 500px;
            overflow-y: auto;
            padding-right: 10px;
            margin-bottom: 20px;
        }
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
st.markdown('<div class="intro">👋 Ask me anything about <strong>Gurleen</strong> — her projects, education, skills, certifications and more.</div>', unsafe_allow_html=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant",
        "content": "Hi! I'm Gurleen's assistant. You can ask me anything about her projects, skills, education, or trainings! 😊"
    }]

# Suggested Questions Section
st.markdown("#### 💡 Quick Questions")
cols = st.columns(2)
for i, question in enumerate(suggested_questions):
    if cols[i % 2].button(question, key=f"suggested_{i}"):

        # Append user query and display immediately
        st.session_state.messages.append({"role": "user", "content": question})
        st.session_state.messages.append({"role": "assistant", "content": "🤖 " + get_answer(question)})
        st.rerun()


# Scrollable chat history
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
st.markdown('</div>', unsafe_allow_html=True)

# Chat input
prompt = st.chat_input("Type your question about Gurleen here...")

if prompt:
    # Add the user message immediately to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate and display the assistant's response
    with st.chat_message("assistant"):
        with st.spinner("Typing..."):
            response = get_answer(prompt)
        response = "🤖 " + response
        st.session_state.messages.append({"role": "assistant", "content": response})

    st.rerun()
