from utils import FREQ_MAP
from Tone import Tone


class Note:
    def __init__(self, freq_str, duration=1):
        self.freq_str = freq_str
        self.duration = duration
        self.freq_str = FREQ_MAP[(self.freq_str)]

    def play(self, speaker=None):
        Tone.sine(self.freq_str, duration=self.duration, speaker=speaker)
