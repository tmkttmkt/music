import matplotlib.pyplot as plt
import numpy as np
from scipy import fftpack
from scipy.io import wavfile
from fft import ifft_Mix
#x=np.concatenate([x,np.zeros(44100*1-x.shape[0])])
x,f,sig,tm=ifft_Mix()
fig = plt.figure()

ax_1 = fig.add_subplot(231)
ax_2 = fig.add_subplot(232)
ax_3 = fig.add_subplot(233)
ax_4 = fig.add_subplot(234)
ax_5 = fig.add_subplot(235)
ax_6 = fig.add_subplot(236)

N=len(sig)
ax_3.plot(tm, sig)
#ax_3.set_title("moto", color="black")
ax_4.plot(f[0:N//2], np.abs(x[0:N//2])/N)
#ax_4.set_title("fft", color="black")

ifft_time1 = np.fft.ifft(x,len(sig))
tme = ifft_time1.shape[0] # サンプル終了時刻
tm = np.linspace(0.0, tme, len(ifft_time1), endpoint=False) 
ax_1.plot(tm,ifft_time1)
file_name="outfile1.wav"
lss= np.tile(ifft_time1.real, 1)
wave = (lss* float(2 ** 15 - 1)).astype(np.int16) 
wavfile.write(file_name,44100, wave)

ifft_time1 = np.fft.ifft(x,len(tm)*10)
print(ifft_time1[-100:])
tme = ifft_time1.shape[0] # サンプル終了時刻
tm = np.linspace(0.0, tme, len(ifft_time1), endpoint=False) 
ax_2.plot(tm,ifft_time1)
file_name="outfile2.wav"
lss= np.tile(ifft_time1.real, 1)
wave = (lss* float(2 ** 15 - 1)).astype(np.int16) 
wavfile.write(file_name,44100, wave)

ifft_time1 = np.fft.ifft(x,len(tm)*10,axis=0)
print(ifft_time1[-100:])
tme = ifft_time1.shape[0] # サンプル終了時刻
tm = np.linspace(0.0, tme, len(ifft_time1), endpoint=False) 
ax_5.plot(tm,ifft_time1)
file_name="outfile3.wav"
lss= np.tile(ifft_time1.real, 1)
wave = (lss* float(2 ** 15 - 1)).astype(np.int16) 
wavfile.write(file_name,44100, wave)

plt.show()

"""
"backward", "ortho", "forward","backward", "forward"
"""
