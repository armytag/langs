import math
import random as rand


def flatten_matrix(matrix):
    return [item for array in matrix for item in array]


NASALS = [
    "m", "n", "ɳ", "ɲ", "ŋ",
]
STIFF_STOPS = [
    "p", "t", "ʈ", "c", "k",
]
SLACK_STOPS = [
    "b̥", "d̥", "ɖ̥", "ɟ̊", "g̊",
]
FRICATIVES = [
    "f", "s", "ç",
]
TRILLS = [
    "r",
]
APPROXIMANTS = [
    "ɻ", "j",
]
NONSLACK = flatten_matrix([NASALS, STIFF_STOPS, FRICATIVES, TRILLS, APPROXIMANTS])
VOWELS = [
    "i", "ɛ", "ɨ", "a", "u", "ɔ",
]

SYLL_STRUCTS = []
SYLL_STRUCTS += ['V'] * 1
SYLL_STRUCTS += ['CV'] * 4
SYLL_STRUCTS += ['CCV'] * 0
STRESS_STRUCTS = []
STRESS_STRUCTS += ['CVC'] * 2
STRESS_STRUCTS += ['CCVC'] * 0
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
            [NONSLACK, SLACK_STOPS]
        ))
    if len(onset_shape) == 2:
        onset = rand.choice(flatten_matrix(
            [NONSLACK, SLACK_STOPS]
        )) + rand.choice(flatten_matrix(
            [TRILLS,]
        ))
    if len(coda_shape) == 1:
        coda += rand.choice(flatten_matrix(
            [NONSLACK,]
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
        syllables = []
        word = ''
        if syll_count == 1:
            structure = rand.choice(flatten_matrix(
                [STRESS_STRUCTS, SYLL_STRUCTS,]
            ))
            syllable = get_syllable(structure)
            syllables.append(syllable)
        else:
            # Stressed syllable
            structure = rand.choice(STRESS_STRUCTS)
            syllable = get_syllable(structure)
            syllables.append(syllable)
            # Unstressed syllables
            for s in range(syll_count - 1):
                structure = rand.choice(SYLL_STRUCTS)
                syllable = get_syllable(structure)
                if rand.random() > 0.5:
                    syllables.append(syllable)
                else:
                    syllables = flatten_matrix([[syllable], syllables])
        word = ".".join(syllables)
        if len(word) > 1 and word not in words:
            words.append(word)
            print(word)
            w += 1
