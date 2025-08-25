import regex as re

stop = re.compile(r"[\p{P}\p{Zs}\n\t]")

def get_chunks(text: str, chunk_size=500) -> list[str]:
    chunks = []
    while len(text) > chunk_size:
        match = list(stop.finditer(text[:chunk_size]))
        split_at = match[-1].end() if match else chunk_size
        chunks.append(text[:split_at].strip())
        text = text[split_at:].lstrip()

    if text:
        chunks.append(text.strip())
    return chunks