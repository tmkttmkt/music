
import numpy as np
import librosa
import matplotlib.pyplot as plt

dt=1
f=440
sampling_rate=44100

t = np.arange(0, dt, 1/sampling_rate)

# 正弦波の式を使って波形生成
wave = np.cos(2 * np.pi * f * t)


# チャンネルが2 （ステレオ) の場合，交互にデータが入っているので，二つおきに読み出す。
# ただし，今回の場合はモノラルのはず。つまり，sounds.channels = 1

dt = 1.0/44100 # サンプリング時間

N=len(wave)
# 時間アレイを作る
tms = 0.0 # サンプル開始時間を0にセット

tm = np.linspace(tms,N,N, endpoint=False) # 時間ndarrayを作成

# DFT

x = np.fft.fft(wave)
f = np.fft.fftfreq(N, dt) # xのindexに対応する周波数のndarrayを取得




fig = plt.figure()

ax_1 = fig.add_subplot(121)
ax_2 = fig.add_subplot(122)
ax_1.plot(t,x)
ax_2.plot(f,x)


plt.show()
