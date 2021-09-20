from os import system
from time import sleep

from pygame import mixer

class Voice:
    def __init__(self,file_path:str="audio/tts_output.wav") -> None:
        self.audio_path=file_path
        self.synthesiser = mixer
        self.synthesiser.init()

    def speak(self, text:str) -> None:
        system(f'tts --text "{text}" --out_path {self.audio_path}')
        self.synthesiser.music.load(self.audio_path)
        self.synthesiser.music.play()
        sleep(5)