import cv2
import librosa
import numpy as np

# 音声ファイルの読み込み
y, sr = librosa.load('dension2g.wav')

# STFTの計算
n_fft = 2048
hop_length = 512
D = librosa.stft(y, n_fft=n_fft, hop_length=hop_length)

magnitude = np.flipud(np.abs(D))
# 振幅スペクトルを 0-255 の範囲にスケーリング
magnitude_db = librosa.amplitude_to_db(magnitude, ref=np.max)
magnitude_normalized = cv2.normalize(magnitude_db, None, 0, 255, cv2.NORM_MINMAX)
square_img = cv2.resize(magnitude_normalized, (magnitude_normalized.shape[1], magnitude_normalized.shape[1]))

# OpenCVで表示
cv2.imshow('Spectrogram', square_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 画像として保存
cv2.imwrite('spectrogram_image.png', square_img)
