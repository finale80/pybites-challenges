import pytest
import wordvalue

import operator

# scores computed using http://www.dvorkin.com/scrabscor.php
WORDS = {
    'banana' : 8,
    'mango' : 8,
    'papaya' : 13,
    'kiwi' : 11
}
BEST_WORD = max(WORDS.items(), key=operator.itemgetter(1))[0]

def test_word_score():
    for word in WORDS:
        assert wordvalue.calc_word_value(word) == WORDS[word]

def test_best_in_list():
    assert wordvalue.max_word_value(list(WORDS.keys())) == BEST_WORD
