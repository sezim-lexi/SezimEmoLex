# SezimEmoLex: Sentiment and Emotion Lexicon for Kazakh Language

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)

**SezimEmoLex** is a Python package for emotion and sentiment analysis of Kazakh text.  
It provides a simple and familiar API inspired by **NRCLex**, allowing text analysis using a lexicon of **8,557 Kazakh words**.

Each word in the lexicon is annotated with:

- **8 emotions**: anger, anticipation, disgust, fear, joy, sadness, surprise, trust  
- **Sentiment polarity**: positive (1), negative (-1), or neutral (0)

This package is designed for researchers, developers, and linguists working with the Kazakh language.

---

## 🚀 Quickstart

Analyze emotions and sentiment in just a few lines of code.

```python
from sezim_emolex import SezimEmoLex, SezimAnalyzer

# Analyze a single word
word = "ашу"
lex = SezimEmoLex(word)

print(lex.word)
print(lex.get_sentiment_label())
print(lex.get_emotions())

# Analyze full text
analyzer = SezimAnalyzer()
text = "мен қатты ашуландым бірақ соңында бәрі жақсы болды"

result = analyzer.analyze(text)

print(result["sentiment_label"])
print(result["emotions"])
```

---

## 📦 Installation

Install directly from GitHub:

```bash
pip install git+https://github.com/sezim-lexi/sezim-emolex.git
```

For development:

```bash
git clone https://github.com/sezim-lexi/sezim-emolex.git
cd sezim-emolex
pip install -e .
```

---

## 📊 Dataset

The lexicon is stored in:

```
data/sezim_emolex.csv
```

It contains **8,557 Kazakh words** annotated with emotions and sentiment.

### Dataset Format

| Column | Description | Type |
|--------|------------|------|
| word | Kazakh word (lemma) | str |
| is_positive | Positive sentiment flag | int |
| is_negative | Negative sentiment flag | int |
| sentiment | Sentiment score (-1/0/1) | int |
| is_neutral | Neutral flag | int |
| anger | Emotion flag | int |
| anticipation | Emotion flag | int |
| disgust | Emotion flag | int |
| fear | Emotion flag | int |
| joy | Emotion flag | int |
| sadness | Emotion flag | int |
| surprise | Emotion flag | int |
| trust | Emotion flag | int |

---

### Statistics

| Metric | Value |
|--------|------|
| Total Words | 8,557 |
| Positive Words | 1,431 (16.7%) |
| Negative Words | 2,479 (29.0%) |
| Neutral Words | 4,647 (54.3%) |

---

## ⚙️ API Reference

### SezimEmoLex(word)

- `lex.word` — input word  
- `lex.found` — True if word exists in lexicon  
- `lex.get_sentiment()` — returns (-1, 0, 1)  
- `lex.get_sentiment_label()` — negative / neutral / positive  
- `lex.get_emotions()` — dict of 8 emotions  
- `lex.has_emotion(name)` — check emotion  
- `lex.get_emotion_count()` — number of emotions  

---

### SezimAnalyzer()

- `analyzer.analyze(text)` returns:

| Field | Description |
|------|-------------|
| sentiment_score | cumulative score |
| sentiment_label | overall sentiment |
| emotions | aggregated counts |
| words_found | matched lexicon words |

---

## 🤝 Contributing

Contributions are welcome!  
Please open an issue or submit a pull request.


## 📚 Citation

If you use **SezimEmoLex** in your research, dataset, or software, please cite the resource as follows:

```bibtex
@misc{sezimemolex2026,
  title        = {SezimEmoLex: A Kazakh Sentiment and Emotion Lexicon},
  author       = {Nazerke Algashbekova and Amandyk Kartbayev},
  year         = {2026},
  note         = {Work in progress — paper under preparation},
  howpublished = {\url{https://github.com/sezim-lexi/SezimEmoLex}}
}
```

We appreciate citations as they support reproducible research and proper attribution of scholarly resources.

