import matplotlib.pyplot as plt
import numpy as np

def Plot(string, n):
    volt_list = [(-n)*(-1)**int(i) for i in string]     # setting upper an lower voltages using the actual string
    print(f"the list is: {(volt_list)}")
    length  = int(len(volt_list))  # length of actual binary stream
    square_list = []
    for i in range(len(volt_list)-1):   # algorithm for voltage boundary plotting
        if(volt_list[i] == -n and volt_list[i+1] == n):
            for i in range(2):
                square_list.append(-n)
        elif(volt_list[i] == n and volt_list[i+1] == -n):
            for i in range(2):
                square_list.append(n)
        elif(volt_list[i] == n and volt_list[i+1] == n):
            for i in range(1):
                square_list.append(n)
        elif(volt_list[i] == -n and volt_list[i+1] == -n):
            for i in range(1):
                square_list.append(-n)
    
    if(volt_list[-1] == n):
        square_list.append(n)
    elif(volt_list[-1] == -n):
        square_list.append(-n)
    


    time_list = []
    counter  = 0
    i = 0
    while(i<(len(square_list)-1)):      # algorithm for time graph respective to the voltage graph
        if(square_list[i] == square_list[i+1]):
            time_list.append(counter)
            counter += 1
            i = i+1
        elif(square_list[i] != square_list[i+1]):
            time_list.append(counter)
            time_list.append(counter)
            i = i+2
            counter += 1
    # time_axis = [i for i in range(len(time_list))]

    ## matplotlib commands
    plt.xlabel('Time')
    plt.ylabel('Voltage')
    plt.title('Binary is : '+ string)
    originy = [0,0]
    olen = len(time_list)
    originx = [0,olen]
    plt.plot(originx, originy)
    # plt.plot(time_axis, square_list, marker = 'o')
    plt.plot(time_list, square_list, marker = 'o')  # plotting the graph
    plt.show()
    

    
    