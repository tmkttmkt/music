import numpy as np
import matplotlib.pyplot as plt

def generate_sine_wave(frequency, duration, sampling_rate):
    # サンプリングポイントを生成
    t = np.arange(0, duration, 1/sampling_rate)
    
    # 正弦波の式を使って波形生成
    wave = np.cos(2 * np.pi * frequency * t)
    
    return t, wave

def inverse_fourier_transform(sine_wave):
    
    # 逆フーリエ変換
    inverse_transform = np.fft.fft(sine_wave)
    
    return inverse_transform  # 実部だけを取得

# パラメータの設定
frequency = 440  # Hz
duration = 1  # 秒
sampling_rate = 44100  # サンプリングレート

# 逆フーリエ変換を実行


fig = plt.figure()

ax_1 = fig.add_subplot(221)
ax_2 = fig.add_subplot(222)
ax_3 = fig.add_subplot(223)
ax_4 = fig.add_subplot(224)

tm,wavem=generate_sine_wave(frequency, duration, sampling_rate)
ax_1.plot(tm,wavem)

generated_wave = inverse_fourier_transform(wavem)
t=np.linspace(0,len(generated_wave), len(generated_wave), endpoint=False)
ax_2.plot(t, generated_wave)

f = np.fft.fftfreq(len(generated_wave), 1/sampling_rate)
ax_3.plot(f, generated_wave)

plt.show()
