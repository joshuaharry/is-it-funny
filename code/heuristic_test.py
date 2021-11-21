from heuristic import count_adult_slang, count_antonyms, count_sounds


def test_slang_ex1():
    assert (
        count_adult_slang(
            "The coitus was so good that even the neighbors had a cigarette."
        )
        == 1
    )


def test_slang_ex2():
    assert (
        count_adult_slang("Artificial Insemination: procreation without recreation.")
        == 2
    )


def test_antonyms():
    assert count_antonyms("good evil happy unhappy") == 2


def test_rhymes():
    assert count_sounds("cat mat") == 1


def test_alliteration():
    assert count_sounds("sally sells sea shells by the sea shore") == 2


def test_rhyme_alliteration():
    assert count_sounds("potato potato") == 2
