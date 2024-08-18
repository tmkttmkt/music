import numpy as np
from onp import Onp





class Track:
    def __init__(self,rate,second,args):
        self.rate=rate
        self.wave=np.zeros(int(rate * second))
        if len(args)>0:
            if type(args[0]) == Onp:
                wave=[]
                for on in args:
                    wave.append(on.wave)
                wave=np.concatenate(wave)
            elif isinstance(args[0],np.ndarray):
                wave=np.concatenate(args)
            else:
                ValueError("そんなものは入れれない")
            self.wave=np.concatenate([self.wave,wave])
    def append_start(self,second):
        wave=np.zeros(int(self.rate * second))
        wave=np.concatenate([wave,self.wave])
    def append(self,onp):
        self.wave=np.concatenate([self.wave,onp.wave])
    def volume(self,volume):
        self.wave*=volume
    def __and__(self,other):
        if self.rate!=other.rate:
            ValueError("レートがあってません")
        return Track(self.rate,0,[self.wave*other.wave])
    def __or__(self,other):
        if self.rate!=other.rate:
            print("レートがあってません")
            exit()
        return Track(self.rate,0,[self.wave+other.wave])
    def __add__(self,other):
        if self.rate!=other.rate:
            ValueError("レートがあってません")
            exit()
        return Track(self.rate,0,[np.concatenate([self.wave,other.wave])])