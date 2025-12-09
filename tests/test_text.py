import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n


@pytest.mark.parametrize(
    ("src", "exp"),
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("Hello  WORLD", "hello world"),
        ("  doble   espacios ", "doble espacios"),
        ("", ""),
    ],
)
def test_normalize(src, exp):
    assert normalize(src) == exp


def test_tokenize_and_count_freq():
    txt = "a a b c a"
    tokens = tokenize(txt)
    assert tokens == ["a", "a", "b", "c", "a"]
    freq = count_freq(tokens)
    assert freq == {"a": 3, "b": 1, "c": 1}


def test_top_n_tie_breaker():
    freq = {"apple": 2, "banana": 2, "cherry": 1}
    assert top_n(freq, 2) == [("apple", 2), ("banana", 2)]
