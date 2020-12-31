class WordEntry:
    """Contains info about a word-definition entry of Chinese-English dictionary CC-CEDICT.

    Attributes:
        simp: A string with the simplified representation of the word.
        trad: A string with the traditional representation of the word.
    """

    def __init__(self, simp, trad):
        self.simp = simp
        self.trad = trad
        self.definition_entries = []

    def __str__(self):
        """Returns string representation of WordEntry.

        Returns:
            String representation, including simplified and traditional forms and definitions. Examples:

            '代码 | 代碼\n【dai4 ma3】 code'
            '软件 | 軟件\n【ruan3 jian4】 (computer) software'
        """
        return (
            self.simp
            + " | "
            + self.trad
            + "\n"
            + self.get_definition_entries_formatted()
        )

    def add_definition_entry(self, definition_entry):
        """Adds a new definition entry corresponding to the word.

        Args:
             definition_entry: The definition to add.
        """
        self.definition_entries.append(definition_entry)

    def get_definition_entries_formatted(self):
        """Returns a formatted string of the entry's definitions.

        Returns:
            Formatted string representation of entry's definition. If the word contains more than one definition, then the definitions will be enumerated. Examples:

            '1) 【hao3】 good; well; proper; good to; easy to; very; so; (suffix indicating completion or readiness); (of two people) close; on intimate terms; (after a personal pronoun) hello\n2) 【hao4】 to be fond of; to have a tendency to; to be prone to'
            '【huai4】 bad; spoiled; broken; to break down; (suffix) to the utmost'
        """

        count = len(self.definition_entries)
        if count > 1:
            defs = []
            for index, entry in enumerate(self.definition_entries):
                defs.append(str(index + 1) + ") " + str(entry))
            return "\n".join(defs)

        elif count == 1:
            return str(self.definition_entries[0])


class DefinitionEntry:
    """Contains the pinyin and definition corresponding to a Chinese word.

    A given Chinese word may have multiple associated DefinitionEntries (i.e., different pinyin along with different definitions).

    Attributes:
        pinyin: A string containing the pinyin representation of a word, using numbers to indicate tones (e.g., "hao3").
        definitions: A list of strings of different definitions / meanings for the word.
    """

    def __init__(self, pinyin, definitions=[]):
        self.pinyin = pinyin
        self.definitions = definitions

    def __str__(self):
        """Returns string representation of DefinitionEntry.

        Returns:
            String representation, with pinyin and all definitions for this entry. Examples:

            '【wu2 liao2】 bored; boring; senseless'
            '【hao4 qi2】 inquisitive; curious; inquisitiveness; curiosity'
        """
        return (
            "【" + self.pinyin + "】" + " " + "; ".join(str(x) for x in self.definitions)
        )
