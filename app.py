from flask import Flask, render_template, request
import os
import json
import sys
import pymorphy2
import inspect
from collections import namedtuple

# `pymorphy2` relies on the deprecated ``inspect.getargspec`` which was removed
# in Python 3.11. Provide a compatible implementation that mimics the old
# behaviour using ``inspect.getfullargspec``.
if not hasattr(inspect, "getargspec"):
    ArgSpec = namedtuple("ArgSpec", "args varargs keywords defaults")

    def getargspec(func):
        spec = inspect.getfullargspec(func)
        return ArgSpec(spec.args, spec.varargs, spec.varkw, spec.defaults)

    inspect.getargspec = getargspec

BASE_DIR = getattr(sys, "_MEIPASS", os.path.abspath(os.path.dirname(__file__)))

# Ensure pymorphy2 uses dictionaries bundled with the executable
if getattr(sys, "_MEIPASS", False):
    os.environ.setdefault(
        "PYMORPHY2_DICT_PATH", os.path.join(BASE_DIR, "pymorphy2_dicts_ru", "data")
    )

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static"),
)
morph = pymorphy2.MorphAnalyzer()

LANGUAGE_FOLDER = os.path.join(BASE_DIR, "languages")

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


import webbrowser
import threading

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == '__main__':
    threading.Timer(1.0, open_browser).start()
    app.run(debug=False)