import random as rand

ONSETS = [
        'p', 'b', 'pʷ', 'bʷ',
        't', 'd', 'tʷ', 'dʷ',
        'ʈ', 'ɖ', 'ʈʷ', 'ɖʷ',
        'k', 'g', 'kʷ', 'gʷ',
]
VOWELS = [
        'i', 'e', 'ɛ', 'u', 'o', 'ɔ'
]
CODAS = [
        'f', 'm',
        's', 'l',
        'x'
]
SYLL_STRUCTS = []
SYLL_STRUCTS += ['VC'] * 4
SYLL_STRUCTS += ['CV'] * 3
SYLL_STRUCTS += ['CVC'] * 2
SYLL_COUNTS = []
SYLL_COUNTS = [1] * 4
SYLL_COUNTS += [2] * 2
SYLL_COUNTS += [3] * 1

def generate_syllable(has_onset, has_coda):
    onset = ''
    coda = ''
    vowel = rand.choice(VOWELS)
    if has_onset:
        onset = rand.choice(ONSETS)
    if has_coda:
        coda = rand.choice(CODAS)
    return onset + vowel + coda

def get_syllable(s):
    return generate_syllable(s[0]=='C', s[-1]=='C')

if __name__ == "__main__":
    word_count = 20
    for idx in range(word_count):
        syll_count = rand.choice(SYLL_COUNTS)
        word = ''
        for idx in range(syll_count):
            structure = rand.choice(SYLL_STRUCTS)
            syllable = get_syllable(structure)
            word += syllable
        print(word)
