import matplotlib.pyplot as plt
from fft import ifft_Mix
import numpy as np
from scipy.io import wavfile

def slice(li):
    if li[0]>0:
        print("start up")
        print(li[0])
        n=1
        while li[n]>0:
            print(li[n])
            n+=1
        print(n,li[n])
        li=li[n:]
    elif li[0]<0:
        print("start dn")
        print(li[0])
        n=1
        while li[n]<0:
            print(li[n])
            n+=1
        print(n,li[n])
        li=li[n:]
    if li[-1]>0:
        print("end up")
        print(li[0])
        n=-2
        while li[n]>0:
            print(li[n])
            n-=1
        print(n,li[n])
        li=li[:n]
    elif li[-1]<0:
        print("end dn")
        print(li[0])
        n=-2
        while li[n]<0:
            print(li[n])
            n-=1
        print(n,li[n])
        li=li[:n]
    return li

x,f,sig,tm=ifft_Mix()
fig = plt.figure()

ax_1 = fig.add_subplot(221)
ax_2 = fig.add_subplot(222)
ax_3 = fig.add_subplot(223)
ax_4 = fig.add_subplot(224)


N=len(sig)
ax_3.plot(tm, sig)
ax_4.plot(f[0:N//2], np.abs(x[0:N//2])/N)


ifft_itm=np.fft.ifft(x)
ax_1.plot(tm,ifft_itm)
file_name="out.wav"
lss= np.tile(ifft_itm.real, 1)
wave = (lss* float(2 ** 15 - 1)).astype(np.int16) 
wavfile.write(file_name,44100, wave)

exq=slice(ifft_itm.real)
print("fin")
print(len(exq))
lss=np.tile(exq, 200)
wave = (lss* float(2 ** 15 - 1)).astype(np.int16) 
file_name="out100.wav"
wavfile.write(file_name,44100, wave)

ifft_itm=np.fft.ifft(x.real)
ax_2.plot(tm,ifft_itm)
file_name="out10.wav"
lss= np.tile(ifft_itm.real, 10)
wave = (lss* float(2 ** 15 - 1)).astype(np.int16) 
wavfile.write(file_name,44100, wave)

plt.show()
