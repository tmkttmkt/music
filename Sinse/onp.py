import numpy as np
import scipy
from scipy import signal
from random import randint
import pyfftw
import librosa
import scipy.fft
from A import normal_stft
from player import Player
from onp_fun import *
"""
Onpクラスがこのままでいいのか
1.波メソットをクラスに分離
2.基本と派生に分類
音ASDR
"""

class Onp:
    length:int=0
    wave_function:Wave=Wave(440,0.5)
    effects:list[Effect]=[]
    window:Window=Window()
    __wave=np.zeros(1)
    def __init__(self,second,rate=44100):
        self.length=int(second*rate)
        self.__wave=np.zeros(self.length)
        self.rate=rate
    @property #ゲッター
    def simwave(self):
        return self.wave_function.cal(self.__wave)
    @property #ゲッター
    def wave(self):
        wave=self.window.cal(self.wave_function.cal(self.__wave))
        for effect in self.effects:
            wave=effect.cal(wave)
        return wave
    def fft(self):
        wave=pyfftw.interfaces.numpy_fft.fft(self.wave_function.cal(self.__wave))
        return (wave/np.max(np.abs(wave)))
    def stft(self,element_stft=normal_stft):
        return librosa.stft(self.wave_function.cal(self.__wave), n_fft=element_stft["n_fft"], hop_length=element_stft["hop_length"], win_length=element_stft["win_length"], window=element_stft["window"])