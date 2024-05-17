import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from sinse import *

fs = 44100  # Hz
k=kyok(fs)
time=1
on=k.create_onp(time)

on.sin(40,0.1)
on.sin(43,0.2)
# サンプリング周波数
# サンプル数
t = np.arange(0, time, 1/fs)  # 1秒間の信号


# フーリエ変換
freqs = fftfreq(len(t), 1/fs)
fft_values = fft(on.wave)

# フーリエ変換の結果は対称性を持つため、半分だけを取得
positive_freqs = freqs[:len(freqs)//2]
positive_fft_values = 2.0/len(t) * np.abs(fft_values[:len(freqs)//2])
print(fft_values[:100])

# プロット
plt.figure(figsize=(12, 4))

# オリジナル信号のプロット
plt.subplot(1, 2, 1)
plt.plot(t, on.wave)
plt.title('Original Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# フーリエ変換の結果のプロット
plt.subplot(1, 2, 2)
plt.plot(positive_freqs, positive_fft_values)
plt.title('Fourier Transform')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
