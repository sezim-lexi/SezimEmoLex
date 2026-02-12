> # SezimEmoLex: Kazakh Sentiment & Emotion Lexicon

[![PyPI version](https://badge.fury.io/py/sezim-emolex.svg)](https://badge.fury.io/py/sezim-emolex) <!--- Placeholder -->
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Data License: CC BY 4.0](https://img.shields.io/badge/Data%20License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

**SezimEmoLex** is a Python package for emotion and sentiment analysis of Kazakh text. It provides a simple and familiar API, inspired by `NRCLex`, to analyze text using a comprehensive lexicon of **8,557 Kazakh words**.

Each word in the lexicon is annotated with:
- **8 emotions**: `anger`, `anticipation`, `disgust`, `fear`, `joy`, `sadness`, `surprise`, `trust`
- **Sentiment polarity**: `positive` (1), `negative` (-1), or `neutral` (0)

This package is ideal for researchers, developers, and linguists working with the Kazakh language.

---

## 🚀 Quickstart

Analyze emotions and sentiment in just a few lines of code.

```python
from sezim_emolex import SezimEmoLex, SezimAnalyzer

# --- Analyze a single word ---
word = "ашу"
lex = SezimEmoLex(word)

print(f"Word: {lex.word}")
# >>> Word: ашу

print(f"Sentiment: {lex.get_sentiment_label()}")
# >>> Sentiment: negative

print(f"Emotions: {lex.get_emotions()}")
# >>> Emotions: {'anger': 1, 'anticipation': 0, ...}

# --- Analyze a full text ---
analyzer = SezimAnalyzer()
text = "мен қатты ашуландым бірақ соңында бәрі жақсы болды"

result = analyzer.analyze(text)

print(f"\nText: '{result['text']}'")
# >>> Text: 'мен қатты ашуландым бірақ соңында бәрі жақсы болды'

print(f"Overall Sentiment: {result['sentiment_label']}")
# >>> Overall Sentiment: neutral

print(f"Emotion Scores: {result['emotions']}")
# >>> Emotion Scores: {'anger': 1, 'joy': 1, ...}
```

## 📦 Installation

Install the package directly from GitHub:

```bash
pip install git+https://github.com/YOUR-USERNAME/SezimEmoLex.git
```

Or, for development, clone the repository and install in editable mode:

```bash
git clone https://github.com/YOUR-USERNAME/SezimEmoLex.git
cd SezimEmoLex
pip install -e .
```

## 📊 Dataset

The lexicon is stored in `data/sezim_emolex.csv` and is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

### Dataset Format

The CSV file contains the following columns:

| Column | Description | Type |
| :--- | :--- | :--- |
| `word` | The Kazakh word (lemma) | `str` |
| `is_positive` | Binary flag for positive sentiment | `int` (0/1) |
| `is_negative` | Binary flag for negative sentiment | `int` (0/1) |
| `sentiment` | Overall sentiment score | `int` (-1/0/1) |
| `is_neutral` | Binary flag for neutral sentiment | `int` (0/1) |
| `anger` | Binary flag for the emotion | `int` (0/1) |
| `anticipation`| Binary flag for the emotion | `int` (0/1) |
| `disgust` | Binary flag for the emotion | `int` (0/1) |
| `fear` | Binary flag for the emotion | `int` (0/1) |
| `joy` | Binary flag for the emotion | `int` (0/1) |
| `sadness` | Binary flag for the emotion | `int` (0/1) |
| `surprise` | Binary flag for the emotion | `int` (0/1) |
| `trust` | Binary flag for the emotion | `int` (0/1) |

### Statistics

| Metric | Value |
| :--- | :--- |
| **Total Words** | 8,557 |
| **Positive Words** | 1,431 (16.7%) |
| **Negative Words** | 2,479 (29.0%) |
| **Neutral Words** | 4,647 (54.3%) |

## ⚙️ API Reference

### `SezimEmoLex(word)`

Analyzes a single word.

- **`lex.word`**: The input word.
- **`lex.found`**: `True` if the word was found in the lexicon.
- **`lex.get_sentiment()`**: Returns sentiment score (-1, 0, 1).
- **`lex.get_sentiment_label()`**: Returns sentiment label (`'negative'`, `'neutral'`, `'positive').
- **`lex.get_emotions()`**: Returns a dictionary of all 8 emotions with binary scores.
- **`lex.has_emotion('fear')`**: Returns `True` if the word has the specified emotion.
- **`lex.get_emotion_count()`**: Returns the total number of emotions associated with the word.

### `SezimAnalyzer()`

Analyzes a string of text.

- **`analyzer.analyze(text)`**: Returns a dictionary with detailed analysis, including:
  - `sentiment_score`: The cumulative sentiment score of all found words.
  - `sentiment_label`: The overall sentiment of the text.
  - `emotions`: A dictionary with the cumulative count for each emotion.
  - `words_found`: The number of words from the text found in the lexicon.

## 📜 License

- The **source code** is licensed under the [MIT License](LICENSE).
- The **dataset** (`data/sezim_emolex.csv`) is licensed under the [Creative Commons Attribution 4.0 International (CC BY 4.0)](data/LICENSE_DATA.md).

## ✍️ Citation

If you use this dataset or software in your research, please cite it. You can use the "Cite this repository" feature on the GitHub page.

```bibtex
@software{Algashbekova_SezimEmoLex_2026,
  author = {Algashbekova, Nazerke and Manus AI},
  title = {{SezimEmoLex: A Kazakh Emotion Lexicon}},
  month = feb,
  year = 2026,
  publisher = {GitHub},
  url = {https://github.com/YOUR-USERNAME/SezimEmoLex}
}
```

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request.

---

*This package was developed with the assistance of Manus AI.*
