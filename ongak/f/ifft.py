import matplotlib.pyplot as plt
import numpy as np
from scipy import fftpack
from scipy.io import wavfile
from fft import ifft_Mix,show
#x=np.concatenate([x,np.zeros(44100*1-x.shape[0])])
print()
x,f,sig,tm=ifft_Mix()
fig = plt.figure()

ax_1 = fig.add_subplot(221)
ax_2 = fig.add_subplot(222)
ax_3 = fig.add_subplot(223)
ax_4 = fig.add_subplot(224)

N=len(sig)
ax_3.plot(tm, sig)
ax_4.plot(f[0:N//2], np.abs(x[0:N//2]))

lis=np.zeros(100000)
z=np.concatenate([lis,x,lis])

show(z)
show(x)

ifft_time1 = np.fft.ifft(x,len(x))
tme = ifft_time1.shape[0] # サンプル終了時刻
tm = np.linspace(0.0, tme, len(ifft_time1), endpoint=False) 
ax_1.plot(tm,ifft_time1)
ax_1.set_title("Title", color="black")
file_name="outfile1.wav"
lss= np.tile(ifft_time1.real, 1)
wave = (lss* float(2 ** 15 - 1)).astype(np.int16) 
wavfile.write(file_name,44100, wave)

ifft_time1 = np.fft.ifft(z,len(z)*2)
tme = ifft_time1.shape[0] # サンプル終了時刻
tm = np.linspace(0.0, tme, len(ifft_time1), endpoint=False) 
ax_2.plot(tm,ifft_time1)
ax_2.set_title("Titlea", color="black")
file_name="outfile2.wav"
lss= np.tile(ifft_time1.real, 1)
wave = (lss* float(2 ** 15 - 1)).astype(np.int16) 
wavfile.write(file_name,44100, wave)

plt.show()

"""
"backward", "ortho", "forward","backward", "forward"
"""


print()
