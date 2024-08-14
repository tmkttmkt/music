import numpy as np
import scipy
from scipy import signal
from random import randint

import scipy.fft
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
        wave=self.wave_function.cal(self.__wave)
        fft_size=2024
        if len(wave) < fft_size:
            padded_wave = np.pad(wave, (0, fft_size - len(wave)), 'constant')
        else:
            padded_wave = wave
        # ウィンドウ関数の適用: ハニング窓を使用
        windowed_wave = padded_wave * np.hanning(len(padded_wave))
        waved=scipy.fft.fft(windowed_wave)[0:self.rate//2]
        return (waved/np.max(np.abs(waved)))
def Ifft(array,v=1.0,rate=44100):
    second=len(array)/rate
    cls=Onp(second)
    fft_size = len(array)*2

    # 元のFFTサイズに合わせてゼロパディング
    padded_freq_data = np.zeros(fft_size, dtype=complex)
    padded_freq_data[:len(array)] = array
    padded_freq_data[len(array):] = np.conj(array[::-1])[:fft_size - len(array)]

    # IFFTの計算
    wave = scipy.fft.ifft(padded_freq_data).real
    cls.wave_function=Constwave(wave,v)
    return cls
