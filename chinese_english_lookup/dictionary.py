import os
import random

from .wordentry import WordEntry


class Dictionary:
    def __init__(self):
        self.words_dict = {}
        self.parse()

    def parse(self):
        words_dict = {}

        dirname = os.path.dirname(__file__)
        cedict_file = os.path.join(dirname, "cedict/cedict_1_0_ts_utf-8_mdbg.txt")

        with open(cedict_file) as file:
            for line in file:
                if line.startswith("#"):
                    continue

                parts_tuple = line.partition("[")
                words = parts_tuple[0].strip().split()
                trad = words[0]
                simp = words[1]

                py_and_def_tuple = parts_tuple[2].strip().partition("]")
                pinyin = py_and_def_tuple[0]
                definitions = py_and_def_tuple[2].strip(" /").split("/")

                new_word_entry = WordEntry(simp, trad, pinyin, definitions)
                words_dict[simp] = new_word_entry
                words_dict[trad] = new_word_entry

        self.words_dict = words_dict
        self.words_dict_list = list(words_dict.values())

    def lookup(self, word):
        return self.words_dict.get(word.strip())

    def random_entry(self):
        return random.choice(self.words_dict_list)
