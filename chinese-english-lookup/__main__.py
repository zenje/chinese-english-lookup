import random

from parse import populate_words_dict


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
    main()
