import numpy as np


def cosine_similarity(v1, v2):
    "Return the cosine similarity of two vectors."
    return (np.dot(v1, v2)) / (np.linalg.norm(v1) * np.linalg.norm(v2))


def get_glove_embeddings():
    "Map strings to word embedding vectors."
    out = dict()
    with open("raw/glove.840B.300d.txt") as the_file:
        for line in the_file:
            key, *vec = line.split(" ")
            out[key] = np.array([float(x) for x in vec])
    return out


def rank_similarities():
    "Rank the words in the GloVe corpus by their cosine similarity to the word sexuality."
    embeddings = get_glove_embeddings()
    words = [word for word in embeddings]
    sexuality = embeddings["sexuality"]
    words.sort(key=lambda x: cosine_similarity(sexuality, embeddings[x]), reverse=True)
    return words


similarities = rank_similarities()
for word in similarities:
    print(word)
