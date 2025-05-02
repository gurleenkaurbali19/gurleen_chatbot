import streamlit as st
from chatbot import get_answer

# Page config
st.set_page_config(page_title="Gurleen's Chatbot", page_icon="💬")

# Custom CSS for better styling
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
    </style>
""", unsafe_allow_html=True)

# Title and intro
st.title("💬 Gurleen's Personal Chatbot")
st.markdown("👋 Welcome! I'm a personal chatbot trained to answer questions about **Gurleen** — her skills, projects, education, and more.")
st.divider()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant",
        "content": "Hi! I'm Gurleen's assistant. You can ask me anything about her projects, skills, education, or trainings! 😊"
    }]

# Display all past messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
prompt = st.chat_input("Type your question about Gurleen here...")

if prompt:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get chatbot response
    response = get_answer(prompt)
    response = "🤖 " + response

    # Add bot response to history
    st.session_state.messages.append({"role": "assistant", "content": response})

    # Display bot response
    with st.chat_message("assistant"):
        st.markdown(response)
