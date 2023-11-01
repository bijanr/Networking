import matplotlib.pylab as plt
import webbrowser
from graycode_generator import *

x = []
y = []
def Plotting(bit_length):
    
    bit = bit_length
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
    ax = plt.axes()
    plt.scatter(x,y)
    plt.plot([0,0], [bitmin, bitmax])
    plt.plot([bitmin, bitmax], [0,0] )

    plt.suptitle("Quadrature Amplitude Modulation")
    plt.title(f"Binary String : {(bit)}",fontsize='large', loc='left', fontweight='bold', style = 'italic', family='monospace')
    ax.set_xticks(x)
    ax.set_yticks(y)
    figure = "N-Bit-QAM.svg"
    plt.savefig(figure)
    webbrowser.open(figure)
