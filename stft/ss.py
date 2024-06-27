import librosa
import matplotlib.pyplot as plt
import numpy as np


y, sr = librosa.load('wav\\gou.wav')
print(y)
print(len(y))
print('Sampling rate (Hz): %d' % sr)
print('Audio length (seconds): %.2f' % (len(y) / sr))

D = np.abs(librosa.stft(y, n_fft=2048, hop_length=44100//1000))
print(D.shape)


DB = librosa.amplitude_to_db(D, ref=np.max)
plt.figure(figsize=(16, 6))
librosa.display.specshow(DB, sr=sr, hop_length=512, x_axis='time', y_axis='log')
plt.colorbar()
plt.show()

# 仮の振幅スペクトログラムデータを生成する
D = np.random.random((100, 200))  # 仮のデータ（100行 x 200列）

# 振幅スペクトログラムをプロットする
 # viridisカラーマップを使用
#
