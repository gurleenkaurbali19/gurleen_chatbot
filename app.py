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

# Custom CSS for styling
st.markdown("""
    <style>
        .main {
            background-color: #f9f9fc;
        }
        .stChatMessage {
            padding: 10px;
            border-radius: 12px;
            margin-bottom: 10px;
        }
        .stChatMessage.user {
            background-color: #e0f7fa;
        }
        .stChatMessage.assistant {
            background-color: #f1f0f0;
        }
        .stTextInput>div>div>input {
            border-radius: 10px;
            border: 1px solid #ccc;
        }
        .suggested-button {
            margin: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# Title and intro
st.title("💬 Gurleen's Personal Chatbot")
st.markdown("👋 Welcome! I'm a personal chatbot trained to answer questions about **Gurleen** — her skills, projects, education, and more.")
st.divider()

# Show suggested questions at top
st.markdown("#### 💡 Suggested Questions:")
cols = st.columns(2)
for i, question in enumerate(suggested_questions):
    if cols[i % 2].button(question, key=f"suggested_{i}"):
        st.session_state.messages.append({"role": "user", "content": question})
        response = get_answer(question)
        st.session_state.messages.append({"role": "assistant", "content": "🤖 " + response})

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant",
        "content": "Hi! I'm Gurleen's assistant. You can ask me anything about her projects, skills, education, or trainings! 😊"
    }]

# Display chat messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User text input
prompt = st.chat_input("Type your question about Gurleen here...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    response = get_answer(prompt)
    st.session_state.messages.append({"role": "assistant", "content": "🤖 " + response})

    with st.chat_message("assistant"):
        st.markdown("🤖 " + response)
