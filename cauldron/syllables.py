import random as rand

ONSETS = [
        # "m̥", "m", "n̥", "n", "ŋ̊", "ŋ",
        "hm", "m", "hn", "n", "hnj", "nj",
        "p", "b", "t", "k", "g",
        "pw", "bw", "tw", "kw", "gw",
        "py", "by", "ty", "ky", "gy",
        "f", "s", "x",
        # "r", "l", "ɬ",
        "r", "l", "hl",
]
VOWELS = [
        "a", "e",
]
CODAS = [
        "m", "n", "nj",
        "f", "s", "x",
        "r", "l", "hl",
]
SYLL_STRUCTS = ['V'] * 0
SYLL_STRUCTS += ['VC'] * 0
SYLL_STRUCTS += ['CV'] * 3
SYLL_STRUCTS += ['CVC'] * 1
SYLL_COUNTS = []
SYLL_COUNTS = [1] * 3
SYLL_COUNTS += [2] * 3
SYLL_COUNTS += [3] * 2

def generate_syllable(has_coda):
    coda = ''
    onset = rand.choice(ONSETS)
    vowel = rand.choice(VOWELS)
    if vowel == 'e':
        if 'y' in onset:
            onset = onset[0]
            vowel = 'i'
        elif onset == 'hnj' or onset == 'nj':
            vowel = 'i'
        if 'w' in onset:
            onset = onset[0]
            vowel = 'u'
        elif onset == 'hm' or onset == 'm':
            vowel = 'u'
    if has_coda:
        coda = rand.choice(CODAS)
    syll = onset + vowel + coda
    return syll

def get_syllable(s):
    return generate_syllable(s[-1]=='C')

if __name__ == "__main__":
    word_count = 10
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
