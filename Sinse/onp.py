import numpy as np

from scipy import signal
from random import randint


from player import Player

class Onp:
    def harmonic(self,func,f,v):
        n=1
        while True:
            func(f*n,v/n)
            n+=1
            if((v/n)<0.01):break
    def __init__(self,second,rate,wave=None) -> None:
        if wave==None:
            self.second=second
            self.rate=rate
            self.wave=np.zeros(int(rate * second))
        else:
            self.second=int(len(wave)/rate)
            self.rate=rate

    def reset(self):
        self.wave=np.zeros(int(self.rate * self.second))
    def paht(self,f):
        print(f)
        return np.cumsum(2.0 * np.pi * f / self.rate * np.ones(int(self.rate * self.second)))
    def noise(self,v,windf=None):
        wave=np.random.rand(int(self.rate*self.second))*v
        if windf!=None:window = windf(len(wave))
        else :window=np.ones(len(wave))
        self.wave+= wave*window
        return self
    def sin(self,f,v,windf=None):
        wave=np.sin(self.paht(f))*v
        if windf!=None:window = windf(len(wave))
        else :window=np.ones(len(wave))
        self.wave+= wave*window
        return self
    def nok(self,f,v,windf=None):
        wave=signal.sawtooth(self.paht(f))*v
        if windf!=None:window = windf(len(wave))
        else :window=np.ones(len(wave))
        self.wave+= wave*window
        return self
    def tan(self,f,v,windf=None):
        wave=signal.square(self.paht(f))*v
        if windf!=None:window = windf(len(wave))
        else :window=np.ones(len(wave))
        self.wave+= wave*window
        return self
    def san(self,f,v,windf=None):
        wave=signal.sawtooth(self.paht(f),0.5)*v
        if windf!=None:window = windf(len(wave))
        else :window=np.ones(len(wave))
        self.wave+= wave*window
        return self
    def sintan(self,f,v,windf=None):
        self.sin(f,v/2,windf=windf)
        self.tan(f,v/2,windf=windf)
        return self
    def noktan(self,f,v,windf):
        self.nok(f,v/2,windf=windf)
        self.tan(f,v/2,windf=windf)
        return self
    def random(self,mf,v,hantai=0):
        R=10**6
        point=0
        wave=np.zeros(len(self.wave))
        n=0
        up_dwon=1
        num=int((((mf*2*4)/(1-hantai))/self.rate)*R)
        print(num,int(-hantai*num),"aa",len(self.wave))
        while n<len(self.wave):
            wave[n]=point
            point+=randint(int(-hantai*num),num)*up_dwon
            if R<point:
                point=R
                up_dwon=-1
            elif -R>point:
                point=-R
                up_dwon=1
            n+=1
        wave/=R
        wave*=v
        self.wave+=wave
        return self
    def ifft(self,lis,v):
        l=np.zeros(len(self.wave))
        n=0
        for fd in lis:
            l[int(n)]=fd
            if n!=0:l[len(l)-int(n)]=fd
            n+=1
        wave=np.fft.ifft(l).real
        self.wave+=(wave/np.max(np.abs(wave)))*v
    def fft(self):
        wave=np.fft.fft(self.wave)[0:self.rate//2]
        return (wave/np.max(np.abs(wave)))
    
    def __and__(self,other):
        if self.rate!=other.rate:
            print("レートがあってません")
            exit()
        return Onp(0,self.rate,wave=self.rate*other.rate)
    def __or__(self,other):
        if self.rate!=other.rate:
            print("レートがあってません")
            exit()
        return Onp(0,self.rate,wave=self.rate+other.rate)
    def __add__(self,other):
        if self.rate!=other.rate:
            print("レートがあってません")
            exit()
        return Onp(0,self.rate,wave=np.concatenate([self.rate,other.rate]))