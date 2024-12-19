from twttr import shorten


def test_word():
    assert shorten("twitter") == "twttr"


def test_ignore_case():
    assert shorten("TwItter") == "Twttr"


def test_ignore_nums():
    assert shorten("CSI50") == "CS50"


def test_ignore_punc():
    assert shorten("CS50!") == "CS50!"
