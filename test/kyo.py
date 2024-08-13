from Sinse import *
#C→G→Am→Em→F→C→F→G
k=kyok(44100,file_name="kyudesu")



w1=k.create_onp(2)
w1.wave_function=Sin(f("A3"),0.8)
w1.window=ADSR_par(0.1,0.2,0.7,0.3)
w2=k.create_onp(2)
w2.wave_function=Sin(f("G3"),0.5)
w2.window=ADSR_par(0.1,0.2,0.7,0.3)

w3=k.create_onp(2)
w3.wave_function=Sin(f("A3"),0.4)
w3.window=ADSR_par(0.1,0.2,0.7,0.3)

w4=k.create_onp(2)
w4.wave_function=Sin(f("E3"),0.5)
w4.window=ADSR_par(0.1,0.2,0.7,0.3)

w5=k.create_onp(2)
w5.wave_function=Sin(f("F3"),0.6)
w5.window=ADSR_par(0.1,0.2,0.7,0.3)

w6=k.create_onp(2)
w6.wave_function=Sin(f("C3"),0.6)
w6.window=ADSR_par(0.1,0.2,0.7,0.3)

w7=k.create_onp(2)
w7.wave_function=Sin(f("F3"),0.5)
w7.window=ADSR_par(0.1,0.2,0.7,0.3)

w8=k.create_onp(2)
w8.wave_function=Sin(f("G3"),0.7)
w8.window=ADSR_par(0.1,0.2,0.7,0.3)

waon=k.create_track(0,[w1,w2,w3,w4,w5,w6,w7,w8])

m1=k.create_onp(1)
m1.wave_function=Nok(f("A4"),0.07)

m2=k.create_onp(0.5)
m2.wave_function=Nok(f("B4"),0.07)

m2d=k.create_onp(0.5)
m2d.wave_function=Nok(f("C5"),0.07)

m3=k.create_onp(1)
m3.wave_function=Nok(f("E5"),0.07)

m4=k.create_onp(1)
m4.wave_function=Nok(f("F5"),0.07)

m5=k.create_onp(1)
m5.wave_function=Nok(f("E5"),0.07)

m6=k.create_onp(1)
m6.wave_function=Nok(f("G5"),0.07)

m7=k.create_onp(1)
m7.wave_function=Nok(f("D5"),0.07)

m8=k.create_onp(2)
m8.wave_function=Nok(f("C5"),0.07)

st9=k.create_onp(0.5)

m9=k.create_onp(0.5)
m9.wave_function=Nok(f("A4"),0.07)

m10=k.create_onp(0.5)
m10.wave_function=Nok(f("B4"),0.07)

m10d=k.create_onp(0.5)
m10d.wave_function=Nok(f("C5"),0.07)


m11=k.create_onp(1)
m11.wave_function=Nok(f("E5"),0.07)

m12=k.create_onp(1)
m12.wave_function=Nok(f("D5"),0.07)

m13=k.create_onp(1)
m13.wave_function=Nok(f("E5"),0.07)

m14=k.create_onp(1)
m14.wave_function=Nok(f("F5"),0.07)

m15=k.create_onp(1)
m15.wave_function=Nok(f("G5"),0.07)

m16=k.create_onp(1)
m16.wave_function=Nok(f("E5"),0.07)

merody=k.create_track(0,[m1,m2,m2d,m3,m4,m5,m6,m7,m8,m10,m10d,m11,m12,m13,m14,m15,m16])

k.play_waves([waon,merody])
k.write_waves([merody])