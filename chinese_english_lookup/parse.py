import os

from .wordentry import WordEntry

dirname = os.path.dirname(__file__)
cedict_file = os.path.join(dirname, "cedict/cedict_1_0_ts_utf-8_mdbg.txt")


def populate_words_dict():
    words_dict = {}

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

    return words_dict
