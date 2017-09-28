from newwave import play
import sys

sampa_to_ipa = {
    'i': 'iː',
    'I': 'ɪ',
    'E': 'ɛ',
    '{': 'a',
    'A': 'ɑː',
    'Q': 'ɒ',
    'O': 'ɔː',
    'U': 'ʊ',
    'u': 'uː',
    'V': 'ʌ',
    '3': 'əː',
    '@': 'ə',
}

play([sampa_to_ipa[x] for x in sys.argv[1:]])