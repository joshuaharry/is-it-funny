#!/usr/bin/env python3
from dataclasses import dataclass
from typing import List
from sklearn import tree
from datasets import DATA_MAP


@dataclass
class ModelParameters:
    heuristic: str
    training_set: str
    samples: List[float]
    features: List[int]


def extract_model_parameters() -> List[ModelParameters]:
    models: List[ModelParameters] = []
    FEATURES = []
    with open("raw/computed_params") as param_file:
        for line in param_file:
            elems = [el.strip() for el in line.split("\t")]
            if elems[0] == "classifications":
                FEATURES = eval(elems[1])
                continue
            heuristic = elems[0]
            training_set = elems[1]
            training_parameters = eval(elems[2])
            model = ModelParameters(
                heuristic, training_set, training_parameters, FEATURES
            )
            models.append(model)
    return models


# TODO: Write a function that iterates over the model parameters and then
# evaluates the performance on the test data. Once we get this working
# for the heuristic decision trees, replicate with Naive Bayes and the SMV
# vectors.
