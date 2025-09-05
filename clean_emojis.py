#!/usr/bin/env python3
import re
import sys

def remove_emojis(text):
    # Rimuove tutti gli emoji Unicode
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # flags
        "\U00002700-\U000027BF"  # Dingbats
        "\U0001F900-\U0001F9FF"  # Supplemental Symbols
        "\U00002600-\U000026FF"  # Miscellaneous Symbols
        "\U0001F004-\U0001F0CF"  # Cards
        "\U0001F170-\U0001F251"  # Enclosed characters
        "]+", 
        flags=re.UNICODE
    )
    return emoji_pattern.sub('', text)

# Pulisci app.py
with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

cleaned = remove_emojis(content)

# Sostituisci anche i caratteri problematici nei print
cleaned = cleaned.replace('✅', '[OK]')
cleaned = cleaned.replace('🔥', '[FIRE]')
cleaned = cleaned.replace('🚀', '[LAUNCH]')
cleaned = cleaned.replace('📧', '[EMAIL]')
cleaned = cleaned.replace('🎯', '[TARGET]')

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(cleaned)

print("File pulito dalle emoji!")
