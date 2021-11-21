from typing import List
from dataclasses import dataclass
from heuristic import count_adult_slang, count_antonyms, count_sounds
from scrape import (
    extract_reviews,
    extract_news_headlines,
    extract_jokes,
    extract_jeopardy_questions,
)

JOKES = extract_jokes()
TRAINING_JOKES = JOKES[:1000]
TEST_JOKES = JOKES[1000:]

HEADLINES = extract_news_headlines()
TRAINING_HEADLINES = HEADLINES[:1000]
TEST_HEADLINES = HEADLINES[1000:]

REVIEWS = extract_reviews()
TRAINING_REVIEWS = REVIEWS[:1000]
TEST_REVIEWS = REVIEWS[1000:]

JEOPARDY = extract_jeopardy_questions()
TRAINING_JEOPARDY = JEOPARDY[:1000]
TEST_JEOPARDY = JEOPARDY[1000:]


TRAINING_CLASSIFICATIONS = []
for i in TRAINING_JOKES:
    TRAINING_CLASSIFICATIONS.append(1)
for i in TRAINING_HEADLINES:
    TRAINING_CLASSIFICATIONS.append(-1)


def create_samples(fns, documents: List[str]) -> List[List[int]]:
    out = []
    for document in documents:
        cur_sample = []
        for fn in fns:
            cur_sample.append(fn(document))
    return out
