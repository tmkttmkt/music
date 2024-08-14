import numpy as np
from scipy import signal
from random import randint
from player import Player

class Wave:
    def __init__(self,f,v,rate=44100) -> None:
        self.f=f
        self.v=v
        self.rate=rate
    def cal(self,array):
        return np.sin(self.paht(array))*self.v
    def paht(self,array):
        return np.cumsum(2.0 * np.pi * self.f / self.rate * np.ones(len(array)))
    def maxabs(self,array):
        if np.max(np.abs(array))>0:
            return (array/np.max(np.abs(array)))*self.v
        else:
            return array
    def __str__(self) -> str:
        return str(round(self.f,4))+"Hzの"+self.__class__.__name__

class Constwave(Wave):
    def __init__(self,array,v) -> None:
        self.array=array
        self.v=v
    def cal(self,array):
        return self.maxabs(self.array)

class Reverse(Wave):
    def __init__(self,wave:Wave) -> None:
        self.wave=wave
    def cal(self, array):
        return self.wave.cal(array)*-1
class Wavelist(Wave):
    def __init__(self,list,v,rate=44100,siki="*") -> None:
        self.v=v
        self.rate=rate
        self.list:list[Wave]=list
        self.siki=siki
    def cal(self,array):
        retarray=array.copy()
        if self.siki=="*":func=lambda a,b:a*b
        elif self.siki=="+":func=lambda a,b:a+b
        else :func=None
        for waveobj in self.list:
            retarray=func(retarray,waveobj.cal(array))
        return self.maxabs(retarray)
    def __str__(self) -> str:
        return str(len(self.list))+"個の"+self.__class__.__name__
class Sin(Wave):
    def cal(self,array):
        return np.sin(self.paht(array))*self.v
class Nok(Wave):
    def cal(self,array):
        return signal.sawtooth(self.paht(array))*self.v
class Tan(Wave):
    def cal(self,array):
        return signal.square(self.paht(array))*self.v
class San(Wave):
    def cal(self,array):
        return signal.sawtooth(self.paht(array))*self.v
class Noise(Wave):
    def cal(self,array):
        return np.random.rand(self.paht(array))*self.v

class Random(Wave):
    def __init__(self,mf,v,rate=44100) -> None:
        self.mf=mf
        self.v=v
        self.rate=rate
    def cal(self,array):
        hantai=0
        R=10**6
        point=0
        n=0
        up_dwon=1
        num=int((((self.mf*2*4)/(1-hantai))/self.rate)*R)
        while n<len(array):
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
        wave*=self.v
        return wave
    def __str__(self) -> str:
        return "これはRandomクラスです"




class Window:
    def __init__(self,rate=44100) -> None:
        pass
    def main(sedlf,array):
        M=len(array)
        return np.ones(M)
    def cal(self,array):
        return array*self.main(array)


class Tukey(Window):
    def __init__(self,alpha,rate=44100) -> None:
        self.alpha=alpha
    def main(self,array, alpha):
        M=len(array)
        """
        Tukey window.
        Parameters
        ----------
        M : int
            Number of points in the output window.
        alpha : float, optional
            Shape parameter of the Tukey window.
        Returns
        -------
        w : ndarray
            The window, with the maximum value normalized to one.
        """
        if alpha <= 0:
            return np.ones(M)
        elif alpha >= 1.0:
            return np.hanning(M)
        else:
            x = np.linspace(0, 1, M)
            w = np.ones(M)
            first_condition = x < alpha / 2
            w[first_condition] = 0.5 * (1 + np.cos(2 * np.pi / alpha * (x[first_condition] - alpha / 2)))
            third_condition = x >= (1 - alpha / 2)
            w[third_condition] = 0.5 * (1 + np.cos(2 * np.pi / alpha * (x[third_condition] - 1 + alpha / 2)))
            return w
    def cal(self,array):
        return array*self.main(array,self.alpha)

class ADSR_time(Window):
    def __init__(self,a,d,s,r,rate=44100) -> None:
        self.a=a
        self.d=d
        self.s=s
        self.r=r
        self.rate=rate
    def main(self,array):
        M=len(array)
        attack_samples = int(self.rate * self.a)
        decay_samples = int(self.rate * self.d)
        release_samples = int(self.rate * self.r)
        sustain_samples = M - (attack_samples + decay_samples + release_samples)
        if sustain_samples < 0:
            raise ValueError("アタック、ディケイ、リリース時間の合計が波形の長さを超えています。")
            # ADSR エンベロープを作成
        attack_curve = np.linspace(0, 1, attack_samples)
        decay_curve = np.linspace(1, self.s, decay_samples)
        sustain_curve = np.full(sustain_samples,self.s)
        release_curve = np.linspace(self.s, 0, release_samples)

        # フェーズを連結
        adsr_envelope = np.concatenate([attack_curve, decay_curve, sustain_curve, release_curve])

        # エンベロープを波形に適用
        processed_wave = array[:len(adsr_envelope)] * adsr_envelope

        return processed_wave
        
    def cal(self,array):
        return array*self.main(array)
class ADSR_par(Window):
    def __init__(self,a,d,s,r,rate=44100) -> None:
        self.a=a
        self.d=d
        self.s=s
        self.r=r
        self.rate=rate
    def main(self,array):
        M=len(array)
        attack_samples = int(M*self.a)
        decay_samples = int(M*self.d)
        release_samples = int(M*self.r)
        sustain_samples = M - (attack_samples + decay_samples + release_samples)

        if sustain_samples < 0:
            raise ValueError("アタック、ディケイ、リリース時間の合計が波形の長さを超えています。")
            # ADSR エンベロープを作成
        attack_curve = np.linspace(0, 1, attack_samples)
        decay_curve = np.linspace(1, self.s, decay_samples)
        sustain_curve = np.full(sustain_samples,self.s)
        release_curve = np.linspace(self.s, 0, release_samples)

        # フェーズを連結
        adsr_envelope = np.concatenate([attack_curve, decay_curve, sustain_curve, release_curve])

        # エンベロープを波形に適用
        processed_wave = array[:len(adsr_envelope)] * adsr_envelope

        return processed_wave
        
    def cal(self,array):
        return array*self.main(array)


class Effect:
    def __init__(self) -> None:
        pass
    def cal(self,array):
        return array
