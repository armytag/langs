import math
import random as rand

PLOSIVES = [
    "p", "t̪", "ts", "tɬ", "tʃ", "k",
]
FRICATIVES = [
    # "s", "ʃ", "x",
]
NASALS = [
    "m", "n", "ɲ",
]
APPROXIMANTS = [
    "r", "l", "ʟ",
]
VOWELS = [
    "a", "a", "ə", "ə",
    # "ja", "wa", "jə", "wə",
]

SYLL_STRUCTS = []
SYLL_STRUCTS += ['VC'] * 0
SYLL_STRUCTS += ['CV'] * 3
SYLL_STRUCTS += ['CVC'] * 1
SYLL_STRUCTS += ['CCV'] * 0
SYLL_STRUCTS += ['CCVC'] * 0
SYLL_COUNTS = []
SYLL_COUNTS += [1] * 3
SYLL_COUNTS += [2] * 4
SYLL_COUNTS += [3] * 2
SYLL_COUNTS += [4] * 1


def flatten_matrix(matrix):
    return [item for array in matrix for item in array]


def generate_syllable(onset_shape, coda_shape, syll_num):
    onset = ""
    vowel = ""
    coda = ""
    chance = rand.random()
    if len(onset_shape) > 0:
        onset = rand.choice(flatten_matrix(
            [PLOSIVES, NASALS, FRICATIVES, APPROXIMANTS]
        ))
        if chance < (1/4):
            onset += "w"
        elif chance < (2/4):
            onset += "j"
    vowel = rand.choice(VOWELS)
    if len(coda_shape) > 0:
        coda = rand.choice(flatten_matrix(
            [NASALS, APPROXIMANTS]
        ))
    # print("\t", onset, vowel, tone, end=" ")
    # print("→", onset, vowel)
    syll = onset + vowel + coda
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
    word_count = 10 * 100
    words = []
    w = 0
    attempts = 0
    while w < word_count and attempts < 100000:
        syll_count = rand.choice(SYLL_COUNTS)
        syllables = []
        word = ''
        for s in range(syll_count):
            structure = rand.choice(SYLL_STRUCTS)
            if s == 0:
                structure = rand.choice(["V", "V", "VC",])
            syllable = get_syllable(structure, s)
            syllables.append(syllable)
        word = "".join(syllables)
        attempts += 1
        if len(word) > 1 and word not in words:
            words.append(word)
            print(word)
            w += 1
