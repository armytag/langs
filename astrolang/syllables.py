import math
import random as rand

# Proto phonology
PLOSIVES = [
    "p", "t", "c", "k",
    "pʼ", "tʼ", "cʼ", "kʼ", "ʔ",
]
FRICATIVES = [
    "s", "ʃ",
    "sʼ",
]
NASALS = [
    "m", "n"
]
APPROXIMANTS = [
    "w",
    "l",
    # "j",
]
VOWELS = [
    "i", "u", "a",
    # "e", "o",
]

SYLL_STRUCTS = []
SYLL_STRUCTS += ['V'] * 0
SYLL_STRUCTS += ['CV'] * 4
SYLL_STRUCTS += ['CVC'] * 0
SYLL_STRUCTS += ['CCV'] * 0
SYLL_STRUCTS += ['CCVC'] * 0
SYLL_COUNTS = []
SYLL_COUNTS += [1] * 0
SYLL_COUNTS += [2] * 8
SYLL_COUNTS += [3] * 2
SYLL_COUNTS += [4] * 0

def flatten_matrix(matrix):
    return [item for array in matrix for item in array]

def generate_syllable(onset_shape, coda_shape):
    onset = ''
    vowel = rand.choice(VOWELS)
    coda = ''
    if len(onset_shape) == 1:
        onset = rand.choice(flatten_matrix(
            [PLOSIVES, NASALS, APPROXIMANTS, FRICATIVES,]
        ))
    if len(coda_shape) == 1:
        coda = rand.choice(flatten_matrix(
            [NASALS,]
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
    word_count = 10 * 10
    words = []
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
