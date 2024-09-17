from Sinse import *
import matplotlib.pyplot as plt
k=kyok()
num=np.array([[0,0.2],[0,0.2],[0,0.2],[0,0.2]])
ift=k.Istft(num)
plt.plot(ift.wave, color='orange')
plt.title('Reconstructed Audio Signal from iSTFT')
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.plot()