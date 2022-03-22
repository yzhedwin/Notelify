import numpy as np
from scipy.fft import *
from scipy.io import wavfile
import math

def freq(file, start_time, end_time):
    # Open the file and convert to mono
    sr, data = wavfile.read(file)
    if data.ndim > 1:
        data = data[:, 0]
    else:
        pass

    # Return a slice of the data from start_time to end_time
    dataToRead = data[int(start_time * sr / 1000): int(end_time * sr / 1000) + 1]

    # Fourier Transform
    N = len(dataToRead)
    yf = rfft(dataToRead)
    xf = rfftfreq(N, 1 / sr)

    # Uncomment these to see the frequency spectrum as a plot
    # plt.plot(xf, np.abs(yf))
    # plt.show()

    # Get the most dominant frequency and return it
    idx = np.argmax(np.abs(yf))
    freq = xf[idx]
    return freq

def freq_to_note(freq):
    notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

    # formula taken from https://en.wikipedia.org/wiki/Piano_key_frequencies
    note_number = 12 * math.log2(freq / 440) + 49
    note_number = round(note_number)

    note = (note_number - 1) % len(notes)
    note = notes[note]

    octave = (note_number + 8) // len(notes)

    return note, octave

if __name__ == '__main__':
    TIME_INTERVAL = 500
    SAMPLE_SIZE = 60
    for sample in range(SAMPLE_SIZE):
        frequency = freq("data/anthem.wav", sample * TIME_INTERVAL, (sample + 1) * TIME_INTERVAL)
        print("Frequency: ", frequency, "| Note: ", freq_to_note(frequency))
