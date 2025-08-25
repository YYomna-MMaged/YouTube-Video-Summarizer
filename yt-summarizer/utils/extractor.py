import regex as re
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, TranscriptsDisabled
from urllib.parse import urlparse, parse_qs, unquote

pattern = re.compile(r"(?:v=|/)([0-9A-Za-z_-]{11})(?:[&?\/]|$)")

def extract_id(url: str) -> str:
    parsed = urlparse(url)
    qs = parse_qs(parsed.query)

    if parsed.path.startswith("/attribution_link") and "u" in qs:
        nested_url = unquote(qs["u"][0])
        if nested_url.startswith("/"):
            re_url = "https://www.youtube.com" + nested_url
        return extract_id(re_url)

    video_id = pattern.search(url)
    if not video_id:
        raise ValueError(f"Cannot extract id from: {url}")
    return video_id.group(1)

def get_transcript(video_id : str, preferred_languages = ("ar", "en")) -> str:
    try:
        api = YouTubeTranscriptApi()
        transcript_list = api.list(video_id) #return all avalibale transcripts

        for language in preferred_languages: #loop over preferred languages
            try:
                transcript = transcript_list.find_transcript([language]) 
                fetched = transcript.fetch()
                return "\n".join(snippet.text for snippet in fetched if snippet.text.strip())
            except NoTranscriptFound: #if no transcript with this language
                continue

        #if no transcript with preferred languages is available, take the transcript with the original/first language
        transcript = next(iter(transcript_list)) 
        fetched = transcript.fetch()
        return "\n".join(part.text for part in fetched if part.text.strip())

    except TranscriptsDisabled: #if the video does not have a transcript
        return "NO Transcript at this video"

    except Exception as e:
        return f"ERROR: {e}"