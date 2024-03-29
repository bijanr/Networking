import matplotlib.pyplot as plt
import webbrowser
import os

def Graph_Generator(square_list, time_list, nrz_i):    #nrzl plotting without noise
    plt.xlabel('Time')
    plt.ylabel('Voltage')
    plt.title('Binary is : '+ str(nrz_i))
    ax = plt.axes()
    f = plt.figure()
    plt.plot(time_list, square_list, marker = 'o')  # plotting the graph
    

    plt.suptitle("NRZ-L without Noise")
    plt.title(f"Binary String : {str(nrz_i)}",fontsize='large', loc='left', fontweight='bold', style = 'italic', family='monospace')
    ax.set_xticks(time_list)
    ax.set_yticks(square_list)
    ax.set_xticklabels(time_list)
    ax.set_yticklabels(square_list)
    figure = "NRZ_L.svg"
    # path = os.path.abspath(__file__)
    # plt.savefig(os.path.join(path, figure))
    plt.savefig(figure)
    webbrowser.open(figure)


def Graph_Gen_Noise(rand_noise, noise_time, nrz_i):    #nrzl plotting with noise
    
    
    originy = [0,0]
    olen = len(noise_time)
    originx = [0,olen]
    ax2 = plt.axes()
    f = plt.figure()
    plt.plot(noise_time, rand_noise, marker = 'x')  # plotting the graph

    plt.xlabel('Time')
    plt.ylabel('Voltage')
    plt.suptitle("NRZ-L with Noise")
    plt.title(f"Binary String : {str(nrz_i)}",fontsize='large', loc='left', fontweight='bold', style = 'italic', family='monospace')
    ax2.set_xticks(noise_time)
    ax2.set_yticks(rand_noise)
    ax2.set_xticklabels(noise_time)
    ax2.set_yticklabels(rand_noise)
    figu = "NRZ_L_noise.svg"
    # path = os.path.abspath(__file__)
    # plt.savefig(os.path.join(path, figu)) 
    plt.savefig(figu)
    webbrowser.open(figu)
