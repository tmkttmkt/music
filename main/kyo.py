from sinse import *
import matplotlib.pyplot as plt
#C→G→Am→Em→F→C→F→G
k=kyok(44100,file_name="kyokudesu")



w1=k.create_onp(2)
w1.nok(f("C4"),0.1)
kv=k.create_onp(0.5)
w2=k.create_onp(2)
w2.harmonic(w2.nok,f("C4"),0.1)

k.play([w1,kv,w2])


plt.plot(w2.wave[:w2.wave.__len__()//100], label="Waveform")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.title("Waveform of the WAV file")
plt.legend()
plt.show()