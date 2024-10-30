#! /bin/python3

import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import scipy.fftpack as fftpk
import scipy
import pyaudio
import time

#################################################
### Fast Fourier Transform of .wav sound file ###
#################################################

s_rate, signal = wavfile.read("wav/wava1mono.wav")
FFT = abs(scipy.fft.fft(signal))
freqs = fftpk.fftfreq(len(FFT), (1.0 / s_rate))
print(type(freqs),type(FFT),type(s_rate),type(signal))



#################################################
### Playing sine wave sound                   ###
#################################################

p = pyaudio.PyAudio()
volume = 0.5  # range[0.0, 1.0]
fs = 44100  # sampling rate, Hz, must be integer
duration = 2.0  # in seconds, may be float
f = 440.0  # sine frequency, Hz, may be float

# generate samples, note conversion to float32 array
samples = (np.sin(2 * np.pi * np.arange(fs * duration) * f / fs)).astype(np.float32)

output_bytes = (volume * samples).tobytes()


def play():
    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=fs, output=True)
    start_time = time.time()
    stream.write(output_bytes)
    print("Played sound for {:.2f} seconds".format(time.time() - start_time))
    stream.stop_stream()
    stream.close()


def showfft():
    plt.plot(freqs[range(len(FFT) // 2)], FFT[range(len(FFT) // 2)])
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")
    plt.show()


def showWav():
    plt.plot(signal)
    plt.ylabel("Amplitude")
    plt.xlabel("Time")
    plt.title("Sample Wav")
    plt.show()


"""
Call from interactive file when exiting
"""


def exit():
    p.terminate()


DISPATCHER_P = {"showf": showfft, "show": showWav}
DISPATCHER_N = {"play": play}
