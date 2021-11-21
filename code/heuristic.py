#!/usr/bin/env python3
from scrape import CM, ADULT_WORDS
from nltk.corpus import wordnet as wn
from typing import Set
from util import words, unique_words


def unique_antonyms(word: str) -> Set[str]:
    """Find all antonyms associated with a word."""
    out: Set[str] = set()
    for synset in wn.synsets(word):
        for synonym in synset.lemmas():
            antonyms = synonym.antonyms()
            if antonyms:
                for antonym in antonyms:
                    out.add(antonym.name())
    return out


def count_sounds(document: str) -> int:
    """Count the amount of humorous alliteration and rhymes in a document."""
    count = 0
    doc_words = words(document)
    for index, word in enumerate(doc_words[1:], start=1):
        prev_word = doc_words[index - 1]
        if word in CM and prev_word in CM:
            cur_entry = CM[word][0]
            prev_entry = CM[prev_word][0]
            # Alliteration
            if cur_entry[0] == prev_entry[0]:
                count += 1
            # Rhymes
            if cur_entry[-1] == prev_entry[-1]:
                count += 1
    return count


def count_adult_slang(document: str) -> int:
    """Count the number of sexual words in a document."""
    count = 0
    for word in unique_words(document):
        if word in ADULT_WORDS:
            count += 1
    return count


def count_antonyms(document: str) -> int:
    """Count the number of unique antonyms in a document."""
    count = 0
    seen: Set[str] = set()
    words = unique_words(document)
    for word in words:
        antonyms = unique_antonyms(word)
        for antonym in antonyms:
            if antonym in words and antonym not in seen:
                seen.add(word)
                seen.add(antonym)
                count += 1
    return count
