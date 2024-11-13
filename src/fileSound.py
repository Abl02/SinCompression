from src.soundClass import SOUND
import time
import pyaudio

from scipy.io import wavfile
import scipy.fftpack as fftpk
import scipy

import numpy as np

#################################################
### Fast Fourier Transform of .wav sound file ###
#################################################


class FILE(SOUND):
    def __init__(self, filepath, duration=1.0, volume=0.5) -> None:
        super().__init__(0)
        self.file = filepath
        self.duration = duration
        self.volume = volume
        self.s_rate, self.signal = wavfile.read(self.file)

        # Check if the signal is stereo
        channels = 2 if self.signal.ndim > 1 else 1
        if channels == 2:
            self.signal = self.signal.mean(axis=1).astype(
                self.signal.dtype
            )  # Convert to mono
            channels = 1

        self.FFT = abs(scipy.fft.fft(self.signal))
        self.freqs = fftpk.fftfreq(len(self.FFT), (1.0 / self.s_rate))

    def play(self, audio) -> None:
        if self.signal.dtype == np.int16:
            format = pyaudio.paInt16
        elif self.signal.dtype == np.int32:
            format = pyaudio.paInt32
        elif self.signal.dtype == np.float32:
            format = pyaudio.paFloat32
        else:
            raise ValueError("Unsupported audio format: {}".format(self.signal.dtype))

        output_bytes = (self.signal * self.volume).astype(self.signal.dtype).tobytes()

        stream = audio.open(format=format, channels=1, rate=self.s_rate, output=True)
        start_time = time.time()
        stream.write(output_bytes)
        print("Played sound for {:.2f} seconds".format(time.time() - start_time))
        stream.stop_stream()
        stream.close()

