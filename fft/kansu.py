import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
import librosa


def extend_waveform(data, extension_factor):
    # 波形の延長線上にデータを配置
    extended_data = np.concatenate([data] * extension_factor)
    return extended_data*extension_factor

def crossfade(data1, data2, fade_duration,sample_rate):
    fade_samples = int(fade_duration * sample_rate)
    fade = np.linspace(0, 1, fade_samples)

    # クロスフェード適用
    data1[-fade_samples:] *= 1 - fade
    data2[:fade_samples] *= fade

    return data1 + data2
def generate_infinite_wavefile(input_file_path, output_file_path, extension_factor=100):
    # wavファイルの読み込み
    #sample_rate, data = wavfile.read(input_file_path)
    data,sample_rate = librosa.load(input_file_path)

    # フーリエ変換
    fft_result = np.fft.fft(data)
    fft_freqs = np.fft.fftfreq(len(fft_result), 1/sample_rate)

    # フーリエ変換の結果を逆変換して新しい音声データを生成
    new_data = np.fft.ifft(fft_result).real

    # 波形の延長線上にデータを配置
    infinite_data = extend_waveform(new_data, extension_factor)
    fade_duration=0.1
    fade_samples = int(fade_duration * sample_rate)
    infinite_data = crossfade(infinite_data[:-fade_samples], infinite_data[fade_samples:], fade_duration,sample_rate)
    wave = (infinite_data* float(2 ** 15 - 1)).astype(np.int16) 
    wavfile.write(output_file_path,44100, wave)

    # フーリエ変換の結果を可視化
    plt.plot(fft_freqs, np.abs(fft_result))
    plt.title('Fourier Transform')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.show()

# 使用例
input_file_path = 'Mixdown.wav'
output_file_path = 'output_file.wav'
generate_infinite_wavefile(input_file_path, output_file_path, extension_factor=2)
