from flask import Flask, render_template, request
import os
import json
import pymorphy2

app = Flask(__name__)
morph = pymorphy2.MorphAnalyzer()

LANGUAGE_FOLDER = 'languages'

def load_languages():
    languages = {}
    for filename in os.listdir(LANGUAGE_FOLDER):
        if filename.endswith('.json'):
            with open(os.path.join(LANGUAGE_FOLDER, filename), 'r', encoding='utf-8') as f:
                data = json.load(f)
                lang_key = filename.replace('.json', '')
                languages[lang_key] = data
    return languages

languages_data = load_languages()

def translate(text, dictionary, source_lang):
    words = text.lower().split()
    translated = []

    reverse_dict = {v: k for k, v in dictionary.items()}

    for word in words:
        clean_word = ''.join(char for char in word if char.isalnum())

        if source_lang == "ru":
            parsed = morph.parse(clean_word)
            if parsed:
                normal_form = parsed[0].normal_form
            else:
                normal_form = clean_word
            translated_word = dictionary.get(normal_form, f"[{clean_word}]")
        else:
            translated_word = dictionary.get(clean_word, reverse_dict.get(clean_word, f"[{clean_word}]"))

        translated.append(translated_word)

    return ' '.join(translated)

@app.route('/', methods=['GET', 'POST'])
def index():
    translation = ""
    input_text = ""
    selected_lang = "russian_dunmeri"

    if request.method == 'POST':
        input_text = request.form['input_text']
        selected_lang = request.form['language']
        lang_data = languages_data.get(selected_lang, {})
        dictionary = lang_data.get('dictionary', {})
        source_lang = lang_data.get('source_language', 'ru')
        translation = translate(input_text, dictionary, source_lang)

    return render_template(
        'index.html',
        translation=translation,
        input_text=input_text,
        languages=languages_data,
        selected_lang=selected_lang
    )

if __name__ == '__main__':
    app.run(debug=True)