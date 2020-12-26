class WordEntry:
    def __init__(self, simp, trad):
        self.simp = simp
        self.trad = trad
        self.definition_entries = []

    def __str__(self):
        return self.simp + " | " + self.trad

    def add_definition_entry(self, definition_entry):
        self.definition_entries.append(definition_entry)

    def get_definition_entries_formatted(self):
        count = len(self.definition_entries)
        if count > 1:
            defs = []
            for index, entry in enumerate(self.definition_entries):
                defs.append(str(index + 1) + ") " + str(entry))
            return "\n".join(defs)

        elif count == 1:
            return str(self.definition_entries[0])


class DefinitionEntry:
    def __init__(self, pinyin, definitions=[]):
        self.pinyin = pinyin
        self.definitions = definitions

    def __str__(self):
        return (
            "【" + self.pinyin + "】" + " " + "; ".join(str(x) for x in self.definitions)
        )
