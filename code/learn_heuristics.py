print("Installing imports...")
from sklearn.tree import DecisionTreeClassifier
from typing import List
from gen_heuristic_params import Dataset
from scrape import (
    extract_jokes,
    extract_jeopardy_questions,
    extract_news_headlines,
    extract_reviews,
)

print("Extracting jokes from CSV...")
JOKES = extract_jokes()

print("Extracting jeopardy from CSV...")
JEOPARDY = extract_jeopardy_questions()

print("Extracting news from CSV...")
NEWS = extract_news_headlines()

print("Extracting reviews from CSV...")
REVIEWS = extract_reviews()

# Create a tree with the different vector embeddings that we would
# like to use. See ./gen_heuristic_params.py to learn how the tree
# gets constructed.
def create_dataset(name: str, negatives: List[str]) -> Dataset:
    return Dataset(name, JOKES, negatives)


# Run a decision tree classifier using different vector embeddings based
# on the heuristics we're looking for. See the file ./heuristic.py for
# more information about how we compute each of the embeddings.
def evaluate(name: str, negatives: List[str]):
    print(f"Creating dataset for {name}...")
    dataset = create_dataset(name, negatives)

    print(f"Evaluating {name} slang...")
    slang_classifier = DecisionTreeClassifier()
    slang_classifier.fit(
        dataset.slang.train.samples, dataset.slang.train.classifications
    )
    score = slang_classifier.score(
        dataset.slang.test.samples, dataset.slang.test.classifications
    )
    print(f"Score: {score}")

    print(f"Evaluating {name} sounds...")
    sounds_classifier = DecisionTreeClassifier()
    sounds_classifier.fit(
        dataset.sounds.train.samples, dataset.sounds.train.classifications
    )
    score = sounds_classifier.score(
        dataset.sounds.test.samples, dataset.sounds.test.classifications
    )
    print(f"Score: {score}")

    print(f"Evaluating {name} antonyns...")
    antonym_classifier = DecisionTreeClassifier()
    antonym_classifier.fit(
        dataset.antonyms.train.samples, dataset.antonyms.train.classifications
    )
    score = antonym_classifier.score(
        dataset.antonyms.test.samples, dataset.antonyms.test.classifications
    )
    print(f"Score: {score}")

    print(f"Evaluating {name} all...")
    all_classifier = DecisionTreeClassifier()
    all_classifier.fit(dataset.all.train.samples, dataset.all.train.classifications)
    score = all_classifier.score(
        dataset.all.test.samples, dataset.all.test.classifications
    )
    print(f"Score: {score}")


evaluate("reviews", REVIEWS)
evaluate("jeopardy", JEOPARDY)
evaluate("news", NEWS)
