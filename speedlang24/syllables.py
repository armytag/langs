import math
import random as rand


def flatten_matrix(matrix):
    return [item for array in matrix for item in array]


NASALS = [
    "m", "n̥", "n",
    # "m", "hn", "n",
]
PLOSIVES = [
    "b", "t", "d", "k", "ʔ"
    # "b", "t", "d", "k", "ʼ"
]
FRICATIVES = [
    "s", "z", "x",
]
AFFRICATES = [
    "t͡s", "d͡z",
]
TRILLS = [
    "r̥", "r",
    # "hr", "r",
]
APPROXIMANTS = [
    "ʋ", "ɦ",
    # "v", "ɦ",
]
NONAPPROXIMANTS = flatten_matrix([NASALS, PLOSIVES, FRICATIVES, AFFRICATES, TRILLS,])
VOWELS = [
    "a", "a", "i", "u",
]
BREATHY_VOWELS = {
    "a": "a̤",
    "ə": "ə̤",
    "i": "i̤",
    "u": "ṳ",
}

SYLL_STRUCTS = []
SYLL_STRUCTS += ['V'] * 1
SYLL_STRUCTS += ['CV'] * 4
SYLL_STRUCTS += ['CCV'] * 2
STRESS_STRUCTS = []
STRESS_STRUCTS += ['CVC'] * 2
STRESS_STRUCTS += ['CCVC'] * 1
SYLL_COUNTS = []
SYLL_COUNTS += [1] * 3
SYLL_COUNTS += [2] * 2
SYLL_COUNTS += [3] * 1
SYLL_COUNTS += [4] * 0


def generate_syllable(onset_shape, coda_shape):
    onset = ''
    vowel = rand.choice(VOWELS)
    coda = ''
    if len(onset_shape) == 1:
        onset = rand.choice(flatten_matrix(
            [NONAPPROXIMANTS, APPROXIMANTS,]
        ))
    if len(onset_shape) == 2:
        onset = rand.choice(flatten_matrix(
            [NONAPPROXIMANTS,]
        )) + rand.choice(flatten_matrix(
            [APPROXIMANTS,]
        ))
    if len(coda_shape) == 1:
        coda += rand.choice(flatten_matrix(
            [NONAPPROXIMANTS, "ʋ",]
        ))
    # if len(coda_shape) == 0:
    #     if vowel != "a":
    #         vowel = "ə"
    # if onset.endswith("ɦ"):
    #     vowel = BREATHY_VOWELS[vowel]
    #     onset = onset[:-1]
    #     if len(coda_shape) == 1 and len(onset_shape) == 1:
    #         onset = "ʔ"
    syll = onset + vowel + coda
    return syll


def get_syllable(s):
    shapes = s.split('V')
    return generate_syllable(shapes[0], shapes[1])


def generate_frequencies(phonemes):
    frequencies = []
    for i, phone in enumerate(phonemes):
        frequencies.append(borodovsky_gusein_zade(i + 1, len(phonemes)))
    return frequencies


def borodovsky_gusein_zade(r, n):
    return (1 / n) * (math.log(n + 1) - math.log(r))


if __name__ == "__main__":
    word_count = 10 * 2
    words = []
    w = 0
    while w < word_count:
        syll_count = rand.choice(SYLL_COUNTS)
        syllables = []
        word = ''
        if syll_count == 1:
            structure = rand.choice(flatten_matrix(
                [STRESS_STRUCTS, SYLL_STRUCTS,]
            ))
            syllable = get_syllable(structure)
            syllables.append(syllable)
        else:
            # Unstressed syllables
            for s in range(syll_count - 1):
                structure = rand.choice(SYLL_STRUCTS)
                syllable = get_syllable(structure)
                syllables.append(syllable)
            # Stressed syllable
            structure = rand.choice(STRESS_STRUCTS)
            syllable = get_syllable(structure)
            syllables.append(syllable)
        word = "".join(syllables)
        if len(word) > 1 and word not in words:
            words.append(word)
            print(word)
            w += 1
