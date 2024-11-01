from src.soundClass import SOUND
import numpy as np
import pyaudio
import time


#################################################
### Playing sine wave sound                   ###
#################################################


class SIN(SOUND):
    def __init__(self, frequency=440, duration=1.0, volume=0.1, s_rate=44100) -> None:
        super().__init__(s_rate)
        self.f = frequency
        self.duration = duration
        self.volume = volume
        self.signal = self._generateSignal()

    def _generateSignal(self):
        num_samples = int(self.s_rate * self.duration)
        t = np.linspace(0, self.duration, num_samples, endpoint=False)
        waveform = self.volume * np.sin(2 * np.pi * self.f * t)
        return np.int16(waveform * 32767)

    def play(self, audio) -> None:
        output_bytes = self.signal.tobytes()
        stream = audio.open(
            format=pyaudio.paInt16, channels=1, rate=self.s_rate, output=True
        )

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
