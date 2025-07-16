import math
import random as rand

# Proto phonology
NASALS = [
    "m", "n",
]
PLOSIVES = [
    "p", "pʰ", "b",
    "t", "tʰ", "d",
    "t͡ɕ", "d͡ʑ",
    "k", "kʰ", "ʔ",
]
FRICATIVES = [
    "s", "z", "ʃ",
    "f", "v", "x", "h",
]
APPROXIMANTS = [
    "l", "j", "w",
]
TAP = [
    "ɾ",
]
VOWELS = [
    "i", "u", "e", "o", "ɛ", "ɔ", "a",
    "i", "u", "e", "o", "ɛ", "ɔ", "a",
    "iː", "uː", "oː", "aː",
]

SYLL_STRUCTS = []
SYLL_STRUCTS += ['V'] * 8
SYLL_STRUCTS += ['CV'] * 80
SYLL_STRUCTS += ['CCV'] * 8
SYLL_STRUCTS += ['VC'] * 4
SYLL_STRUCTS += ['CVC'] * 40
SYLL_STRUCTS += ['CCVC'] * 4
SYLL_STRUCTS += ['VCC'] * 2
SYLL_STRUCTS += ['CVCC'] * 2
SYLL_STRUCTS += ['CCVCC'] * 2
SYLL_COUNTS = []
SYLL_COUNTS += [1] * 3
SYLL_COUNTS += [2] * 6
SYLL_COUNTS += [3] * 1
SYLL_COUNTS += [4] * 0

def flatten_matrix(matrix):
    return [item for array in matrix for item in array]

def generate_syllable(onset_shape, coda_shape):
    onset = ''
    vowel = rand.choice(VOWELS)
    coda = ''
    if len(onset_shape) >= 1:
        onset = rand.choice(flatten_matrix(
            [PLOSIVES, NASALS, APPROXIMANTS, FRICATIVES, TAP]
        ))
    if len(onset_shape) >= 2:
        onset = onset + rand.choice(flatten_matrix(
            [APPROXIMANTS, TAP]
        ))
    if len(coda_shape) >= 2:
        coda = rand.choice(flatten_matrix(
            [NASALS, "l", "s",]
        ))
    if len(coda_shape) >= 1:
        coda = rand.choice(flatten_matrix(
            [PLOSIVES, NASALS, APPROXIMANTS, FRICATIVES, TAP]
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
    word_count = 200 * 10
    words = []
    w = 0
    while w < word_count:
        syll_count = rand.choice(SYLL_COUNTS)
        word = ''
        for i, s in enumerate(range(syll_count)):
            structure = rand.choice(SYLL_STRUCTS)
            syllable = get_syllable(structure)
            word += syllable
            if i < syll_count - 1:
                word += "."
        if len(word) > 1 and word not in words:
            words.append(word)
            print(word)
            w += 1
