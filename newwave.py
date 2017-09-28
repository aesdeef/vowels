# starting code (that plays a single sine wave) from https://stackoverflow.com/a/27978895

import pyaudio # a library that plays the sounds from memory
import numpy as np
import time
import scipy.io.wavfile # used to save the sounds as .wav files

volume = 0.5     # range [0.0, 1.0]
fs = 44100       # sampling rate, in Hz
f0 = 150.0
f = [f0*i for i in range(1, int(5000/f0))]

# data from:
# Wells, A study of the formants of the pure vowels of British English
# http://www.phon.ucl.ac.uk/home/wells/formants/table-1-uni.htm
data = {
    'iː': {'f1': 285,
        'f2': 2373,
        'f3': 3088,
        'duration': .293},
    'ɪ': {'f1': 356,
        'f2': 2098,
        'f3': 2696,
        'duration': .139},
    'ɛ': {'f1': 569,
        'f2': 1965,
        'f3': 2636,
        'duration': .170},
    'a': {'f1': 748,
        'f2': 1746,
        'f3': 2460,
        'duration': .210}, # IPA: æ
    'ɑː': {'f1': 677,
        'f2': 1083,
        'f3': 2340,
        'duration': .335},
    'ɒ': {'f1': 599,
        'f2': 891,
        'f3': 2605,
        'duration': .178},
    'ɔː': {'f1': 449,
        'f2': 737,
        'f3': 2635,
        'duration': .330},
    'ʊ': {'f1': 376,
        'f2': 950,
        'f3': 2440,
        'duration': .142},
    'uː': {'f1': 309,
        'f2': 939,
        'f3': 2320,
        'duration': .294},
    'ʌ': {'f1': 722,
        'f2': 1236,
        'f3': 2537,
        'duration': .148},
    'əː': {'f1': 581,
        'f2': 1381,
        'f3': 2436,
        'duration': .309}, # IPA: ɜː
    'ə': {'f1': 581,
        'f2': 1381,
        'f3': 2436,
        'duration': .103}, # copied from ɜː with an arbitrary shorter 'duration'
}

# generates a sine wave of the given frequency and duration
def sinewave(frequency, duration):
    global fs
    return np.sin(2*np.pi*np.arange(fs*duration)*frequency/fs)

# generates the sound
def sound(vowel):
    d = data[vowel]['duration']*3
    timbre = (sinewave(f[0], d)/2 + sinewave(f[1], d)/4 + sinewave(f[2], d)/8 + sinewave(f[3], d)/16 + sinewave(f[4], d)/16).astype(np.float32)
    formants = (sinewave(data[vowel]['f1'], d)/2 + sinewave(data[vowel]['f2'], d)/3 + sinewave(data[vowel]['f3'], d)/6).astype(np.float32)
    return timbre/2 + formants/2

# play given sounds (or all if no arguments or an empty list given)
def play(sounds=data):
    if not sounds:
        sounds = data
    # opens the stream to play the sounds
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)

    for vowel in sounds:
        print(vowel)
        # plays the sound
        stream.write(volume*sound(vowel))

        # creates the .wav file, uncomment to re-create the files
        #scipy.io.wavfile.write('%s.wav' % vowel, fs, volume*sound(vowel))

        time.sleep(0.2)

    # closes the stream
    stream.stop_stream()
    stream.close()
    p.terminate()

if __name__ == '__main__':
    play()
