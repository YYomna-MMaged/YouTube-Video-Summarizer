import streamlit as st
from utils.extractor import extract_id, get_transcript
from utils.chunker import get_chunks
from utils.translator import get_lang_code, translate
from utils.summarizer import summarize_chunks
from utils.cleaner import clean_text

st.set_page_config(page_title="YouTube Summarizer", page_icon="📺", layout="wide")

st.title("📺 YouTube Video Summarizer")
url = st.text_input("Enter YouTube Video URL")

if st.button("Generate Summary"):
    if url:
        with st.spinner("Fetching transcript..."):
            try:
                video_id = extract_id(url)
                transcript = get_transcript(video_id)
            except Exception as e:
                st.error(f"❌ Error fetching transcript: {e}")
                st.stop()

        if transcript.startswith("NO Transcript") or transcript.startswith("ERROR"):
            st.warning(transcript)
        else:
            st.subheader("📜 Transcript (first 500 chars)")
            st.write(transcript[:500] + "...")

            chunks = get_chunks(transcript)
            original_language = get_lang_code(chunks[0])

            if not original_language.startswith("en"):
                translated_chunks = [translate(chunk, original_language, "eng_Latn") for chunk in chunks]
            else:
                translated_chunks = chunks

            with st.spinner("Summarizing..."):
                summary = summarize_chunks(translated_chunks)

            cleaned_final = clean_text(summary)

            st.subheader("✨ Final Summary")
            st.write(cleaned_final)

    else:
        st.warning("Please enter a valid YouTube URL")

            
