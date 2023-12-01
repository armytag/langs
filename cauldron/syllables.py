import random as rand

ONSETS = [
        'p', 'b', 'ph', 'pw', 'bw', 'phw',
        't', 'd', 'th', 'tw', 'dw', 'thw',
        'k', 'g', 'kh', 'kw', 'gw', 'khw',
        'm', 'l'
]
VOWELS = [
        "i", "a", "u", ":i", ":a", ":u"
]
CODAS = [
        'f', 'm',
        's', 'l',
]
SYLL_STRUCTS = ['V'] * 1
SYLL_STRUCTS += ['VC'] * 3
SYLL_STRUCTS += ['CV'] * 1
SYLL_STRUCTS += ['CVC'] * 2
SYLL_COUNTS = []
SYLL_COUNTS = [1] * 3
SYLL_COUNTS += [2] * 3
SYLL_COUNTS += [3] * 2

def generate_syllable(has_onset, has_coda):
    onset = ''
    coda = ''
    vowel = rand.choice(VOWELS)
    if has_onset:
        onset = rand.choice(ONSETS)
    if has_coda:
        coda = rand.choice(CODAS)
    syll = onset + vowel + coda
    if onset == 'l':
        print(syll)
    return syll

def get_syllable(s):
    return generate_syllable(s[0]=='C', s[-1]=='C')

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
    print(' '.join(words))
