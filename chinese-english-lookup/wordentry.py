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
