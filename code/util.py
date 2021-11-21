from scrape import STOPWORDS
from nltk import tokenize
from typing import Set, List


def words(document: str) -> List[str]:
    """Extract all words in a particular document, preserving order."""
    return [
        word.lower()
        for word in tokenize.word_tokenize(document)
        if word not in STOPWORDS
    ]


def unique_words(document: str) -> Set[str]:
    """Extract the unique words in a particular document."""
    return set(words(document))
