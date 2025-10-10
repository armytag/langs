import math
import random as rand

IMPLOSIVES = [
]
PLOSIVES = [
    "p", "t", "k",
    "b", "d", "g",
]
FRICATIVES = [
    "s", "x",
]
NASALS = [
    "m", "n",
]
APPROXIMANTS = [
    "w", "l", "j",
]
TRILL = [
    "r",
]
VOWELS = [
    "a", "i", "u",
    "a", "i", "u",
    "aː", "iː", "uː",
]

SYLL_STRUCTS = []
SYLL_STRUCTS += ['VC'] * 0
SYLL_STRUCTS += ['CV'] * 3
SYLL_STRUCTS += ['CVC'] * 0
SYLL_STRUCTS += ['CCV'] * 0
SYLL_STRUCTS += ['CCVC'] * 0
SYLL_COUNTS = []
SYLL_COUNTS += [1] * 1
SYLL_COUNTS += [2] * 2
SYLL_COUNTS += [3] * 3
SYLL_COUNTS += [4] * 1


def flatten_matrix(matrix):
    return [item for array in matrix for item in array]


def generate_syllable(onset_shape, coda_shape, syll_num):
    onset = rand.choice(flatten_matrix(
        [PLOSIVES, NASALS, TRILL, FRICATIVES,]
    ))
    vowel = rand.choice(VOWELS)
    # print("\t", onset, vowel, tone, end=" ")
    # print("→", onset, vowel)
    syll = onset + vowel
    return syll


def get_syllable(s, syll_num):
    shapes = s.split('V')
    return generate_syllable(shapes[0], shapes[1], syll_num)


def generate_frequencies(phonemes):
    frequencies = []
    for i, phone in enumerate(phonemes):
        frequencies.append(borodovsky_gusein_zade(i + 1, len(phonemes)))
    return frequencies


def borodovsky_gusein_zade(r, n):
    return (1 / n) * (math.log(n + 1) - math.log(r))


if __name__ == "__main__":
    # phonemes = NASALS # + FRICATIVES + PLOSIVES + RHOTICS
    # print(phonemes)
    # print(generate_frequencies(phonemes))
    word_count = 10 * 50
    words = []
    w = 0
    attempts = 0
    while w < word_count and attempts < 100000:
        syll_count = rand.choice(SYLL_COUNTS)
        syllables = []
        word = ''
        for s in range(syll_count):
            structure = rand.choice(SYLL_STRUCTS)
            syllable = get_syllable(structure, s)
            syllables.append(syllable)
        word = "".join(syllables)
        attempts += 1
        if len(word) > 1 and word not in words:
            words.append(word)
            print(word)
            w += 1
