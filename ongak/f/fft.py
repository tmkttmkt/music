
import numpy as np
import librosa
def ifft_Mix():
    # 音楽ファイルのパス
    file_path = 'Mixdown.mp3'
    # 音楽ファイルの読み込み（yは音声データ、srはサンプリングレート）
    y, sr = librosa.load(file_path)

    # NumPy配列に変換
    sig = np.array(y)


    # チャンネルが2 （ステレオ) の場合，交互にデータが入っているので，二つおきに読み出す。
    # ただし，今回の場合はモノラルのはず。つまり，sounds.channels = 1

    dt = 1.0/44100 # サンプリング時間

    # 時間アレイを作る
    tms = 0.0 # サンプル開始時間を0にセット
    tme = sig.shape[0] # サンプル終了時刻
    tm = np.linspace(tms, tme, len(sig), endpoint=False) # 時間ndarrayを作成

    # DFT
    N = len(sig)
    x = np.fft.fft(sig)
    f = np.fft.fftfreq(N, dt) # xのindexに対応する周波数のndarrayを取得
    return x,f,sig,tm

def show(x):
    print(len(x))
    M=len(x)
    print()
    n=0
    while n<2:
        print(x[M//2-n],x[M//2+n])
        n+=1
    print()
    n=0
    while n<2:
        print(x[n],x[-1-n])
        n+=1
    print()
