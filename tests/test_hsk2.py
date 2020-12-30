import pytest

from chinese_english_lookup import HSK2

hsk2 = HSK2()


def test_word_counts():
    level_1 = hsk2.get_words_for_level(1)
    level_6 = hsk2.get_words_for_level(6)

    assert len(level_1) == 150
    assert len(level_6) == 2501


def test_get_level_for_word():
    assert hsk2.get_level_for_word("爱") == 1
    assert hsk2.get_level_for_word("追求") == 5
    assert hsk2.get_level_for_word("做主") == 6
