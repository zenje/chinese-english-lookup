import os
import random
from enum import Enum

from .dictionary import Dictionary
from .wordentry import WordEntry, DefinitionEntry


class HSK2:
    """HSK2.0 utility for 2010-2020, categorizing Chinese words by difficulty.

    Parses HSK2.0 file on initialization. Contains 6 levels, from 1 (entry) to 6 (advanced).

    Attributes:
        dictionary: Optional Dictionary instance. If not provided, a new Dictionary instance will be instantiated.
    """

    def __init__(self, dictionary: Dictionary = None):
        if dictionary is None:
            dictionary = Dictionary()
        self.level_list = []  # contains levels to lists of WordEntry
        self.word_to_level_map = {}  # for retrieving level of given word
        self.dictionary = dictionary
        self.parse()

    def parse(self):
        """Parses the HSK2.0 file.

        Called on initialization of HSK2 instance. For each level in HSK2.0, a new entry is added to `level_list`; each level contains a list of corresponding words.
        """
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
        """Returns the corresponding HSK level for the given word.

        Args:
            word: The string of the Chinese word to look up (can be multiple characters).

        Returns:
            An integer - the corresponding HSK level (1-6) of the Chinese word, if found. Otherwise, returns None.
        """
        word = word.strip()
        if word in self.word_to_level_map:
            return self.word_to_level_map.get(word)
        return None

    def get_words_for_level(self, level):
        """Returns the words corresponding to the given HSK level.

        Args:
            level: An integer >=1 and <=6 representing the desired HSK level.

        Returns:
            A list containing the words for the given HSK level.

        Raises:
            ValueError: Error if the `level` argument is invalid.
        """
        if level < 1 or level > 6:
            raise ValueError("Level must be from 1 - 6")
        return self.level_list[level - 1]
