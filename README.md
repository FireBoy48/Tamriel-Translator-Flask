
# 🐉 Tamriel Translator Flask

> Веб-приложение на Flask для перевода с русского и английского языков на **данмерский язык** из вселенной **The Elder Scrolls (TES)**.

---

## 🔮 Возможности

✅ Перевод с русского на добавленные языки  
✅ Поддержка морфологии русского языка (распознаёт формы слов: "боги", "богов" → "бог")  
✅ Обратный перевод: данмерский → русский  
✅ Поддержка нескольких языков через JSON-файлы  
✅ Удобный и адаптивный веб-интерфейс  
✅ Лёгкое расширение словаря и добавление новых языков

---

## 🚀 Установка и запуск с помощью Poetry

### 📌 Требования

- Python 3.10
- [Poetry](https://python-poetry.org/docs/#installation)

### 🔹 1. Установите зависимости

```bash
poetry install
```

### 🔹 2. Запустите приложение

```bash
poetry run python app.py
```

### 🔹 3. Откройте в браузере

```
http://127.0.0.1:5000/
```

---

## 🧠 Добавление новых языков

Чтобы добавить новый язык, просто создай JSON-файл в папке `languages/`:

### Пример: `french_dunmeri.json`

```json
{
  "source_language": "fr",
  "target_language": "dunmeri",
  "dictionary": {
    "bonjour": "sera",
    "mort": "dakka",
    "vie": "alma"
  }
}
```

После перезапуска приложения язык появится в выпадающем списке.

---

## 📦 Пример использования

### Ввод:
```
Боги и вода, смерть и тело
```

### Вывод:
```
daedra [и] nalu dakka [и] kogo
```

---

## 🧾 Зависимости

Управляются через `Poetry`:

- `Flask` — веб-фреймворк
- `pymorphy2` — морфологический анализатор русского языка

---

## 🏛 Источники

- 🔗 [UESP Wiki: Dark Elvish](https://en.uesp.net/wiki/Lore:Dark_Elvish)
- 🔗 [Casual Scrolls Wiki: Dunmeri Language](https://casualscrolls.fandom.com/wiki/Dunmeri_language)
- 🎮 TES III: Morrowind, TES Online

---

## 📜 Лицензия

Проект создан в образовательных и фанатских целях.  
Все права на вселенную The Elder Scrolls принадлежат Bethesda Softworks.

---

## 🛠️ TODO / Идеи

- [ ] Озвучка перевода (TTS)
- [ ] История переводов
- [ ] Загрузка пользовательских словарей
- [ ] Дополнение другими языками


