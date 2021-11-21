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

TRAINING_SETS = [
    ("headlines", TRAINING_HEADLINES),
    ("reviews", TRAINING_REVIEWS),
    ("jeopardy", TRAINING_JEOPARDY),
]

DATA_MAP = {
    "headlines": {"test": TEST_HEADLINES, "training": TRAINING_HEADLINES},
    "reviews": {"test": TEST_REVIEWS, "training": TRAINING_REVIEWS},
    "jeopardy": {"test": TEST_JEOPARDY, "training": TRAINING_JEOPARDY},
}

CLASSIFICATIONS = []
for i in TRAINING_JOKES:
    CLASSIFICATIONS.append(1)
for i in TRAINING_HEADLINES:
    CLASSIFICATIONS.append(-1)
