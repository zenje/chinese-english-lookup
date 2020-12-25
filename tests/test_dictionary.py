import pytest

from chinese_english_lookup import Dictionary

dictionary = Dictionary()


def assert_word_entry(word_to_find, expected_word, expected_definitions):
    found_word = dictionary.lookup(word_to_find)

    assert found_word is not None
    assert str(found_word) == expected_word
    assert found_word.definitions == expected_definitions


def test_case1():
    assert_word_entry("甜蜜", "甜蜜 | 甜蜜【tian2 mi4】", "sweet; happy")


def test_case2():
    assert_word_entry(
        "不三不四",
        "不三不四 | 不三不四【bu4 san1 bu4 si4】",
        "dubious; shady; neither one thing nor the other; neither fish nor fowl; nondescript",
    )


def test_case3():
    assert_word_entry("糊涂", "糊涂 | 糊塗【hu2 tu5】", "muddled; silly; confused")
