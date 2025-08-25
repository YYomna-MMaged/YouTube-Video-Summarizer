from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_chunks(chunks: list[str]) -> str:
    summary = [summarizer(chunk, max_length=130)[0]["summary_text"] for chunk in chunks]
    return " ".join(summary)
