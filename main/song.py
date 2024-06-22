from sinse import *
import numpy as np
k=kyok(file_name="dension2g")
base1=k.create_track(0,[])
base1v=0.1
base1.append(k.create_onp(0.5).tan(f("C3"),base1v*2,windf=np.hamming))
base1.append(k.create_onp(0.5).tan(f("C3"),base1v,windf=np.hamming))
base1.append(k.create_onp(0.5).tan(f("D3"),base1v,windf=np.hamming))
base1.append(k.create_onp(0.5).tan(f("D3"),base1v,windf=np.hamming))
base1.append(k.create_onp(0.5).tan(f("E3"),base1v,windf=np.hamming))
base1.append(k.create_onp(0.5).tan(f("E3"),base1v,windf=np.hamming))
base1.append(k.create_onp(0.5).tan(f("C3"),base1v,windf=np.hamming))
base1.append(k.create_onp(0.5).tan(f("C3"),base1v,windf=np.hamming))

base2=k.create_track(0,[])
base2v=0.1
base2.append(k.create_onp(0.5).tan(f("C4"),base1v*2,windf=np.hamming))
base2.append(k.create_onp(0.5).tan(f("C4"),base1v,windf=np.hamming))
base2.append(k.create_onp(0.5).tan(f("D4"),base1v,windf=np.hamming))
base2.append(k.create_onp(0.5).tan(f("D4"),base1v,windf=np.hamming))
base2.append(k.create_onp(0.5).tan(f("E4"),base1v,windf=np.hamming))
base2.append(k.create_onp(0.5).tan(f("E4"),base1v,windf=np.hamming))
base2.append(k.create_onp(0.5).tan(f("C4"),base1v,windf=np.hamming))
base2.append(k.create_onp(0.5).tan(f("C4"),base1v,windf=np.hamming))

base3=k.create_track(0,[])
base3v=0.9
base3.append(k.create_onp(0.5).sintan(f("C2"),base1v*2,windf=np.hamming))
base3.append(k.create_onp(0.5).sintan(f("C2"),base1v,windf=np.hamming))
base3.append(k.create_onp(0.5).sintan(f("D2"),base1v,windf=np.hamming))
base3.append(k.create_onp(0.5).sintan(f("D2"),base1v,windf=np.hamming))
base3.append(k.create_onp(0.5).sintan(f("E2"),base1v,windf=np.hamming))
base3.append(k.create_onp(0.5).sintan(f("E2"),base1v,windf=np.hamming))
base3.append(k.create_onp(0.5).sintan(f("C2"),base1v,windf=np.hamming))
base3.append(k.create_onp(0.5).sintan(f("C2"),base1v,windf=np.hamming))

mero1=k.create_track(0,[])
merov=0.2
mero1.append(k.create_onp(0.5).nok(f("C5"),merov,windf=np.hamming))
mero1.append(k.create_onp(0.25).nok(f("B5"),merov,windf=np.hamming))
mero1.append(k.create_onp(0.25).nok(f("C5"),merov,windf=np.hamming))

mero1.append(k.create_onp(0.25).nok(f("D5"),merov,windf=np.hamming))
mero1.append(k.create_onp(0.25).nok(f("B5"),merov,windf=np.hamming))
mero1.append(k.create_onp(0.5).nok(f("A5"),merov,windf=np.hamming))

mero1.append(k.create_onp(0.25).nok(f("E5"),merov,windf=np.hamming))
mero1.append(k.create_onp(0.5).nok(f("D5"),merov,windf=np.hamming))
mero1.append(k.create_onp(0.25).nok(f("C5"),merov,windf=np.hamming))

mero1.append(k.create_onp(0.5).nok(f("C5"),merov,windf=np.hamming))
mero1.append(k.create_onp(0.25).nok(f("E5"),merov,windf=np.hamming))
mero1.append(k.create_onp(0.25).nok(f("D5"),merov,windf=np.hamming))


mero2=k.create_track(0,[])
mero2.append(k.create_onp(0.5).sin(f("C5"),merov,windf=np.hamming))
mero2.append(k.create_onp(0.25).sin(f("B5"),merov,windf=np.hamming))
mero2.append(k.create_onp(0.25).sin(f("C5"),merov,windf=np.hamming))

mero2.append(k.create_onp(0.25).sin(f("D5"),merov,windf=np.hamming))
mero2.append(k.create_onp(0.25).sin(f("B5"),merov,windf=np.hamming))
mero2.append(k.create_onp(0.5).sin(f("A5"),merov,windf=np.hamming))

mero2.append(k.create_onp(0.25).sin(f("E5"),merov,windf=np.hamming))
mero2.append(k.create_onp(0.5).sin(f("D5"),merov,windf=np.hamming))
mero2.append(k.create_onp(0.25).sin(f("C5"),merov,windf=np.hamming))

mero2.append(k.create_onp(0.5).sin(f("C5"),merov,windf=np.hamming))
mero2.append(k.create_onp(0.25).sin(f("E5"),merov,windf=np.hamming))
mero2.append(k.create_onp(0.25).sin(f("D5"),merov,windf=np.hamming))

mero3=k.create_track(0,[])
mero3.append(k.create_onp(0.5).tan(f("C5"),merov*1.5,windf=np.hamming))
mero3.append(k.create_onp(0.25).tan(f("B5"),merov*0.5,windf=np.hamming))
mero3.append(k.create_onp(0.25).tan(f("C5"),merov*0.5,windf=np.hamming))

mero3.append(k.create_onp(0.25).tan(f("D5"),merov*0.5,windf=np.hamming))
mero3.append(k.create_onp(0.25).tan(f("B5"),merov*0.5,windf=np.hamming))
mero3.append(k.create_onp(0.5).tan(f("A5"),merov*1.5,windf=np.hamming))

mero3.append(k.create_onp(0.25).tan(f("E5"),merov*0.5,windf=np.hamming))
mero3.append(k.create_onp(0.5).tan(f("D5"),merov*1.5,windf=np.hamming))
mero3.append(k.create_onp(0.25).tan(f("C5"),merov*0.5,windf=np.hamming))

mero3.append(k.create_onp(0.5).tan(f("C5"),merov*1.5,windf=np.hamming))
mero3.append(k.create_onp(0.25).tan(f("E5"),merov*0.5,windf=np.hamming))
mero3.append(k.create_onp(0.25).tan(f("D5"),merov*0.5,windf=np.hamming))
mero3.append(k.create_onp(2).tan(f("C5"),merov,windf=np.hamming))

k.play_waves([base1+base2+base3,mero1+mero2+mero3])
k.write_waves([base1+base2+base3,mero1+mero2+mero3])