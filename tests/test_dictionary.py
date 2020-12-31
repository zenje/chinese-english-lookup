import pytest

from chinese_english_lookup import Dictionary


@pytest.fixture
def dictionary():
    return Dictionary()


@pytest.mark.parametrize(
    "word_to_find, expected_simp, expected_trad, expected_definitions",
    [
        ("甜蜜", "甜蜜", "甜蜜", "【tian2 mi4】 sweet; happy"),
        ("糊涂", "糊涂", "糊塗", "【hu2 tu5】 muddled; silly; confused"),
        (
            "好",
            "好",
            "好",
            "1) 【hao3】 good; well; proper; good to; easy to; very; so; (suffix indicating completion or readiness); (of two people) close; on intimate terms; (after a personal pronoun) hello\n2) 【hao4】 to be fond of; to have a tendency to; to be prone to",
        ),
    ],
)
def test_assert_word_entry(
    dictionary, word_to_find, expected_simp, expected_trad, expected_definitions
):
    found_word = dictionary.lookup(word_to_find)

    assert found_word is not None
    assert found_word.simp == expected_simp
    assert found_word.trad == expected_trad
    assert found_word.get_definition_entries_formatted() == expected_definitions
