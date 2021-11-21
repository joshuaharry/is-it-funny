#!/usr/bin/env python3
from typing import List, Any
from heuristic import count_adult_slang, count_antonyms, count_sounds
from datasets import TRAINING_JOKES, CLASSIFICATIONS, TRAINING_SETS

HEURISTICS = [
    ("slang", count_adult_slang),
    ("antonyms", count_antonyms),
    ("sounds", count_sounds),
    ("all", [count_antonyms, count_adult_slang, count_antonyms]),
]


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


print("classifications\t", CLASSIFICATIONS)
for method in HEURISTICS:
    for training in TRAINING_SETS:
        print(f"{method[0]}\t{training[0]}\t", end="")
        inputs = []
        if type(method[1]) != list:
            inputs = create_decision_params([method[1]], TRAINING_JOKES, training[1])
        else:
            inputs = create_decision_params(method[1], TRAINING_JOKES, training[1])
        print(inputs)
