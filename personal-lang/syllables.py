import math
import random as rand

NASALS = [
    "m", "n", "ɳ",
]
PLOSIVES = [
    "p", "b", "t", "d", "ʈ", "ɖ", "k",
]
AFFRICATES = [
    "ts", "ʈʂ",
]
FRICATIVES = [
    "f", "s", "ʂ", "x", "χ", "h",
]
APPROXIMANTS = [
    "w", "ʟ",
]
RHOTICS = [
    "ɾ", "ɽ",
]
VOWELS = [
    "i", "e", "ɛ", "u", "o", "ɔ", "a",
]
SYLL_STRUCTS = []
SYLL_STRUCTS += ['V'] * 1
SYLL_STRUCTS += ['CV'] * 4
SYLL_STRUCTS += ['CVC'] * 0
SYLL_STRUCTS += ['CCV'] * 0
SYLL_STRUCTS += ['CCVC'] * 0
SYLL_COUNTS = []
SYLL_COUNTS += [1] * 1
SYLL_COUNTS += [2] * 3
SYLL_COUNTS += [3] * 2
SYLL_COUNTS += [4] * 2

def flatten_matrix(matrix):
    return [item for array in matrix for item in array]

def generate_syllable(onset_shape, coda_shape):
    onset = ''
    vowel = rand.choice(VOWELS)
    coda = ''
    if len(onset_shape) == 1:
        onset = rand.choice(flatten_matrix(
            [PLOSIVES, NASALS, AFFRICATES, FRICATIVES, APPROXIMANTS, RHOTICS]
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
    word_count = 10 * 2
    words = []
    # for idx in range(word_count):
    w = 0
    while w < word_count:
        syll_count = rand.choice(SYLL_COUNTS)
        word = ''
        for s in range(syll_count):
            structure = rand.choice(SYLL_STRUCTS)
            syllable = get_syllable(structure)
            word += syllable
        if len(word) > 1 and word not in words:
            words.append(word)
            print(word)
            w += 1
