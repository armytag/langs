import math
import random as rand

IMPLOSIVES = [
    "ɓ", "ɗ",
]
PLOSIVES = [
    "p", "t", "ts", "k", "ʔ",
    "pʷ", "tʷ", "tsʷ", "kʷ", "ʔʷ",
]
FRICATIVES = [
    "θ", "s", "ʃ", "h",
    "θʷ", "sʷ", "ʃʷ", "hʷ",
]
SONORANTS = [
    "m", "n", "l", "j",
    "mʷ", "nʷ", "lʷ", "w",
]
VOWELS = [
    "e", "iː", "a", "aː",
]
TONES = [
    # "L", "H",
    "̀", "́",
]

SYLL_STRUCTS = []
SYLL_STRUCTS += ['VC'] * 0
SYLL_STRUCTS += ['CV'] * 3
SYLL_STRUCTS += ['CVC'] * 0
SYLL_STRUCTS += ['CCV'] * 0
SYLL_STRUCTS += ['CCVC'] * 0
SYLL_COUNTS = []
SYLL_COUNTS += [1] * 1
SYLL_COUNTS += [2] * 0
SYLL_COUNTS += [3] * 0
SYLL_COUNTS += [4] * 0


def flatten_matrix(matrix):
    return [item for array in matrix for item in array]


def generate_syllable(onset_shape, coda_shape, syll_num):
    onset = rand.choice(flatten_matrix(
        [IMPLOSIVES, PLOSIVES, SONORANTS, FRICATIVES,]
    ))
    vowel = rand.choice(VOWELS)
    tone = rand.choice(TONES)
    # print("\t", onset, vowel, tone, end=" ")
    if onset == "w" or "ʷ" in onset:
        if vowel == "e":
            vowel = "o"
            onset = delabialize(onset)
        elif vowel == "iː":
            vowel = "uː"
            onset = delabialize(onset)
    if syll_num == 0:
        vowel = apply_tone(vowel, tone)
    # print("→", onset, vowel)
    syll = onset + vowel
    return syll


def delabialize(consonant):
    if consonant == "w":
        return "j"
    if len(consonant) > 1 and consonant[-1] == "ʷ":
        return consonant[:-1]


def apply_tone(vowel, tone):
    if len(vowel) > 1:
        return vowel[0] + tone + vowel[1:]
    return vowel + tone


def get_syllable(s, syll_num):
    shapes = s.split('V')
    return generate_syllable(shapes[0], shapes[1], syll_num)


def is_labial(syllable):
    for c in ["w", "ʷ", "o", "u"]:
        if c in syllable:
            return True
    return False


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
            if len(syllables) > 0 and is_labial(syllables[-1]):
                while is_labial(syllable):
                    structure = rand.choice(SYLL_STRUCTS)
                    syllable = get_syllable(structure, s)
            syllables.append(syllable)
        # for syll in syllables:
        #     print(syll, is_labial(syll))
        word = "".join(syllables)
        attempts += 1
        if len(word) > 1 and word not in words:
            words.append(word)
            print(word)
            w += 1
