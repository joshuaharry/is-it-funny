from typing import List, Any
from scrape import (
    extract_reviews,
    extract_news_headlines,
    extract_jokes,
    extract_jeopardy_questions,
)
from heuristic import count_adult_slang, count_antonyms, count_sounds

JOKES = extract_jokes()
TRAINING_JOKES = JOKES[:1000]

HEADLINES = extract_news_headlines()
TRAINING_HEADLINES = HEADLINES[:1000]

REVIEWS = extract_reviews()
TRAINING_REVIEWS = REVIEWS[:1000]

JEOPARDY = extract_jeopardy_questions()
TRAINING_JEOPARDY = JEOPARDY[:1000]

HEURISTICS = [
    count_adult_slang,
    count_antonyms,
    count_sounds,
    [count_antonyms, count_adult_slang, count_antonyms],
]
TRAINING_SETS = [TRAINING_HEADLINES, TRAINING_REVIEWS, TRAINING_JEOPARDY]

CLASSIFICATIONS = []
for i in TRAINING_JOKES:
    CLASSIFICATIONS.append(1)
for i in TRAINING_HEADLINES:
    CLASSIFICATIONS.append(-1)


def create_decision_params(
    fns: List[Any], jokes: List[str], not_jokes: List[str]
) -> List[List[int]]:
    inputs: List[List[int]] = []

    def update_input_classifications(list_var: List[str]):
        for var in list_var:
            input: List[int] = []
            for fn in fns:
                input.append(fn(var))
            inputs.append(input)

    update_input_classifications(jokes)
    update_input_classifications(not_jokes)
    return inputs


print(CLASSIFICATIONS)
for method in HEURISTICS:
    for training in TRAINING_SETS:
        inputs = []
        if type(method) != list:
            inputs = create_decision_params([method], JOKES, training)
        else:
            inputs = create_decision_params(method, JOKES, training)
        print(inputs)
