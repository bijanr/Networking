import matplotlib.pylab as plt
import webbrowser
from graycode_generator import *
x = []
y = []
bit = int(input("Enter the bitstream: "))
bitmax = int(bit/4)
bitmin = bitmax - (2 * bitmax) 
i = bitmin + 1
while(i<bitmax):
    j = bitmin + 1
    while(j<bitmax):
        x.append(i)
        y.append(j)
        j += 2
    i += 2
f = plt.figure()
plt.scatter(x,y)
plt.plot([0,0], [bitmin, bitmax])
plt.plot([bitmin, bitmax], [0,0] )
figu = "Qam graph.svg"
plt.savefig(figu)
webbrowser.open(figu)