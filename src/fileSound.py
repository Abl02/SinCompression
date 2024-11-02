from src.soundClass import SOUND
import time
import pyaudio

from scipy.io import wavfile
import scipy.fftpack as fftpk
import scipy

import numpy as np
import heapq

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

    def plot(self, plt) -> None:
        plt.plot(self.signal)
        plt.ylabel("Amplitude")
        plt.xlabel("Time")
        plt.title("Sample Wav")
        plt.show()

    def plotFFT(self, plt) -> None:
        plt.plot(
            self.freqs[range(len(self.FFT) // 2)], self.FFT[range(len(self.FFT) // 2)]
        )
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Amplitude")
        plt.show()

    def decompose(self, plt) -> None:
        # TO DO - the same as plotfft for the moment, should be modified to
        # calculate the frequencies that composes the sound and write them in
        # a file (should waight way less then the initial file) then reverse
        # fft to the file to get the initial wav sound (with low differences)
        
        positive_freqs = self.freqs[:len(self.freqs) // 2]
        positive_magnitudes = self.FFT[:len(self.freqs) // 2]

        # Find the top '100' frequencies based on magnitude using a heap
        top_frequencies = heapq.nlargest(100, zip(positive_magnitudes, positive_freqs), key=lambda x: x[0])

        # Extract and sort by frequency for better readability
        top_frequencies.sort(key=lambda x: x[1])  # Sort by frequency, if desired

        duration = 0.1
        # Generate a time array
        t = np.linspace(0, duration, int(self.s_rate * duration), endpoint=False)

        # Plot each sine wave
        plt.figure(figsize=(12, 6))
        for magnitude, frequency in top_frequencies:
            sine_wave = (magnitude*5) * np.sin(2 * np.pi * (frequency/10) * t)
            plt.plot(t, sine_wave, alpha=0.5, label=f'{frequency:.1f} Hz')

        # Label the plot
        plt.xlabel("Time (s)")
        plt.ylabel("Amplitude")
        plt.title(f"Top {100} Frequencies as Sine Waves")
        plt.legend(loc="upper right", fontsize="small", ncol=2)
        plt.show()
