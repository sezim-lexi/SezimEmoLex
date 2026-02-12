"""
SezimEmoLex - Kazakh Sentiment & Emotion Lexicon

A comprehensive lexicon of 8,557 Kazakh words annotated with:
- 8 emotions: anger, anticipation, disgust, fear, joy, sadness, surprise, trust
- Sentiment polarity: positive (1), negative (-1), neutral (0)

Example:
    >>> from sezim_emolex import SezimEmoLex, SezimAnalyzer
    >>> lex = SezimEmoLex("абайлау")
    >>> lex.get_emotions()
    {'anger': 0, 'anticipation': 0, 'disgust': 0, 'fear': 0, 
     'joy': 0, 'sadness': 0, 'surprise': 0, 'trust': 0}
    >>> lex.get_sentiment()
    0
    
    >>> analyzer = SezimAnalyzer()
    >>> result = analyzer.analyze("абайлау құлақ")
    >>> result['sentiment_label']
    'neutral'
"""

from .lexicon import SezimEmoLex, SezimAnalyzer

__version__ = "1.0.0"
__author__ = "SEZIM Contributors"
__license__ = "CC-BY-4.0 (data), MIT (code)"

__all__ = [
    'SezimEmoLex',
    'SezimAnalyzer',
    '__version__',
    '__author__',
    '__license__',
]
