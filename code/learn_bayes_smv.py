print("Beginning imports...")
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import SVC
from typing import List
from scrape import (
    extract_jeopardy_questions,
    extract_jokes,
    extract_news_headlines,
    extract_reviews,
)

print("Code imported.")


def verbose_load(name: str, fn) -> List[str]:
    print(f"Loading {name} from csv...")
    answer = fn()
    print(f"{name} loaded.")
    return answer


JOKES = verbose_load("jokes", extract_jokes)
HEADLINES = verbose_load("headlines", extract_news_headlines)
REVIEWS = verbose_load("reviews", extract_reviews)
JEOPARDY = verbose_load("jeopardy", extract_jeopardy_questions)

TRAINING_SIZE = 1000

TEST_SIZE = 15000


def evaluate(name: str, all_positives: List[str], all_negatives: List[str]):
    bayes = MultinomialNB()
    vectorizer = TfidfVectorizer()
    svm = SVC()
    positives = all_positives[0 : TRAINING_SIZE + TEST_SIZE]
    negatives = all_negatives[0 : TRAINING_SIZE + TEST_SIZE]

    print(f"Vectorizing {name} training_data...")
    vectorizer.fit([*positives, *negatives])
    training_classes = [
        *[1 for _ in range(TRAINING_SIZE)],
        *[-1 for _ in range(TRAINING_SIZE)],
    ]
    testing_classes = [*[1 for _ in range(TEST_SIZE)], *[-1 for _ in range(TEST_SIZE)]]
    training_vec = vectorizer.transform(
        positives[:TRAINING_SIZE] + negatives[:TRAINING_SIZE]
    )
    testing_vec = vectorizer.transform(positives[:TEST_SIZE] + negatives[:TEST_SIZE])

    print("Fitting naive bayes...")
    bayes.fit(training_vec, training_classes)
    print("Fitting SVM...")
    svm.fit(training_vec, training_classes)

    print("Scoring naive bayes...")
    bayes_score = bayes.score(testing_vec, testing_classes)
    print(f"Bayes score: {bayes_score}")

    print("Scoring SVM...")
    svm_score = svm.score(testing_vec, testing_classes)
    print(f"SVM score: {svm_score}")


evaluate("headlines", JOKES, HEADLINES)
evaluate("reviews", JOKES, REVIEWS)
evaluate("jeopardy", JOKES, JEOPARDY)
