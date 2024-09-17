import librosa
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

# 音声ファイルの読み込み
y, sr = librosa.load('kyudesu.wav')

# STFTのパラメータ
n_fft = 2048           # フーリエ変換に使用するサンプルの数
hop_length = 512       # 隣接するフレーム間のサンプル数
win_length = 2048      # 各フレームに適用されるウィンドウのサイズ
window = 'hann'        # ウィンドウ関数

# STFTの計算
D = librosa.stft(y, n_fft=n_fft, hop_length=hop_length, win_length=win_length, window=window)


# デシベルスケールに変換
S_db = librosa.amplitude_to_db( np.abs(D), ref=np.max)

# スペクトログラムのプロット
plt.figure(figsize=(10, 6))
librosa.display.specshow(S_db, sr=sr, hop_length=hop_length, x_axis='time', y_axis='log', cmap='viridis')
plt.colorbar(format='%+2.0f dB')
plt.title('STFT Spectrogram')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.show()

# iSTFTを使用して信号を再構築
y_reconstructed = librosa.istft(D, hop_length=hop_length, win_length=win_length, window=window)

# オリジナルと再構築された音声信号をプロット
plt.figure(figsize=(14, 6))

# オリジナル信号のプロット
plt.subplot(2, 1, 1)
plt.plot(y, color='blue')
plt.title('Original Audio Signal')
plt.xlabel('Sample')
plt.ylabel('Amplitude')

# 再構築された信号のプロット
plt.subplot(2, 1, 2)
plt.plot(y_reconstructed, color='orange')
plt.title('Reconstructed Audio Signal from iSTFT')
plt.xlabel('Sample')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()

# 再構築された音声信号を保存
output_file = 'kyudesu_stft.wav'
sf.write(output_file, y_reconstructed, sr)
