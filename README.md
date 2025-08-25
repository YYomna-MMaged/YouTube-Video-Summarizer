# 📺 YouTube Video Summarizer

A Streamlit web application that allows you to **summarize YouTube videos** easily.  
It extracts the transcript of a video, optionally translates it to English, and then generates a clean, concise summary using HuggingFace models.

---

## 🚀 Features
- Extracts video transcripts directly from YouTube.
- Detects the original language of the transcript.
- Translates transcripts to English if needed.
- Summarizes long transcripts into concise text.
- User-friendly **Streamlit web interface**.

---

## 📂 Project Structure
yt_summarizer/
│── utils/
│ ├── extractor.py # Extracts video ID and transcript
│ ├── chunker.py # Splits transcript into chunks
│ ├── translator.py # Detects and translates language
│ ├── summarizer.py # Summarizes chunks using HuggingFace
│ ├── cleaner.py # Cleans and formats final summary
│
│── all_summarizer.py # Main Streamlit application
│── requirements.txt # Project dependencies

---

## 🛠️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/YYomna-MMaged/YouTube-Video-Summarizer.git
   cd YouTube-Video-Summarizer/yt_summarizer

python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

pip install -r requirements.txt

## 🔑 HuggingFace Token Setup
This project uses HuggingFace models.  
You need an access token:

1. Create a token from [HuggingFace Tokens](https://huggingface.co/settings/tokens) with **Read access**.  
2. In **Streamlit Cloud**, go to **Settings → Secrets** and add:
   ```toml
   HF_TOKEN = "your_token_here"
3. The app will automatically load this token.

## 🌐 Deployment (Streamlit Cloud)
1. Push your code to GitHub.  
2. Go to [Streamlit Cloud](https://share.streamlit.io/).  
3. Deploy the repo and set:  
   - **Main file path:** `yt_summarizer/all_summarizer.py`  
   - **Secrets:** Add your `HF_TOKEN`.  
4. Your app will be live online 🎉  

---

## 📸 Example Workflow
1. Enter YouTube video URL.  
2. Fetch transcript (auto-detected language).  
3. Translate (if not English).  
4. Generate and display summary.  

---

## 📦 Requirements
Main dependencies:
- `streamlit`  
- `youtube-transcript-api`  
- `transformers`  
- `torch`  
- `huggingface-hub`  
- `langdetect`  

(Full list in `requirements.txt`) 