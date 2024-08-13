import numpy as np
from scipy.io import wavfile
import subprocess

from A import A1_FREQ,FREQUENCY,f,nf
from player import Player
from onp import *
from track import Track
class kyok:
    def __init__(self,rate=44100,second=1,file_name=None) -> None:
        self.rate=rate
        self.file_name=file_name
        self.p=Player()
        self.output_file_name=None
        self.second=second
    def create_onp(self,second):
        return Onp(second,self.rate)
    def create_track(self,second,args):
        return Track(self.rate,second,args)
    def write_waves(self,args,file_name=""):
        wargs=np.zeros(int(self.rate * self.second))
        for sine in args:
            if len(wargs)>len(sine.wave):
                rwave=np.pad(sine.wave, (0, len(wargs)-len(sine.wave)), 'constant')
            elif len(wargs)<len(sine.wave):
                wargs=np.pad(wargs, (0, len(sine.wave)-len(wargs)), 'constant')
                rwave=sine.wave
            else:
                rwave=sine.wave
            wargs=wargs+rwave
            
        wave = (wargs * float(2 ** 15 - 1)).astype(np.int16)  # 値域を 16bit にする
        if file_name=="":
            if self.file_name==None:
                file_name="output"
            else:
                file_name=self.file_name
        file_name+=".wav"
        wavfile.write(file_name,self.rate, wave)
        self.output_file_name=file_name
    def play_waves(self,args):
        wargs=np.zeros(int(self.rate * self.second))
        for sine in args:
            if len(wargs)>len(sine.wave):
                rwave=np.pad(sine.wave, (0, len(wargs)-len(sine.wave)), 'constant')
            elif len(wargs)<len(sine.wave):
                wargs=np.pad(wargs, (0, len(sine.wave)-len(wargs)), 'constant')
                rwave=sine.wave
            else:
                rwave=sine.wave
            wargs=wargs+rwave
        self.p.open_stream()
        self.p.play_wave(wargs)
    def write(self,args,file_name=""):
        wargs=[]
        for on in args:
            wargs.append(on.wave)
        wave=np.concatenate(wargs)
        wave = (wave * float(2 ** 15 - 1)).astype(np.int16)  # 値域を 16bit にする
        if file_name=="":
            if self.file_name==None:
                file_name="output"
            else:
                file_name=self.file_name
        file_name+=".wav"
        wavfile.write(file_name,self.rate, wave)
        self.output_file_name=file_name
    def play(self,args):
        wargs=[]
        for on in args:
            wargs.append(on.wave)
        wave=np.concatenate(wargs)
        self.p.open_stream()
        self.p.play_wave(wave)
    def run(self):
        if self.output_file_name:
            subprocess.run(self.output_file_name, shell=True)
        else:
            raise RuntimeError("まだ出力してねぇぞ")
