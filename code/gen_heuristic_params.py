from typing import List, Any
from dataclasses import dataclass
from heuristic import count_adult_slang, count_antonyms, count_sounds

TRAINING_SIZE = 1000

TESTING_SIZE = 15000


@dataclass
class Sample:
    samples: List[List[int]]
    classifications: List[int]


def create_sample(
    methods: List[Any], positives: List[str], negatives: List[str]
) -> Sample:
    samples = []
    classifications = []

    def update_samples(documents: List[str], num: int):
        nonlocal samples
        nonlocal classifications
        nonlocal methods
        for document in documents:
            classifications.append(num)
            add = []
            for fn in methods:
                add.append(fn(document))
            samples.append(add)

    update_samples(positives, 1)
    update_samples(negatives, -1)
    return Sample(samples, classifications)


@dataclass
class Heuristic:
    name: str
    method: List[Any]
    train: Sample
    test: Sample

    def __init__(
        self, name: str, fns: List[Any], positives: List[str], negatives: List[str]
    ):
        self.name = name
        training_positives = positives[:TRAINING_SIZE]
        training_negatives = negatives[:TRAINING_SIZE]
        self.train = create_sample(fns, training_positives, training_negatives)
        max_positives = positives[TRAINING_SIZE:]
        max_negatives = negatives[TRAINING_SIZE:]
        testing_positives = max_positives[:TESTING_SIZE]
        testing_negatives = max_negatives[:TESTING_SIZE]
        self.test = create_sample(fns, testing_positives, testing_negatives)
        self.method = fns


@dataclass
class Dataset:
    name: str
    slang: Heuristic
    antonyms: Heuristic
    sounds: Heuristic
    all: Heuristic

    def __init__(self, name: str, positives: List[str], negatives: List[str]):
        self.name = name
        self.slang = Heuristic(
            f"{name} slang", [count_adult_slang], positives, negatives
        )
        self.sounds = Heuristic(f"{name} sounds", [count_sounds], positives, negatives)
        self.antonyms = Heuristic(
            f"{name} antonyms", [count_antonyms], positives, negatives
        )
        self.all = Heuristic(
            f"{name} all",
            [count_adult_slang, count_sounds, count_antonyms],
            positives,
            negatives,
        )
