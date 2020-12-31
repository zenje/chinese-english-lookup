import os
import random
from enum import Enum

from .dictionary import Dictionary
from .wordentry import WordEntry, DefinitionEntry


class Category(Enum):
    """Enum class representing the categories for HSK3.0.

    Attributes:
        title: The string name of the category.
        index: The integer representing the associated index, used by the HSK3 class.
    """

    ENTRY = ("普及化 - Entry Level", 0)
    INTERMEDIATE = ("中级 - Intermediate Level", 1)
    ADVANCED = ("高级 - Advanced Level", 2)
    SUPPLEMENTAL = ("附录 - Supplemental Vocab", 3)

    def __init__(self, title, index):
        self.title = title
        self.index = index

    @classmethod
    def get_by_index(cls, index):
        for c in cls:
            if c.index == index:
                return c


class HSK3:
    """HSK3.0 utility for post-2020, categorizing Chinese words by difficulty.

    Parses HSK2.0 file on initialization. Contains 4 categories: entry, intermediate, advanced, supplemental.

    Attributes:
        dictionary: Optional Dictionary instance. If not provided, a new Dictionary instance will be instantiated.
    """

    def __init__(self, dictionary: Dictionary = Dictionary()):
        self.category_list = []  # contains categories to lists of WordEntry
        self.word_to_category_map = {}  # for retrieving category of given word
        self.dictionary = dictionary
        self.parse()

    def parse(self):
        """Parses the HSK3.0 file.

        Called on initialization of HSK3 instance. For each category in HSK3.0, a new entry is added to `category_list`; each category contains a list of corresponding words.
        """

        dirname = os.path.dirname(__file__)
        hsk_file = os.path.join(dirname, "hsk/HSK3.0 wordlist [post-2020].txt")

        category_index = -1
        category_words = None

        with open(hsk_file) as file:
            for line in file:

                # read new category for words that follow
                if line.startswith("//"):
                    category_words = []
                    self.category_list.append(category_words)
                    category_index += 1
                    continue

                word = line.strip()
                word_entry = self.dictionary.lookup(word)
                if word_entry is not None:
                    category_words.append(word_entry)
                    self.word_to_category_map[word] = category_index

    def get_category_for_word(self, word):
        """Returns the corresponding HSK category for the given word.

        Args:
            word: The string of the Chinese word to look up (can be multiple characters).

        Returns:
            The string name of the HSK category associated to the word, if found. Otherwise, returns None.
        """
        word = word.strip()
        if word in self.word_to_category_map:
            category_index = self.word_to_category_map.get(word)
            return Category.get_by_index(category_index).title
        return None

    def get_words_for_category(self, category=Category):
        """Returns the words corresponding to the given HSK category.

        Args:
            category: The Category to get words for.

        Returns:
            A list containing the words for the given HSK category.
        """
        return self.category_list[category.index]

    def get_entry(self):
        """Returns the words corresponding to HSK Entry level."""
        return self.get_words_for_category(Category.ENTRY)

    def get_intermediate(self):
        """Returns the words corresponding to HSK Intemediate level."""
        return self.get_words_for_category(Category.INTERMEDIATE)

    def get_advanced(self):
        """Returns the words corresponding to HSK Advanced level."""
        return self.get_words_for_category(Category.ADVANCED)

    def get_supplemental(self):
        """Returns the words corresponding to HSK Supplemental level."""
        return self.get_words_for_category(Category.SUPPLEMENTAL)
