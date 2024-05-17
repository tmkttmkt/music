from sinse import *

k=kyok(44100,file_name="kyokudesu")
w0=k.create_onp(1.5)
w0.sin(f("F3"),0.25)
w0.sin(f("A3"),0.25)
w0.sin(f("C4"),0.25)
w0.sin(f("E4"),0.25)

w1=k.create_onp(1)
w1.sin(f("A3"),0.1)
w1.sin(f("C4"),0.1)
w1.sin(f("E4"),0.1)

w2=k.create_onp(1)
w2.sin(f("C4"),0.1)
w2.sin(f("E4"),0.1)
w2.sin(f("G4"),0.1)

w3=k.create_onp(1)
w3.sin(f("E4"),0.1)
w3.sin(f("G4"),0.1)
w3.sin(f("B4"),0.1)

w4=k.create_onp(2)
w4.sin(f("C4"),0.1)
w4.sin(f("E4"),0.1)
w4.sin(f("G4"),0.1)

ky=k.create_onp(1)

w5=k.create_onp(1.5)
w5.sin(f("A4"),0.05)
w5.sin(f("C5"),0.05)
w5.sin(f("E5"),0.05)

waon=k.create_track(0,[w0,w1,w2,w3,w4,w5])

l1=k.create_onp(1)
l1.nok(f("A4"),0.2)

l2=k.create_onp(1)
l2.nok(f("G4"),0.2)

l3=k.create_onp(1)
l3.nok(f("B4"),0.2)

l4=k.create_onp(1)
l4.nok(f("C5"),0.2)

s1=k.create_onp(0.25)
s1.tan(f("A4"),0.2)
s2=k.create_onp(1)
s2.nok(f("G4"),0.2)
s3=k.create_onp(0.25)
s3.tan(f("A4"),0.2)
s4=k.create_onp(1)
s4.nok(f("B4"),0.2)

merody1=k.create_track(1.5,[l1,l2,l3,l4])
merody2=k.create_track(4.7,[s1,s2,s3,s4])

k.play_waves([waon,merody1,merody2])
k.write_waves([waon,merody1,merody2])