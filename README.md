# chinese-english-lookup

A simple Python package for Chinese-to-English word definition retrieval. Definitions sourced from Chinese-English dictionary [CC-CEDICT](https://www.mdbg.net/chinese/dictionary?page=cc-cedict).

Also includes utility for HSK3.0 (post-2020) and HSK2.0 (2010-2020).

## Installation

```bash
pip install chinese-english-lookup
```

## Usage

### Running CLI demo for Dictionary

Run command `chinese-english-lookup`:

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

### Using Dictionary utility

(**Please note**: package name `chinese_english_lookup` contains underscores rather than hyphens)

```python3
>>> from chinese_english_lookup import Dictionary
>>> d = Dictionary()
>>> word_entry = d.lookup('牛油果')
>>> print(word_entry)
牛油果 | 牛油果
【niu2 you2 guo3】 avocado (Persea americana)
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

### Using HSK3 utility

```python3
>>> from chinese_english_lookup import HSK3
>>> hsk3 = HSK3()
>>> intermediate_words = hsk3.get_intermediate()
>>> len(intermediate_words)
3167
>>> for word in intermediate_words:
...     print(str(word))    # output omitted

>>> print(intermediate_words[0])
阿姨 | 阿姨
【a1 yi2】 maternal aunt; step-mother; childcare worker; nursemaid; woman of similar age to one's parents (term of address used by child); CL:個|个[ge4]

>>> hsk3.get_category_for_word('醉')
'中级 - Intermediate Level'
```

### Using HSK2 utility

```python3
>>> from chinese_english_lookup import HSK2
>>> hsk2 = HSK2()
>>> level_4_words = hsk2.get_words_for_level(4)
>>> len(level_4_words)
598
>>> for word in level_4_words:
...     print(str(word))    # output omitted

>>> print(level_for_words[0])
爱情 | 愛情
【ai4 qing2】 romance; love (romantic); CL:個|个[ge4],份[fen4]

>>> hsk2.get_level_for_word('梦')
4
```

## License
[MIT](https://choosealicense.com/licenses/mit/)