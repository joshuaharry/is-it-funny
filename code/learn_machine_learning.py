print("Starting imports...")
from scrape import (
    extract_jokes,
    extract_jeopardy_questions,
    extract_news_headlines,
    extract_reviews,
)
from sklearn import naive_bayes, svm

TRAINING_SIZE = 1000

print("Extracting jokes from CSV...")
JOKES = extract_jokes()

print("Extracting jeopardy from CSV...")
JEOPARDY = extract_jeopardy_questions()

print("Extracting news from CSV...")
NEWS = extract_news_headlines()

print("Extracting reviews from CSV...")
REVIEWS = extract_reviews()
