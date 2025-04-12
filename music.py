from pysine import sine
sine(frequency=440.0, duration=1.0)
c = 260
d2 = 292
e3 = 328
f4 = 347
g5 = 390
a6 = 437
b7 = 491
c8 = 520

def Exes():
    sine(frequency=g5, duration=0.75)
    sine(frequency=f4, duration=0.25)
    sine(frequency=e3, duration=0.25)
    sine(frequency=c, duration=0.25)
    sine(frequency=c, duration=0.25)
    sine(frequency=d2, duration=0.25)
    sine(frequency=b7, duration=0.5)
    sine(frequency=b7, duration=0.5)
    sine(frequency=g5, duration=0.5)

Exes()
