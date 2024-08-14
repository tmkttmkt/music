from Sinse import *

import matplotlib.pyplot as plt
k=kyok(44100,file_name="kyudesu")
w1=k.create_onp(2)

lis=[Sin(f("C3"),0.8),Nok(f("C3")/2,0.2),Tan(f("C3")/3,0.6)]
w1.wave_function=Sin(f("C3"),0.8)#Wavelist(lis,0.5,siki="+")
print(f("C3"))
w2=Ifft(w1.fft(),v=0.5)
plt.plot(w1.fft(), color='orange')
plt.show()

k.play([w1,w2])
k.write([w1,w2])