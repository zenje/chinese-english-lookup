import random

from .dictionary import Dictionary


def main():
    dictionary = Dictionary()
    word_lookup = ""

    while word_lookup != "!":
        word_lookup = input(
            "\nLook up a Chinese word, type 'random', or type '!' to quit: "
        ).strip()

        if word_lookup != "!" and word_lookup != "random":
            found_word = dictionary.lookup(word_lookup)
            if found_word is not None:
                print(
                    str(found_word)
                    + "\n"
                    + found_word.get_definition_entries_formatted()
                )
            else:
                print("Not found")
        elif word_lookup == "random":
            random_word_entry = dictionary.random_entry()
            print(
                str(random_word_entry)
                + "\n"
                + random_word_entry.get_definition_entries_formatted()
            )


if __name__ == "__main__":
    main()
