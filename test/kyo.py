from main.sinse import *
#C→G→Am→Em→F→C→F→G
k=kyok(44100,file_name="kyokudesu")



w1=k.create_onp(2)
w1.sin(f("C4"),0.1)
w1.sin(f("E4"),0.1)
w1.sin(f("G4"),0.1)

w2=k.create_onp(2)
w2.sin(f("G3"),0.1)
w2.sin(f("B3"),0.1)
w2.sin(f("D4"),0.1)

w3=k.create_onp(2)
w3.sin(f("A3"),0.1)
w3.sin(f("C4"),0.1)
w3.sin(f("E4"),0.1)

w4=k.create_onp(2)
w4.sin(f("E3"),0.15)
w4.sin(f("G3"),0.15)
w4.sin(f("B3"),0.15)

w5=k.create_onp(2)
w5.sin(f("F3"),0.2)
w5.sin(f("A3"),0.2)
w5.sin(f("C4"),0.2)

w6=k.create_onp(2)
w6.sin(f("C3"),0.2)
w6.sin(f("E3"),0.2)
w6.sin(f("G3"),0.2)

w7=k.create_onp(2)
w7.sin(f("F3"),0.2)
w7.sin(f("A3"),0.2)
w7.sin(f("C4"),0.2)

w8=k.create_onp(2)
w8.sin(f("G3"),0.2)
w8.sin(f("B3"),0.2)
w8.sin(f("D4"),0.2)


waon=k.create_track(0,[w1,w2,w3,w4,w5,w6,w7,w8],name="waon")

m1=k.create_onp(1)
m1.nok(f("A4"),0.07)

m2=k.create_onp(0.5)
m2.nok(f("B4"),0.07)

m2d=k.create_onp(0.5)
m2d.nok(f("C5"),0.07)

m3=k.create_onp(1)
m3.nok(f("E5"),0.07)

m4=k.create_onp(1)
m4.nok(f("F5"),0.07)

m5=k.create_onp(1)
m5.nok(f("E5"),0.07)

m6=k.create_onp(1)
m6.nok(f("G5"),0.07)

m7=k.create_onp(1)
m7.nok(f("D5"),0.07)

m8=k.create_onp(2)
m8.nok(f("C5"),0.07)

st9=k.create_onp(0.5)

m9=k.create_onp(0.5)
m9.nok(f("A4"),0.07)

m10=k.create_onp(0.5)
m10.nok(f("B4"),0.07)

m10d=k.create_onp(0.5)
m10d.nok(f("C5"),0.07)


m11=k.create_onp(1)
m11.nok(f("E5"),0.07)

m12=k.create_onp(1)
m12.nok(f("D5"),0.07)

m13=k.create_onp(1)
m13.nok(f("E5"),0.07)

m14=k.create_onp(1)
m14.nok(f("F5"),0.07)

m15=k.create_onp(1)
m15.nok(f("G5"),0.07)

m16=k.create_onp(1)
m16.nok(f("E5"),0.07)

merody=k.create_track(0,[m1,m2,m2d,m3,m4,m5,m6,m7,m8,m10,m10d,m11,m12,m13,m14,m15,m16],name="merod")

k.play_waves([waon,merody])
k.write_waves([merody])