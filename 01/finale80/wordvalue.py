import sys
sys.path.insert(0, '..')

from data import DICTIONARY, LETTER_SCORES

def load_words(fname):
    """Load dictionary into a list and return list"""
    with open(fname) as fin:
        return fin.readlines()

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum(LETTER_SCORES.get(c,0) for c in word.strip().upper())
    

def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if words is None:
        words = load_words(DICTIONARY)
    return max(words, key=calc_word_value)

if __name__ == "__main__":
    pass # run unittests to validate
