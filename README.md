# chinese-cccedict-parser

A simple Python package for Chinese-to-English word definition retrieval. Definitions sourced from Chinese-English dictionary [CC-CEDICT](https://www.mdbg.net/chinese/dictionary?page=cc-cedict).

## Installation

```bash
pip install chinese-english-lookup
```

## Usage

Via command line, script for demo purposes:

(**Please note**: script `chinese-english-lookup` contains hyphens)
```bash
chinese-english-lookup

Look up a Chinese word, type 'random', or type '!' to quit: 美好
美好 | 美好
【mei3 hao3】 beautiful; fine

Look up a Chinese word, type 'random', or type '!' to quit: random
赤贫如洗 | 赤貧如洗
【chi4 pin2 ru2 xi3】 without two nickels to rub together (idiom); impoverished
```

Importing from package:

(**Please note**: package name `chinese_english_lookup` contains underscores rather than hyphens)

```bash
>>> from chinese_english_lookup import Dictionary
>>> d = Dictionary()
>>> word_entry = d.lookup('牛油果')
>>> print(word_entry)
牛油果 | 牛油果
>>> word_entry.simp
'牛油果'
>>> word_entry.trad
'牛油果'
>>> len(word_entry.definition_entries)
1
>>> word_entry.get_definition_entries_formatted()
'【niu2 you2 guo3】 avocado (Persea americana)'
>>> word_entry.definition_entries[0].pinyin
'niu2 you2 guo3'
>>> word_entry.definition_entries[0].definitions
['avocado (Persea americana)']
```

## License
[MIT](https://choosealicense.com/licenses/mit/)