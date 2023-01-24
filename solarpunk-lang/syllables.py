import argparse
from random import choice, random

INITIALS = [
        'm', 'n', 'ŋ', 'p', 'b', 't', 'd', 'k', 'ɡ',
        'pʷ', 'bʷ', 'tʷ', 'dʷ', 'kʷ', 'ɡʷ',
        'pʲ', 'bʲ', 'tʲ', 'dʲ', 'kʲ', 'ɡʲ',
        'f', 's', 'x', 'l'
]
PALATAL_VOWELS = ['ɪ', 'ɛ', 'a']
CARDINAL_VOWELS = ['ɨ', 'ə', 'a']
LABIAL_VOWELS = ['ʊ', 'ɔ', 'a']
FINALS = [
        'm', 'n', 'ŋ',
        'f', 's', 'x', 'l'
]
WORD_LENGTHS = [
        1, 1, 1, 1,
        2, 2,
        3,
]


def main(iterations=20, syllables=-1):
    words = []
    if syllables < 0:
        syllables = WORD_LENGTHS
    else:
        syllables = [syllables]
    for iteration in range(iterations):
        unique = False
        while not unique:
            word = ''
            for syllable in range(choice(syllables)):
                onset = choice(INITIALS)
                if 'm' in onset or 'ʷ' in onset:
                    vowel = choice(LABIAL_VOWELS)
                elif 'ŋ' in onset or 'ʲ' in onset:
                    vowel = choice(PALATAL_VOWELS)
                else:
                    vowel = choice(CARDINAL_VOWELS)
                coda = ''
                if random() < 0.33:
                    coda = choice(FINALS)
                word += onset + vowel + coda
            if word not in words:
                unique = True
                words.append(word)
    words.sort()
    print(*words, sep='\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--iterations')
    parser.add_argument('-s', '--syllables')
    arɡs = parser.parse_args()

    iterations = 20
    syllables = -1
    if arɡs.iterations:
        iterations = int(arɡs.iterations)
    if arɡs.syllables:
        syllables = int(arɡs.syllables)
    main(iterations, syllables)
