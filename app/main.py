import streamlit as st
from utils import extract_text_from_pdf, summarize_text, answer_question, generate_challenge


# Set page title and layout
st.set_page_config(page_title="Smart Research Assistant", layout="wide")
st.title("📚 Smart Assistant for Research Summarization")

# File uploader
uploaded_file = st.file_uploader("Upload a PDF or TXT document", type=["pdf", "txt"])

# If file is uploaded
if uploaded_file:
    # Extract the document text
    document_text = extract_text_from_pdf(uploaded_file)

    # Show summary
    st.subheader("🔍 Document Summary (150 words max)")
    try:
        summary = summarize_text(document_text)
        st.write(summary)
    except:
        st.warning("Summary function not yet implemented.")

    # Mode selector
    mode = st.radio("Choose Interaction Mode", ["Ask Anything", "Challenge Me"])

    if mode == "Ask Anything":
        user_q = st.text_input("Ask a question about the document")
        if user_q:
            try:
                answer, source = answer_question(user_q, document_text)
                st.success(answer)
                st.caption(f"📌 Justified from: {source}")
            except:
                st.warning("Answering function not yet implemented.")

    elif mode == "Challenge Me":
        if st.button("Generate Questions"):
            try:
                questions = generate_challenge(document_text)
                for q in questions:
                    st.markdown(f"**Q: {q['question']}**")
                    user_answer = st.text_input("Your Answer:", key=q['id'])
                    if user_answer:
                        eval_result = q['evaluate'](user_answer)
                        st.write(f"✅ Feedback: {eval_result['feedback']}")
                        st.caption(f"📌 Justified from: {eval_result['source']}")
            except:
                st.warning("Challenge Me logic not yet implemented.")

