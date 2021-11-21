#!/usr/bin/env python3
from typing import List, Set
from nltk.corpus import wordnet as wn
import csv
from nltk.corpus import stopwords, cmudict

CM = cmudict.dict()

STOPWORDS = stopwords.words("english")


def create_adult_set() -> Set[str]:
    out: Set[str] = set()
    with open("raw/sexuality_similarity") as the_file:
        for line in the_file:
            if len(out) > 5000:
                break
            word = line.strip().lower()
            if len(wn.synsets(word)) < 4 and word not in STOPWORDS:
                out.add(word)
    return out


ADULT_WORDS = create_adult_set()


def read_csv(the_path: str, col: int) -> List[str]:
    """Open the file at THE_PATH and put column COL of each row into a list."""
    with open(the_path) as the_file:
        reader = csv.reader(the_file)
        return [row[col] for row in reader]


def read_first_col_csv(the_path: str) -> List[str]:
    """Reads the first column of every row in a CSV into a list."""
    with open(the_path) as the_file:
        reader = csv.reader(the_file)
        return [row[0] for row in reader]


def extract_jokes() -> List[str]:
    """Extract jokes from the short jokes dataset."""
    return read_csv("raw/short_joeks.csv", 1)


def extract_news_headlines() -> List[str]:
    """Extract News Headlines from the ABC dataset."""
    return read_csv("raw/abcnews-date-text.csv", 1)


def extract_jeopardy_questions() -> List[str]:
    """Extract Jeopardy questions from the Jeopardy dataset."""
    return read_csv("raw/JEOPARDY_CSV.csv", 5)


def extract_reviews() -> List[str]:
    """Extract Amazon reviews from the Amazon dataset."""
    return read_csv("raw/Reviews.csv", 8)
