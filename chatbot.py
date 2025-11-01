import json
import faiss
import numpy as np
from dotenv import load_dotenv
import os
from langchain_cohere import ChatCohere
from sentence_transformers import SentenceTransformer

# Load environment variables
load_dotenv()
api_key = os.getenv("COHERE_API_KEY")

# Load your JSON data
with open('mydata.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Safely extract prompts and responses
questions = [item.get('prompt', '') for item in data]
answers = [item.get('response', '') for item in data]

# Load pre-trained embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Create FAISS index
embeddings = model.encode(questions)
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

# Initialize Cohere Chat model
cohere_client = ChatCohere(model="command-r-plus-08-2024", cohere_api_key=api_key)

def get_answer(query):
    query_embedding = model.encode([query])
    D, I = index.search(np.array(query_embedding), k=5)
    threshold = 1.0
    relevant_answers = [answers[i] for i, dist in zip(I[0], D[0]) if dist < threshold]

    # Smart + concise fallback
    if not relevant_answers:
        fallback_prompt = (
            f"You are Gurleen's personal chatbot. The user asked: '{query}'. "
            f"There is no specific information about this topic in Gurleen's data. "
            f"Do NOT ask the user for input. Instead, reply naturally in one or two short sentences — "
            f"politely mentioning that the detail isn't available and, if appropriate, redirect to Gurleen's professional background, "
            f"skills, or projects in a friendly, conversational way. "
            f"Never invent placeholders or imaginary details."
        )
        response = cohere_client.invoke(fallback_prompt)
        return response.content.strip() if hasattr(response, "content") else str(response).strip()

    # Normal context-based flow
    prompt = (
        f"You are Gurleen's personal chatbot. You answer questions about Gurleen, "
        f"a fresher who graduated with BCA in 2025. The user asked: '{query}'. "
        f"Here are the relevant answer chunks from Gurleen's data:\n"
        + "\n---\n".join(relevant_answers) +
        "\n\nPlease provide a clear, friendly, and relevant answer based only on these chunks."
    )

    response = cohere_client.invoke(prompt)
    return response.content.strip() if hasattr(response, "content") else str(response).strip()
