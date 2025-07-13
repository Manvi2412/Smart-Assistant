# Smart Assistant for Research Summarization

This project implements a GenAI-powered smart assistant that reads and understands user-uploaded documents (PDF or TXT), summarizes their contents, answers questions with context-based reasoning, and generates logic-based challenges—all with accurate justifications sourced from the original document.

This was built as part of a GenAI internship assignment focused on contextual comprehension, logical reasoning, and interactive AI tooling.

---

## Features

- Upload and parse structured English documents (PDF or TXT)
- Automatically generate a concise summary (≤ 150 words)
- Interactive Q&A mode: ask free-form questions and receive accurate, justified responses
- Challenge mode: system-generated logic-based questions + evaluation with feedback
- Context-grounded answers with reference to source snippets
- Clean, browser-based UI for seamless interaction
- Fully local setup using open-source models (no API keys required)

---

## Architecture Overview

- **Frontend**: Streamlit (runs locally in-browser)
- **Document Parsing**: PyMuPDF for PDF, native reading for TXT
- **Summarization Model**: `sshleifer/distilbart-cnn-12-6` (HuggingFace Transformers)
- **Question Answering Model**: `distilbert-base-cased-distilled-squad`
- **Challenge Evaluation**: Keyword matching + context analysis
- **Language**: Python 3.9+

---

## Folder Structure
smart-assistant/
├── app/
│ ├── main.py # Streamlit UI
│ └── utils.py # Core logic: parsing, summarization, Q&A, challenge
├── requirements.txt # Project dependencies
├── README.md # This file



---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/smart-assistant.git
cd smart-assistant
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the App
```bash
streamlit run app/main.py
```
### How It Works
1. Upload a Document

- Supported formats: .pdf, .txt
- Text is extracted using PyMuPDF or native decoding

2. Summary Generation

- A pre-trained BART model generates a ≤150-word summary
- Designed for research papers, reports, manuals, and structured content

3. Ask Anything Mode

- Users can enter any question about the document
- A Q&A model answers using the document as context
- Each answer is justified with a supporting source snippet

4. Challenge Me Mode
- The system generates 3 comprehension or logic-based questions
- Users respond; the assistant evaluates and gives feedback
- Each evaluation is tied back to content from the document

- Technologies Used
1. Python
2. Streamlit
3. Hugging Face Transformers
4. PyMuPDF (fitz)
5. uuid (for dynamic inputs)
6. Regex and keyword matching (custom evaluation logic)

- Deployment
  
1. This application runs locally and does not require GPU or API keys.
2. Future improvements may include deployment via Hugging Face Spaces, Docker, or Streamlit Cloud for hosted demos.

- Author
Manvi Taneja

B.Tech (Information Technology), graduating 2026
Passionate about GenAI, NLP, and building impactful AI tools
manvitaneja70952@gmail.com

License
This project is for educational and demonstration purposes only.









