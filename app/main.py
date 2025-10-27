import streamlit as st
from utils import extract_text_from_pdf, summarize_text, answer_question, generate_challenge

# -------------------- PAGE SETUP --------------------
st.set_page_config(
    page_title="Smart Research Assistant",
    layout="wide",
    page_icon="📚",
)

# -------------------- SIDEBAR --------------------
with st.sidebar:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
        width=120,
    )
    st.markdown("## 👋 Welcome!")
    st.write(
        "This **Smart Research Assistant** helps you upload documents, summarize them, "
        "and interact using AI — either by **asking questions** or **taking a challenge**!"
    )
    st.markdown("---")
    st.caption("🚀 Built with Streamlit & Hugging Face Transformers")

# -------------------- MAIN CONTENT --------------------
st.markdown(
    """
    <h1 style='text-align:center; color:#3b82f6;'>
        📚 Smart Assistant for Research Summarization
    </h1>
    <p style='text-align:center; color:gray;'>
        Upload your research document and interact intelligently with its content.
    </p>
    """,
    unsafe_allow_html=True,
)

# File uploader section
uploaded_file = st.file_uploader(
    "📂 Upload a PDF or TXT Document", type=["pdf", "txt"], help="Supported formats: .pdf, .txt"
)

# -------------------- MAIN LOGIC --------------------
if uploaded_file:
    with st.spinner("📄 Extracting document text..."):
        document_text = extract_text_from_pdf(uploaded_file)

    # Summary Section
    st.markdown("### 🔍 Document Summary")
    with st.container():
        try:
            summary = summarize_text(document_text)
            st.success(summary)
        except Exception as e:
            st.warning("⚠️ Summary function not yet implemented or failed to load.")
            st.exception(e)

    st.markdown("---")
    st.markdown("### 💡 Choose Interaction Mode")

    mode = st.radio(
        "Select Mode:",
        ["Ask Anything", "Challenge Me"],
        horizontal=True,
        index=0,
    )

    # -------------------- ASK ANYTHING MODE --------------------
    if mode == "Ask Anything":
        st.markdown("#### 🤔 Ask questions about your document below:")
        user_q = st.text_input("💬 Your Question")
        if user_q:
            with st.spinner("🧠 Thinking..."):
                try:
                    answer, source = answer_question(user_q, document_text)
                    st.success(f"**Answer:** {answer}")
                    st.caption(f"📎 {source}")
                except Exception as e:
                    st.warning("⚠️ Answering function not yet implemented.")
                    st.exception(e)

    # -------------------- CHALLENGE MODE --------------------
    elif mode == "Challenge Me":
        st.markdown("#### 🎯 Let's see how well you understood!")
        if st.button("✨ Generate Questions"):
            with st.spinner("🔍 Creating your challenge..."):
                try:
                    questions = generate_challenge(document_text)
                    for q in questions:
                        st.markdown(f"**🧩 Q:** {q['question']}")
                        user_answer = st.text_input("✍️ Your Answer:", key=q["id"])
                        if user_answer:
                            eval_result = q["evaluate"](user_answer)
                            st.info(f"**Feedback:** {eval_result['feedback']}")
                            st.caption(f"📎 From document: {eval_result['source']}")
                            st.markdown("---")
                except Exception as e:
                    st.warning("⚠️ Challenge logic not yet implemented.")
                    st.exception(e)
else:
    st.markdown(
        """
        <div style='text-align:center; margin-top: 3em;'>
            <img src='https://cdn-icons-png.flaticon.com/512/2995/2995620.png' width='150'>
            <h3 style='color:gray;'>Please upload a document to begin.</h3>
        </div>
        """,
        unsafe_allow_html=True,
    )

# -------------------- FOOTER --------------------
st.markdown(
    """
    <hr>
    <div style='text-align:center; color:gray; font-size:0.9em;'>
        © 2025 Smart Research Assistant | Designed with ❤️ by Manvi Taneja
    </div>
    """,
    unsafe_allow_html=True,
)
