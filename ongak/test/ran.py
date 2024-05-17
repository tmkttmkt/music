from sinse import *
from random import randint

HAN={
    0:0.0625,
    1:0.125,
    2:0.25,
    3:0.5,
    4:1,
}

rate = 44100     
k=kyok(rate)
n=10
lis=[]
while n>0:
    o=k.create_onp(HAN[randint(0,4)])
    o.sin(nf(randint(0,6)+7*4),0.5)
    lis.append(o)
    n-=randint(0,1)
k.play(lis)