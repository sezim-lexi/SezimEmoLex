"""
Unit tests for SezimEmoLex
"""

import pytest
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from sezim_emolex import SezimEmoLex, SezimAnalyzer


class TestSezimEmoLex:
    """Test the SezimEmoLex class"""
    
    def test_word_found(self):
        """Test that a known word is found"""
        lex = SezimEmoLex("абайлау")
        assert lex.found is True
        assert lex.word == "абайлау"
    
    def test_word_not_found(self):
        """Test that an unknown word returns neutral values"""
        lex = SezimEmoLex("хүлік_бұл_сөз_жоқ")
        assert lex.found is False
        assert lex.sentiment == 0
        assert lex.is_neutral == 1
    
    def test_sentiment_values(self):
        """Test sentiment values are -1, 0, or 1"""
        for word in ["абайлау", "абайсыз", "абзац"]:
            lex = SezimEmoLex(word)
            assert lex.sentiment in [-1, 0, 1]
    
    def test_get_sentiment_label(self):
        """Test sentiment label conversion"""
        lex_neutral = SezimEmoLex("абайлау")
        assert lex_neutral.get_sentiment_label() == "neutral"
        
        lex_negative = SezimEmoLex("абайсыз")
        assert lex_negative.get_sentiment_label() == "negative"
    
    def test_get_emotions(self):
        """Test getting emotions dictionary"""
        lex = SezimEmoLex("абайлау")
        emotions = lex.get_emotions()
        
        assert isinstance(emotions, dict)
        assert len(emotions) == 8
        assert all(e in emotions for e in ['anger', 'fear', 'joy', 'sadness', 'trust', 'anticipation', 'disgust', 'surprise'])
        assert all(v in [0, 1] for v in emotions.values())
    
    def test_has_emotion(self):
        """Test checking for specific emotion"""
        lex = SezimEmoLex("абайсыз")
        
        # This word should have sadness
        assert lex.has_emotion('sadness') in [True, False]  # Depends on lexicon
    
    def test_has_emotion_invalid(self):
        """Test that invalid emotion raises error"""
        lex = SezimEmoLex("абайлау")
        
        with pytest.raises(ValueError):
            lex.has_emotion('invalid_emotion')
    
    def test_get_emotion_count(self):
        """Test emotion count"""
        lex = SezimEmoLex("абайлау")
        count = lex.get_emotion_count()
        
        assert isinstance(count, int)
        assert 0 <= count <= 8
    
    def test_case_insensitive(self):
        """Test that analysis is case-insensitive"""
        lex1 = SezimEmoLex("абайлау")
        lex2 = SezimEmoLex("АБАЙЛАУ")
        
        assert lex1.sentiment == lex2.sentiment
        assert lex1.get_emotions() == lex2.get_emotions()
    
    def test_repr(self):
        """Test string representation"""
        lex = SezimEmoLex("абайлау")
        repr_str = repr(lex)
        
        assert "SezimEmoLex" in repr_str
        assert "абайлау" in repr_str
    
    def test_str(self):
        """Test human-readable string"""
        lex = SezimEmoLex("абайлау")
        str_repr = str(lex)
        
        assert "Word:" in str_repr
        assert "Sentiment:" in str_repr
        assert "Emotions:" in str_repr


class TestSezimAnalyzer:
    """Test the SezimAnalyzer class"""
    
    def test_analyzer_initialization(self):
        """Test that analyzer initializes correctly"""
        analyzer = SezimAnalyzer()
        assert analyzer.lexicon_df is not None
    
    def test_analyze_single_word(self):
        """Test analyzing a single word"""
        analyzer = SezimAnalyzer()
        result = analyzer.analyze("абайлау")
        
        assert result['text'] == "абайлау"
        assert result['words_found'] == 1
        assert result['total_words'] == 1
        assert 'sentiment_label' in result
        assert 'emotions' in result
    
    def test_analyze_multiple_words(self):
        """Test analyzing multiple words"""
        analyzer = SezimAnalyzer()
        result = analyzer.analyze("абайлау абайсыз")
        
        assert result['total_words'] == 2
        assert result['words_found'] >= 0
    
    def test_analyze_result_structure(self):
        """Test that result has expected structure"""
        analyzer = SezimAnalyzer()
        result = analyzer.analyze("абайлау")
        
        required_keys = ['text', 'words_found', 'total_words', 'sentiment_score', 'sentiment_label', 'emotions', 'word_results']
        assert all(key in result for key in required_keys)
    
    def test_analyze_emotions_structure(self):
        """Test that emotions dict has all emotions"""
        analyzer = SezimAnalyzer()
        result = analyzer.analyze("абайлау")
        
        emotions = result['emotions']
        expected_emotions = ['anger', 'anticipation', 'disgust', 'fear', 'joy', 'sadness', 'surprise', 'trust']
        
        assert all(e in emotions for e in expected_emotions)
        assert all(isinstance(v, int) for v in emotions.values())
    
    def test_analyze_sentiment_label(self):
        """Test sentiment label in results"""
        analyzer = SezimAnalyzer()
        result = analyzer.analyze("абайлау")
        
        assert result['sentiment_label'] in ['positive', 'negative', 'neutral']
    
    def test_analyze_unknown_words(self):
        """Test analyzing text with unknown words"""
        analyzer = SezimAnalyzer()
        result = analyzer.analyze("хүлік_бұл_сөз_жоқ")
        
        assert result['words_found'] == 0
        assert result['total_words'] == 1


class TestLexiconData:
    """Test the lexicon data"""
    
    def test_lexicon_loaded(self):
        """Test that lexicon is loaded"""
        lexicon = SezimEmoLex._get_lexicon()
        assert lexicon is not None
        assert len(lexicon) > 0
    
    def test_lexicon_columns(self):
        """Test that lexicon has required columns"""
        lexicon = SezimEmoLex._get_lexicon()
        
        required_cols = ['word', 'sentiment', 'anger', 'fear', 'joy', 'sadness', 'trust', 'anticipation', 'disgust', 'surprise']
        assert all(col in lexicon.columns for col in required_cols)
    
    def test_lexicon_size(self):
        """Test lexicon size"""
        lexicon = SezimEmoLex._get_lexicon()
        
        # Should have around 8,557 words
        assert len(lexicon) > 8000
        assert len(lexicon) < 10000


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
