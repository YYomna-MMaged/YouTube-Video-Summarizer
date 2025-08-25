# 📺 YouTube Video Summarizer

A Streamlit web application that allows you to **summarize YouTube videos** easily.  
It extracts the transcript of a video, translates it to English if needed, and then generates a clean, concise summary using HuggingFace models.
- Try Now: [yyomna-mmaged-youtube-video--yt-summarizereng-summarizer-j4tyhb.streamlit.app/](https://yyomna-mmaged-youtube-video--yt-summarizereng-summarizer-j4tyhb.streamlit.app/)

> **⚠️ Note:**  
> The deployed version currently summarizes **only English transcripts**, since it uses the Facebook summarization model ([facebook/bart-large-cnn](https://huggingface.co/facebook/bart-large-cnn)).
- To see whole code check the notebook
---

## 🚀 Features
- Extracts video transcripts directly from YouTube.
- Detects the original language of the transcript.
- Translates transcripts to English if needed.
- Summarizes long transcripts into concise text.
- User-friendly **Streamlit web interface**.

> **Note:** The deployed application only supports English texts. To see the full project, please see the notebook.

---

## 📂 Project Structure

```bash
yt_summarizer/
├── utils/
│   ├── extractor.py      # Extracts video ID and transcript
│   ├── chunker.py        # Splits transcript into chunks
│   ├── translator.py     # Detects and translates language
│   ├── summarizer.py     # Summarizes chunks using HuggingFace
│   ├── cleaner.py        # Cleans and formats final summary
│
├── all_summarizer.py     # Main Streamlit application
├── requirements.txt      # Project dependencies
```

## 🛠️ Installation

1. Clone this repository:
```bash
   git clone https://github.com/YYomna-MMaged/YouTube-Video-Summarizer.git
   cd YouTube-Video-Summarizer/yt_summarizer
```
2. Create a virtual environment and activate it:
```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```
3. Install dependencies:
```bash
pip install -r requirements.txt
``` 

## 🌐 Deployment (Streamlit Cloud)
1. Push your code to GitHub.  
2. Go to [Streamlit Cloud](https://share.streamlit.io/).  
3. Deploy the repo and set:  
   - **Main file path:** `yt_summarizer/eng_summarizer.py`  
4. Your app will be live online 🎉  

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