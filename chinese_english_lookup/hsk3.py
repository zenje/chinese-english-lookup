import os
import random
from enum import Enum

from .dictionary import Dictionary
from .wordentry import WordEntry, DefinitionEntry


class Category(Enum):
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


"""
    HSK3.0 utility:
    - Contains 4 categories: entry, intermediate, advanced, supplementary
"""


class HSK3:
    def __init__(self, dictionary: Dictionary = Dictionary()):
        self.category_list = []  # contains categories to lists of WordEntry
        self.word_to_category_map = {}  # for retrieving category of given word
        self.dictionary = dictionary
        self.parse()

    def parse(self):
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
        word = word.strip()
        if word in self.word_to_category_map:
            category_index = self.word_to_category_map.get(word)
            return Category.get_by_index(category_index).title
        return None

    def get_words_for_category(self, category=Category):
        return self.category_list[category.index]

    def get_entry(self):
        return self.get_words_for_category(Category.ENTRY)

    def get_intermediate(self):
        return self.get_words_for_category(Category.INTERMEDIATE)

    def get_advanced(self):
        return self.get_words_for_category(Category.ADVANCED)

    def get_supplemental(self):
        return self.get_words_for_category(Category.SUPPLEMENTAL)
