import random


class WordEntry:
    def __init__(self, simp, trad, pinyin, definitions):
        self.simp = simp
        self.trad = trad
        self.pinyin = pinyin
        self.definitions = definitions

    def __str__(self):
        return self.simp + " | " + self.trad + "【" + self.pinyin + "】"

    def get_definitions(self):
        return "; ".join(str(x) for x in self.definitions)


# num_lines = sum(1 for line in open('data/cedict_1_0_ts_utf-8_mdbg.txt'))
# print(num_lines)


def main():
    words_dict = {}
    with open("../cedict/cedict_1_0_ts_utf-8_mdbg.txt") as file:
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
