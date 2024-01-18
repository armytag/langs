import random as rand

NASALS = [
    "m", "n", "ng",
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
SYLL_STRUCTS += ['CCV'] * 1
SYLL_STRUCTS += ['CCVC'] * 1
SYLL_COUNTS = []
SYLL_COUNTS += [1] * 1
SYLL_COUNTS += [2] * 1
SYLL_COUNTS += [3] * 1
SYLL_COUNTS += [4] * 1

def generate_syllable(has_cluster, has_coda):
    onset = ''
    vowel = ''
    coda = ''
    if has_cluster:
        shape = rand.choice([
            [PLOSIVES, APPROXIMANTS],
            [PLOSIVES, FRICATIVES],
            [FRICATIVES, APPROXIMANTS],
        ])
        for part in shape:
            onset += rand.choice(part)
    else:
        onset = rand.choice(rand.choice([
            PLOSIVES, NASALS, FRICATIVES, APPROXIMANTS
        ]))
    vowel = rand.choice(VOWELS)
    if has_coda:
        coda = rand.choice(rand.choice([
            NASALS, FRICATIVES, APPROXIMANTS
        ]))
    syll = onset + vowel + coda
    return syll

def get_syllable(s):
    if len(s) < 3:  # Must be 'V', 'CV', or 'VC'
        return generate_syllable(False, s[-1]=='C')
    return generate_syllable(s[1]=='C', s[-1]=='C')

if __name__ == "__main__":
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
