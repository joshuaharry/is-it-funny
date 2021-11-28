from typing import List, Any
from dataclasses import dataclass
from heuristic import count_adult_slang, count_antonyms, count_sounds

TRAINING_SIZE = 1000

TESTING_SIZE = 15000


# A sample contains a list of vectors (lists), in which the coordinates
# of the vector correspond to some embedding based on one of the heuristics.
@dataclass
class Sample:
    samples: List[List[int]]
    classifications: List[int]


# Create a Sample using a list of methods, a list of positive examples,
# and a list of negative examples.
#
# Every element of the Methods list is a *function* that we run to populate
# the embedding vector with some heuristic information. We iterate through
# the functions in `methods` in order and place the results into a separate
# list which becomes the embedding vector for the decision tree classifier.
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


# A Heuristic includes training vectors with embedding for a heuristic and
# test vectors with embedding for a heuristic.
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


# A dataset contains embeds a Heuristic object for each of the four
# Heuristics we want to examine.
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
