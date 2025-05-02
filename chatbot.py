import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Loading your data
with open('mydata.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Extracting prompts and responses
questions = [item['prompt'] for item in data]
answers = [item['response'] for item in data]

# Loading pre-trained model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Encoding the questions
embeddings = model.encode(questions)

# Creating FAISS index
dimension = embeddings[0].shape[0]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

def get_answer(query):
    query_embedding = model.encode([query])
    D, I = index.search(np.array(query_embedding), k=1)
    if D[0][0] < 1.0:  # threshold for better matching
        return answers[I[0][0]]
    else:
        return "Sorry, I don’t have an answer to that right now!"
