import math
import random as rand

NASALS = [
    "m", "n"
]
PLOSIVES = [
    "p", "t", "d", "k",
]
FRICATIVES = [
    "f", "s", "z", "x",
]
APPROXIMANTS = [
    "w", "r", "l", 
]
VOWELS = [
    "i", "e", "a", "o", "u",
]
SYLL_STRUCTS = []
SYLL_STRUCTS += ['V'] * 2
SYLL_STRUCTS += ['CV'] * 3
SYLL_STRUCTS += ['CVC'] * 3
SYLL_STRUCTS += ['CCV'] * 2
SYLL_STRUCTS += ['CCVC'] * 2
SYLL_COUNTS = []
SYLL_COUNTS += [1] * 1
SYLL_COUNTS += [2] * 1
SYLL_COUNTS += [3] * 1
SYLL_COUNTS += [4] * 1

def generate_syllable(onset_shape, coda_shape):
    onset = ''
    vowel = rand.choice(VOWELS)
    coda = ''
    if len(onset_shape) == 2:
        shape = rand.choice([
            [PLOSIVES, APPROXIMANTS],
            [PLOSIVES, FRICATIVES],
            [FRICATIVES, APPROXIMANTS],
        ])
        for part in shape:
            onset += rand.choice(part)
    elif len(onset_shape) == 1:
        onset = rand.choice(rand.choice([
            PLOSIVES, NASALS, FRICATIVES, APPROXIMANTS
        ]))
    if len(coda_shape) == 1:
        coda = rand.choice(rand.choice([
            NASALS, FRICATIVES, APPROXIMANTS
        ]))
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
    # phonemes = NASALS # + FRICATIVES + PLOSIVES + APPROXIMANTS
    # print(phonemes)
    # print(generate_frequencies(phonemes))
    word_count = 20
    words = []
    for idx in range(word_count):
        syll_count = rand.choice(SYLL_COUNTS)
        word = ''
        for idx in range(syll_count):
            structure = rand.choice(SYLL_STRUCTS)
            syllable = get_syllable(structure)
            word += syllable
        words.append(word)
        print(word)
