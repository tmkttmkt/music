import numpy as np
from scipy.io import wavfile
from scipy import signal
import subprocess

A1_FREQ = 55.0
FREQUENCY = {
    "C": A1_FREQ * 2 ** (-9 / 12.0),
    "C#": A1_FREQ * 2 ** (-8 / 12.0),
    "Db": A1_FREQ * 2 ** (-8 / 12.0),
    "D": A1_FREQ * 2 ** (-7 / 12.0),
    "D#": A1_FREQ * 2 ** (-6 / 12.0),
    "Eb": A1_FREQ * 2 ** (-6 / 12.0),
    "E": A1_FREQ * 2 ** (-5 / 12.0),
    "F": A1_FREQ * 2 ** (-4 / 12.0),
    "F#": A1_FREQ * 2 ** (-3 / 12.0),
    "Gb": A1_FREQ * 2 ** (-3 / 12.0),
    "G": A1_FREQ * 2 ** (-2 / 12.0),
    "G#": A1_FREQ * 2 ** (-1 / 12.0),
    "Ab": A1_FREQ * 2 ** (-1 / 12.0),
    "A": A1_FREQ,
    "A#": A1_FREQ * 2 ** (1 / 12.0),
    "Bb": A1_FREQ * 2 ** (1 / 12.0),
    "B": A1_FREQ * 2 ** (2 / 12.0),
}
def nf(num):
    pa=num%7
    wa=num//7
    base=ord("A")
    base+=pa
    print(num,pa,wa,chr(base))
    return FREQUENCY[chr(base)]*2**(wa-1)
def f(str):
    str=str.upper()
    return FREQUENCY[str[:-1]]*2**(int(str[-1])-1)
class Player(object):

    def __init__(self, rate=44100):
        try:
            import pyaudio
            self._pyaudio = pyaudio.PyAudio()
            self._format = pyaudio.paInt16
        except ImportError:
            self._pyaudio = None
        self._stream = None
        # TODO: support stereo channels
        self._channels = 1
        self._rate = rate

    def enumerate_device(self):
        if not self._pyaudio:
            raise ImportError("Failed to import pyaudio, please install pyaudio")
        for n in range(self._pyaudio.get_device_count()):
            device = self._pyaudio.get_device_info_by_index(n)
            print('index: {index:02d}, name: "{name}", rate: {rate:5d}'.format(
                index=n, name=device["name"], rate=int(device["defaultSampleRate"])))

    def open_stream(self, device_name=None, device_index=-1):
        u""" open audio output stream

        if neither device_name nor device_index is specified,
        default output device will be opened.

        :param str device_name: part of device name (ex: hw:0,0)
        :param int device_index: index of device
        """
        if not self._pyaudio:
            raise ImportError("Failed to import pyaudio, please install pyaudio")
        if device_name:
            for n in range(self._pyaudio.get_device_count()):
                dev = self._pyaudio.get_device_info_by_index(n)
                if dev["name"].find(device_name) >= 0:
                    device = dev
                    break
            else:
                raise RuntimeError("audio device {} not found".format(device_name))
        elif device_index >= 0:
            device = self._pyaudio.get_device_info_by_index(device_index)
        else:
            device = self._pyaudio.get_default_output_device_info()

        self._stream = self._pyaudio.open(
            channels=self._channels,
            format=self._format,
            rate=self._rate,
            output_device_index=device["index"],
            output=True,
        )

    def play_wave(self, wave):
        u""" play normalized wave

        :param numpy.array wave: normalized wave
        """
        if not self._stream:
            raise RuntimeError("audio stream is not opened, please call open_stream() first.")
        wave = (wave * float(2 ** 15 - 1)).astype(np.int16).tobytes()
        self._stream.write(wave)

class onp:
    def __init__(self,second,rate) -> None:
        self.second=second
        self.rate=rate
        self.wave=np.zeros(int(rate * second))
    def reset(self):
        self.wave=np.zeros(int(self.rate * self.second))
    def paht(self,f):
        print(f)
        return np.cumsum(2.0 * np.pi * f / self.rate * np.ones(int(self.rate * self.second)))
    
    def noise(self,v):
        self.wave+=np.random.rand(self.rate*self.second)*v
    def sin(self,f,v):
        self.wave+=np.sin(self.paht(f))*v
    def nok(self,f,v):
        self.wave+=signal.sawtooth(self.paht(f))*v
    def tan(self,f,v):
        self.wave+=signal.square(self.paht(f))*v
    def san(self,f,v):
        self.wave+=signal.sawtooth(self.paht(f),0.5)*v
    def sintan(self,f,v):
        self.wave+=np.sin(self.paht(f))*v/2
        self.wave+=signal.square(self.paht(f))*v/2
    def noktan(self,f,v):
        self.wave+=signal.square(self.paht(f),0.5)*v/2
        self.wave+=signal.square(self.paht(f))*v/2
class track:
    def __init__(self,rate,second,args,name):
        self.wave=np.zeros(int(rate * second))
        wave=[]
        for on in args:
            wave.append(on.wave)
        wave=np.concatenate(wave)
        self.wave=np.concatenate([self.wave,wave])
        self.name=name
    def volume(self,volume):
        self.wave*=volume
class kyok:
    def __init__(self,rate,second=1,file_name=None) -> None:
        self.rate=rate
        self.file_name=file_name
        self.p=Player()
        self.output_file_name=None
        self.second=second
    def create_onp(self,second):
        return onp(second,self.rate)
    def create_track(self,second,args,name=""):
        return track(self.rate,second,args,name)
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
