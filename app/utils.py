import fitz  # PyMuPDF
import io

def extract_text_from_pdf(uploaded_file):
    if uploaded_file.name.endswith(".txt"):
        return uploaded_file.read().decode("utf-8")
    
    if uploaded_file.name.endswith(".pdf"):
        pdf_text = ""
        with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
            for page in doc:
                pdf_text += page.get_text()
        return pdf_text
    
from transformers import pipeline

# Load once globally to avoid reloading every time
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(document_text):
    # Limit text to fit model constraints (max 1024 tokens ≈ ~3000-4000 characters)
    trimmed_text = document_text[:3000]

    summary_chunks = summarizer(trimmed_text, max_length=150, min_length=50, do_sample=False)

    return summary_chunks[0]['summary_text']

from transformers import pipeline

# Load Q&A model
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

def answer_question(question, context):
    result = qa_pipeline({
        'question': question,
        'context': context[:3000]  # Limit to avoid token overflow
    })

    answer = result['answer']
    score = result['score']

    # Justify based on sentence containing the answer
    justification = ""
    for sentence in context.split('.'):
        if answer in sentence:
            justification = sentence.strip() + "."
            break

    return answer, f"Justified from: \"{justification}\""

import uuid

def generate_challenge(document_text):
    # Simple logic: extract 3 important-looking sentences and turn them into questions
    sentences = document_text.split('.')[:10]  # Take first 10 sentences for now
    questions = []

    for i in range(min(3, len(sentences))):
        sentence = sentences[i].strip()
        if not sentence:
            continue

        question_text = f"What does this mean: \"{sentence}\"?"

        # Create a dummy evaluation function
        def make_eval(reference_sentence):
            def evaluate(user_answer):
                if any(word.lower() in reference_sentence.lower() for word in user_answer.lower().split()):
                    feedback = "✅ Good! Your answer includes key elements."
                else:
                    feedback = "❌ Hmm, try to relate your answer more closely to the original document."
                return {
                    "feedback": feedback,
                    "source": reference_sentence
                }
            return evaluate

        questions.append({
            "id": str(uuid.uuid4()),  # unique input key for Streamlit
            "question": question_text,
            "evaluate": make_eval(sentence)
        })

    return questions

