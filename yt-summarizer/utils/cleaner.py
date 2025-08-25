import regex as re

def clean_text(text: str) -> str:
    text = re.sub(r"[^\p{L}\p{N}\s.!?,:;/-]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()

    for phrase_length in range(20, 0, -1):
        if phrase_length == 1:
            text = re.sub(r'\b(\w+)(\s+\1\b)+', r'\1', text)
        else:
            pattern = r'\b((?:\w+\s+){' + str(phrase_length-1) + r'}\w+)(\s+\1\b)+'
            text = re.sub(pattern, r'\1', text)
    
    def remove_non_adjacent_duplicates(text):
        words = text.split()
        if len(words) < 4:
            return text
        
        phrase_counts = {} 
        
        for length in range(2, 7):
            for i in range(len(words) - length + 1):
                phrase = tuple(words[i:i+length])
                if phrase not in phrase_counts:
                    phrase_counts[phrase] = []
                phrase_counts[phrase].append(i)
        
        duplicates_to_remove = []
        for phrase, positions in phrase_counts.items():
            if len(positions) > 1 and len(phrase) >= 2:
                duplicates_to_remove.extend(positions[1:])
        
        duplicates_to_remove.sort(reverse=True)
        
        result_words = words.copy()
        for pos in duplicates_to_remove:
            for phrase, positions in phrase_counts.items():
                if pos in positions[1:]: 
                    phrase_len = len(phrase)
                    for _ in range(phrase_len):
                        if pos < len(result_words):
                            result_words.pop(pos)
                    break
        
        return ' '.join(result_words)
    
    text = remove_non_adjacent_duplicates(text)
    
    text = re.sub(r"\s+", " ", text).strip()

    sentences = re.split(r'[.!?\n]+', text)
    seen = set()
    unique_sentences = []
    
    for sentence in sentences:
        sentence = sentence.strip()
        sentence = re.sub(r'^[^\w]+|[^\w]+$', '', sentence).strip()
        
        if sentence and len(sentence) > 2:
            sentence_lower = sentence.lower()
            if sentence_lower not in seen:
                seen.add(sentence_lower)
                unique_sentences.append(sentence)
    
    if unique_sentences:
        result = ". ".join(unique_sentences)
        if not result.endswith(('.', '!', '?')):
            result += "."
        return result
    else:
        return text