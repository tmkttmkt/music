import librosa
import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf


y, sr = librosa.load('wav\\gou.wav')
D = np.abs(librosa.stft(y))
print(D.shape)

S_db = librosa.amplitude_to_db(D)


#"""# スペクトログラムのプロット
plt.figure(figsize=(10, 6))
librosa.display.specshow(S_db, sr=sr, x_axis='time', y_axis='log',cmap='viridis')
plt.colorbar(format='%+2.0f dB')
plt.title('STFT Spectrogram')
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.show()
#"""
y_reconstructed = librosa.istft(D)

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