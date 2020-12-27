import pytest

from chinese_english_lookup import HSK3
from chinese_english_lookup import HSK3Category as Category

hsk3 = HSK3()


def test_word_counts():
    entry_words = hsk3.get_entry()
    intermediate_words = hsk3.get_intermediate()
    advanced_words = hsk3.get_advanced()
    supplemental_words = hsk3.get_supplemental()

    assert len(entry_words) == 2226
    assert len(intermediate_words) == 3167
    assert len(advanced_words) == 4093
    assert len(supplemental_words) == 1409


def test_get_category_for_word():
    assert hsk3.get_category_for_word("天空") == Category.ENTRY.title
    assert hsk3.get_category_for_word("巧克力") == Category.INTERMEDIATE.title
    assert hsk3.get_category_for_word("灯笼") == Category.ADVANCED.title
    assert hsk3.get_category_for_word("粽子") == Category.SUPPLEMENTAL.title
