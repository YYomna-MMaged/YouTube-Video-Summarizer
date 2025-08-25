import streamlit as st
from utils.extractor import extract_id, get_transcript
from utils.chunker import get_chunks
# from utils.translator import get_lang_code, translate
from utils.summarizer import summarize_chunks
from utils.cleaner import clean_text
import os
from huggingface_hub import login
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
from langdetect import detect
import langcodes


st.set_page_config(page_title="YouTube Videos Summarizer", page_icon="📺", layout="wide")

st.title("📺 YouTube Video Summarizer")
url = st.text_input("Enter YouTube Video URL")

# def _get_hf_token():
#     return (
#         st.secrets.get("HF_TOKEN")
#         or st.secrets.get("HUGGINGFACE_HUB_TOKEN")
#         or os.environ.get("HF_TOKEN")
#         or os.environ.get("HUGGINGFACE_HUB_TOKEN")
#     )

# token = _get_hf_token()
# if token:
#     login(token=token)
#     os.environ["HUGGINGFACE_HUB_TOKEN"] = token
# else:
#     st.warning("لم يتم العثور على HF_TOKEN في Secrets. قد تواجه Rate-limit أثناء تحميل النماذج.")


trans_tokenizer = AutoTokenizer.from_pretrained("facebook/nllb-200-distilled-600M")
trans_model = AutoModelForSeq2SeqLM.from_pretrained("facebook/nllb-200-distilled-600M")

def get_lang_code(text: str) -> str:
    lang_ios_code = detect(text)
    language = langcodes.Language.get(lang_ios_code)
    script = language.maximize().script
    return f"{lang_ios_code}_{script}"

def translate(text, src_lang, tgt_lang="eng_Latn"):
    translator = pipeline(
        "translation",
        model=trans_model,
        tokenizer=trans_tokenizer,
        src_lang=src_lang,
        tgt_lang=tgt_lang,
        device=0  # 0 = GPU , -1 = CPU
    )
    result = translator(text, max_length=400)
    return result[0]["translation_text"]

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

            summary = summarize_chunks(chunks)
            cleaned_final = clean_text(summary)

            st.subheader("✨ Final Summary")
            st.write(cleaned_final)

    else:
        st.warning("Please enter a valid YouTube URL")

            
