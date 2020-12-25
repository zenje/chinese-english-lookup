import os

from wordentry import WordEntry

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


def main():
    words_dict = populate_words_dict()
    word_lookup = ""
    words_dict_list = list(words_dict.values())

    while word_lookup != "!":
        word_lookup = input(
            "Look up a Chinese word, type 'random', or type '!' to quit: "
        ).strip()

        if word_lookup != "!" and word_lookup != "random":
            found_word = words_dict.get(word_lookup)
            if found_word is not None:
                print(str(found_word) + "\n" + found_word.get_definitions())
            else:
                print("Not found")
        elif word_lookup == "random":
            random_word_entry = random.choice(words_dict_list)
            print(str(random_word_entry) + "\n" + random_word_entry.get_definitions())


if __name__ == "__main__":
    # execute only if run as a script
    main()
