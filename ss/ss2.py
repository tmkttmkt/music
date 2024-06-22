import librosa
import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf


y, sr = librosa.load('wav\\gou.wav')
print(y)
print(len(y))
print('Sampling rate (Hz): %d' % sr)
print('Audio length (seconds): %.2f' % (len(y) / sr))

n_fft = 2**11
hop_length = 2**9
win_length = 2**10
window = 'hann'

D = np.abs(librosa.stft(y, n_fft=n_fft, hop_length=hop_length, win_length=win_length, window=window))
print(D.shape)

S_db = librosa.amplitude_to_db(D, ref=np.max)


#"""# スペクトログラムのプロット
plt.figure(figsize=(10, 6))
librosa.display.specshow(S_db, sr=sr, x_axis='time', y_axis='log',cmap='viridis')
plt.colorbar(format='%+2.0f dB')
plt.title('STFT Spectrogram')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.show()
#"""
y_reconstructed = librosa.istft(D, hop_length=hop_length, win_length=win_length, window=window)

# オリジナルと再構築された音声信号をプロット
plt.figure(figsize=(14, 6))

# オリジナル信号のプロット
plt.subplot(2, 1, 1)
plt.plot(y)
plt.title('Original Audio Signal')
plt.xlabel('Sample')
plt.ylabel('Amplitude')

# 再構築された信号のプロット
plt.subplot(2, 1, 2)
plt.plot(y_reconstructed)
plt.title('Reconstructed Audio Signal from iSTFT')
plt.xlabel('Sample')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()

output_file = 'reconstructed_audio.wav'
sf.write(output_file, y_reconstructed, sr)