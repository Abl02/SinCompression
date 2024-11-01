from logging import raiseExceptions


class SOUND:
    def __init__(self, s_rate) -> None:
        self.s_rate = s_rate  # Sample rate
        self.signal = None  # Placeholder for audio signal

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
        raise NotImplementedError("Subclasses must implement this method.")
