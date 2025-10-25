import math
import random as rand

NASALS = [
    "m", "n", "ɲ", "ŋ",
]
PLOSIVES = [
    "p", "t", "c", "k",
    "b", "d", "ɟ", "g",
]
FRICATIVES = [
    "f", "s", "ʃ", "x",
]
APPROXIMANTS = [
    "w", "j",
]
LIQUIDS = [
    "l", "r",
]
VOWELS = [
    "i", "ə", "u",
    "ɛ", "a", "ɔ",
]

SYLL_STRUCTS = []
SYLL_STRUCTS += ['V'] * 0
SYLL_STRUCTS += ['VC'] * 0
SYLL_STRUCTS += ['CV'] * 9
SYLL_STRUCTS += ['CV:'] * 1
SYLL_STRUCTS += ['CVC'] * 2
SYLL_STRUCTS += ['CCV'] * 0
SYLL_STRUCTS += ['CCVC'] * 0
SYLL_COUNTS = []
SYLL_COUNTS += [1] * 2
SYLL_COUNTS += [2] * 6
SYLL_COUNTS += [3] * 0
SYLL_COUNTS += [4] * 0


def flatten_matrix(matrix):
    return [item for array in matrix for item in array]


def generate_syllable(onset_shape: str, coda_shape: str):
    onset = ''
    vowel = rand.choice(VOWELS)
    coda = ''
    if len(onset_shape) == 1:
        onset = rand.choice(flatten_matrix(
            [NASALS, PLOSIVES, FRICATIVES, APPROXIMANTS, LIQUIDS,]
        ))
    if coda_shape == ':':
        coda = "ː"
    elif len(coda_shape) == 1:
        coda = rand.choice(flatten_matrix(
            ["m", "n", "ŋ", LIQUIDS,]
        ))
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
    # phonemes = NASALS # + FRICATIVES + PLOSIVES + RHOTICS
    # print(phonemes)
    # print(generate_frequencies(phonemes))
    word_count = 20
    words = []
    w = 0
    while w < word_count:
        syll_count = rand.choice(SYLL_COUNTS)
        syllables = []
        word = ''
        for s in range(syll_count):
            structure = rand.choice(SYLL_STRUCTS)
            while s == 0 and structure == "CV" and syll_count >= 1:
                structure = rand.choice(SYLL_STRUCTS)
            syllables.append(get_syllable(structure))
        word = ".".join(syllables)
        if len(word) > 1 and word not in words:
            words.append(word)
            print(word)
            w += 1
