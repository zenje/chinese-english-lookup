import os
import random
from enum import Enum

from .dictionary import Dictionary
from .wordentry import WordEntry, DefinitionEntry


class HSK2:
    """
    HSK2.0 utility:
    - Contains 4 categories: entry, intermediate, advanced, supplementary
    """

    def __init__(self, dictionary: Dictionary = Dictionary()):
        self.level_list = []  # contains levels to lists of WordEntry
        self.word_to_level_map = {}  # for retrieving level of given word
        self.dictionary = dictionary
        self.parse()

    def parse(self):
        dirname = os.path.dirname(__file__)
        hsk_file = os.path.join(dirname, "hsk/HSK2.0 wordlist [2010-2020].txt")

        level_index = 0
        level_words = None

        with open(hsk_file, encoding="utf-8-sig") as file:
            for line in file:

                # read new level for words that follow
                if line.strip().startswith("//"):
                    level_words = []
                    self.level_list.append(level_words)
                    level_index += 1
                    continue

                split_line = line.strip().split("\t")
                word = split_line[0]
                word_entry = self.dictionary.lookup(word)
                if word_entry is not None:
                    level_words.append(word_entry)
                    self.word_to_level_map[word] = level_index

    def get_level_for_word(self, word):
        word = word.strip()
        if word in self.word_to_level_map:
            return self.word_to_level_map.get(word)
        return None

    def get_words_for_level(self, level):
        if level < 1 or level > 6:
            raise ValueError("Level must be from 1 - 6")
        return self.level_list[level - 1]
