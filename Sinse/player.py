import numpy as np
import pyaudio

class Player(object):
    def __init__(self, rate=44100):
        self._pyaudio = pyaudio.PyAudio()
        self._format = pyaudio.paInt16
        self._stream = None
        # TODO: support stereo channels
        self._channels = 1
        self._rate = rate

    def enumerate_device(self):
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
