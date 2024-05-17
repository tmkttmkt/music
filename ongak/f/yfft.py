
import numpy as np
import librosa
import matplotlib.pyplot as plt
def fft_Mix(file):
    # 音楽ファイルのパス
    # 音楽ファイルの読み込み（yは音声データ、srはサンプリングレート）
    y, sr = librosa.load(file)

    # NumPy配列に変換
    sig = np.array(y)


    # チャンネルが2 （ステレオ) の場合，交互にデータが入っているので，二つおきに読み出す。
    # ただし，今回の場合はモノラルのはず。つまり，sounds.channels = 1

    dt = 1.0/44100 # サンプリング時間

    # 時間アレイを作る
    tms = 0.0 # サンプル開始時間を0にセット
    tme = sig.shape[0] # サンプル終了時刻
    print(len(sig)/44100,len(sig),file)
    tm = np.linspace(tms, tme, len(sig), endpoint=False) # 時間ndarrayを作成

    # DFT
    N = len(sig)
    x = np.fft.fft(sig)
    f = np.fft.fftfreq(N, dt) # xのindexに対応する周波数のndarrayを取得
    return x,f,sig,tm

x_a,f_a,sig_a,tm_a=fft_Mix("ymm\\aa.wav")
x_i,f_i,sig_i,tm_i=fft_Mix("ymm\\ii.wav")
x_u,f_u,sig_u,tm_u=fft_Mix("ymm\\uu.wav")
x_e,f_e,sig_e,tm_e=fft_Mix("ymm\\ee.wav")
x_o,f_o,sig_o,tm_o=fft_Mix("ymm\\oo.wav")
fig = plt.figure()
ax_1 = fig.add_subplot(3,5,1)
N=len(sig_a)
ax_1.plot(f_a[0:N//2], np.abs(x_a[0:N//2])/N)
ax_2 = fig.add_subplot(3,5,2)
N=len(sig_i)
ax_2.plot(f_i[0:N//2], np.abs(x_i[0:N//2])/N)
ax_3 = fig.add_subplot(3,5,3)
N=len(sig_u)
ax_3.plot(f_u[0:N//2], np.abs(x_u[0:N//2])/N)
ax_4 = fig.add_subplot(3,5,4)
N=len(sig_e)
ax_4.plot(f_e[0:N//2], np.abs(x_e[0:N//2])/N)
ax_5 = fig.add_subplot(3,5,5)
N=len(sig_o)
ax_5.plot(f_o[0:N//2], np.abs(x_o[0:N//2])/N)

ax_6 = fig.add_subplot(3,5,6)
ax_6.plot(tm_a,sig_a)
ax_7 = fig.add_subplot(3,5,7)
ax_7.plot(tm_i,sig_i)
ax_8 = fig.add_subplot(3,5,8)
ax_8.plot(tm_u,sig_u)
ax_9 = fig.add_subplot(3,5,9)
ax_9.plot(tm_e,sig_e)
ax_10 = fig.add_subplot(3,5,10)
ax_10.plot(tm_o,sig_o)

def ifft_item(x):
    ifft_itm=np.fft.ifft(x)
    tm = np.linspace(0.0, len(ifft_itm), len(ifft_itm), endpoint=False) 
    return tm,ifft_itm

ax_11 = fig.add_subplot(3,5,11)
tm_a,iff_a=ifft_item(x_a)
ax_11.plot(tm_a,iff_a)
ax_12 = fig.add_subplot(3,5,12)
tm_i,iff_i=ifft_item(x_i)
ax_12.plot(tm_i,iff_i)
ax_13 = fig.add_subplot(3,5,13)
tm_u,iff_u=ifft_item(x_u)
ax_13.plot(tm_u,iff_u)
ax_14 = fig.add_subplot(3,5,14)
tm_e,iff_e=ifft_item(x_e)
ax_14.plot(tm_e,iff_e)
ax_15 = fig.add_subplot(3,5,15)
tm_o,iff_o=ifft_item(x_o)
ax_15.plot(tm_o,iff_o)


plt.show()
