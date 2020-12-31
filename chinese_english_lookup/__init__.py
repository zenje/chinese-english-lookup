"""Contains utilities for Chinese-English dictionary, HSK3.0, and HSK2.0.

    Usage examples:
    
        dictionary = Dictionary()
        found_word_entry = dictionary.lookup('词典')
        
        hsk3 = HSK3()
        intermediate_words = hsk3.get_intermediate()
        for word in intermediate_words:
            print(word)
            
        hsk2 = HSK2()
        level_3_words = hsk2.get_words_for_level(3)
        for word in level_3_words:
            print(word)
"""

from .dictionary import Dictionary
from .hsk2 import HSK2
from .hsk3 import HSK3, Category as HSK3Category

__all__ = ["Dictionary", "HSK2", "HSK3", "HSK3Category"]
