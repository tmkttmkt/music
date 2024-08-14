import librosa
import numpy as np
import matplotlib.pyplot as plt

# 音声ファイルをロード
y, sr = librosa.load("wav\\gou.wav")

# STFTを計算
D = librosa.stft(y)

# 結果をパワースペクトログラム（振幅の二乗）に変換
S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)

# スペクトログラムを表示
plt.figure(figsize=(10, 6))
librosa.display.specshow(S_db, sr=sr, x_axis='time', y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Spectrogram (STFT)')
plt.show()
