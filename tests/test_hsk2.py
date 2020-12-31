import pytest

from chinese_english_lookup import HSK2


@pytest.fixture
def hsk2():
    return HSK2()


@pytest.mark.parametrize("level, expected_size", [(1, 150), (6, 2501)])
def test_word_counts(hsk2, level, expected_size):
    words_for_level = hsk2.get_words_for_level(level)
    assert len(words_for_level) == expected_size


@pytest.mark.parametrize("word, expected_level", [("爱", 1), ("追求", 5), ("做主", 6)])
def test_get_level_for_word(hsk2, word, expected_level):
    assert hsk2.get_level_for_word(word) == expected_level
