from logging import raiseExceptions

import scipy.fftpack as fftpk
import scipy

import numpy as np
import heapq

class SOUND:
    def __init__(self, s_rate) -> None:
        self.s_rate = s_rate  # Sample rate
        self.signal = None  # Placeholder for audio signal

        self.FFT = None
        self.freqs = None

    def play(self, audio):
        """
        Play sound using PyAudio
        :audio: pyaudio.PyAudio()
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def plot(self, plt):
        """
        Plot the audio signal
        :plot: matplot
        """
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
