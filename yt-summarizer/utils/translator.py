from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
from langdetect import detect
import langcodes

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
