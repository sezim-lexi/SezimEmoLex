"""
SezimEmoLex - Kazakh Sentiment & Emotion Lexicon
Main lexicon class for emotion and sentiment analysis
"""

import pandas as pd
from pathlib import Path
from typing import Dict, List, Optional, Tuple


class SezimEmoLex:
    """
    SezimEmoLex: A Kazakh Sentiment & Emotion Lexicon
    
    Provides emotion and sentiment analysis for Kazakh text using a comprehensive
    lexicon of 8,557 Kazakh words annotated with 8 emotions and sentiment polarity.
    
    Emotions: anger, anticipation, disgust, fear, joy, sadness, surprise, trust
    Sentiment: positive (1), negative (-1), neutral (0)
    
    Example:
        >>> lex = SezimEmoLex("абайлау")
        >>> lex.affect_dict
        {'anger': 0, 'anticipation': 0, 'disgust': 0, 'fear': 0, 
         'joy': 0, 'sadness': 0, 'surprise': 0, 'trust': 0}
        >>> lex.raw_emotion_scores
        {'anger': 0, 'anticipation': 0, 'disgust': 0, 'fear': 0, 
         'joy': 0, 'sadness': 0, 'surprise': 0, 'trust': 0}
        >>> lex.sentiment
        0
    """
    
    EMOTIONS = ['anger', 'anticipation', 'disgust', 'fear', 'joy', 'sadness', 'surprise', 'trust']
    _lexicon_cache = None
    
    def __init__(self, word: str):
        """
        Initialize SezimEmoLex with a Kazakh word.
        
        Args:
            word: Kazakh word to analyze
        """
        self.word = word.lower().strip()
        self._lexicon_df = self._get_lexicon()
        self._analyze()
    
    @classmethod
    def _get_lexicon(cls):
        """Load the lexicon CSV file (cached)"""
        if cls._lexicon_cache is None:
            data_path = Path(__file__).parent.parent.parent / 'data' / 'sezim_emolex.csv'
            
            if not data_path.exists():
                raise FileNotFoundError(
                    f"Lexicon file not found: {data_path}\n"
                    "Make sure the package is installed correctly."
                )
            
            cls._lexicon_cache = pd.read_csv(data_path, encoding='utf-8')
        
        return cls._lexicon_cache
    
    def _analyze(self):
        """Analyze the word and extract emotions and sentiment"""
        row = self._lexicon_df[self._lexicon_df['word'] == self.word]
        
        if row.empty:
            self.found = False
            self.affect_dict = {emotion: 0 for emotion in self.EMOTIONS}
            self.raw_emotion_scores = {emotion: 0 for emotion in self.EMOTIONS}
            self.sentiment = 0
            self.is_positive = 0
            self.is_negative = 0
            self.is_neutral = 1
        else:
            self.found = True
            row_dict = row.iloc[0].to_dict()
            
            self.affect_dict = {emotion: int(row_dict.get(emotion, 0)) for emotion in self.EMOTIONS}
            self.raw_emotion_scores = self.affect_dict.copy()
            
            self.sentiment = int(row_dict.get('sentiment', 0))
            self.is_positive = int(row_dict.get('is_positive', 0))
            self.is_negative = int(row_dict.get('is_negative', 0))
            self.is_neutral = int(row_dict.get('is_neutral', 0))
    
    def get_emotions(self) -> Dict[str, int]:
        """Get all emotions for the word."""
        return self.affect_dict.copy()
    
    def get_sentiment(self) -> int:
        """Get sentiment polarity (1, -1, or 0)."""
        return self.sentiment
    
    def get_sentiment_label(self) -> str:
        """Get sentiment as a label ('positive', 'negative', or 'neutral')."""
        if self.sentiment == 1:
            return 'positive'
        elif self.sentiment == -1:
            return 'negative'
        else:
            return 'neutral'
    
    def has_emotion(self, emotion: str) -> bool:
        """Check if word has a specific emotion."""
        if emotion not in self.EMOTIONS:
            raise ValueError(f"Unknown emotion: {emotion}. Valid emotions: {self.EMOTIONS}")
        return bool(self.affect_dict.get(emotion, 0))
    
    def get_emotion_count(self) -> int:
        """Get total number of emotions for the word."""
        return sum(self.affect_dict.values())
    
    def __repr__(self) -> str:
        """String representation"""
        return (
            f"SezimEmoLex(word='{self.word}', sentiment={self.get_sentiment_label()}, "
            f"emotions={self.get_emotion_count()})"
        )
    
    def __str__(self) -> str:
        """Human-readable string"""
        emotions_str = ', '.join([e for e in self.EMOTIONS if self.affect_dict[e]])
        if not emotions_str:
            emotions_str = 'none'
        return (
            f"Word: {self.word}\n"
            f"Sentiment: {self.get_sentiment_label()}\n"
            f"Emotions: {emotions_str}"
        )


class SezimAnalyzer:
    """
    Analyze text for emotions and sentiment using SezimEmoLex.
    
    Example:
        >>> analyzer = SezimAnalyzer()
        >>> text = "абайлау құлақ"
        >>> result = analyzer.analyze(text)
        >>> result['sentiment_score']
        0
        >>> result['emotions']
        {'anger': 0, 'fear': 0, ...}
    """
    
    def __init__(self):
        """Initialize the analyzer"""
        self.lexicon_df = SezimEmoLex._get_lexicon()
    
    def analyze(self, text: str) -> Dict:
        """Analyze text for emotions and sentiment."""
        words = text.lower().split()
        
        emotions = {emotion: 0 for emotion in SezimEmoLex.EMOTIONS}
        sentiment_score = 0
        found_words = 0
        word_results = []
        
        for word in words:
            lex = SezimEmoLex(word)
            if lex.found:
                found_words += 1
                sentiment_score += lex.sentiment
                
                for emotion in SezimEmoLex.EMOTIONS:
                    emotions[emotion] += lex.affect_dict[emotion]
                
                word_results.append({
                    'word': word,
                    'sentiment': lex.get_sentiment_label(),
                    'emotions': lex.get_emotions()
                })
        
        return {
            'text': text,
            'words_found': found_words,
            'total_words': len(words),
            'sentiment_score': sentiment_score,
            'sentiment_label': 'positive' if sentiment_score > 0 else ('negative' if sentiment_score < 0 else 'neutral'),
            'emotions': emotions,
            'word_results': word_results
        }
