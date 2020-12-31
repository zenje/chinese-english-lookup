import pytest

from chinese_english_lookup import HSK3
from chinese_english_lookup import HSK3Category as Category


@pytest.fixture
def hsk3():
    return HSK3()


@pytest.mark.parametrize(
    "get_words_method_to_call, expected_word_count",
    [
        ("get_entry", 2226),
        ("get_intermediate", 3167),
        ("get_advanced", 4093),
        ("get_supplemental", 1409),
    ],
)
def test_word_counts(hsk3, get_words_method_to_call, expected_word_count):
    # invoke method by name
    words = getattr(hsk3, get_words_method_to_call)()
    assert len(words) == expected_word_count


@pytest.mark.parametrize(
    "word, expected_category",
    [
        ("天空", Category.ENTRY),
        ("巧克力", Category.INTERMEDIATE),
        ("灯笼", Category.ADVANCED),
        ("粽子", Category.SUPPLEMENTAL),
    ],
)
def test_get_category_for_word(hsk3, word, expected_category):
    assert hsk3.get_category_for_word(word) == expected_category.title
