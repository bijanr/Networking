import matplotlib.pyplot as plt
import numpy as np
from plot import *

def Exit():
    print('Invalid binary string! ')



string = input('Enter the Binary string : ')
length = len(string)
binary_list = [int(i) for i in string]
n = 5
for i in range(len(binary_list)):
    if(binary_list[i] == 0 or binary_list[i] == 1 ):
        Plot(string, n)      # plots function if the number is binary
        break
    else:
        Exit()  #exits if the integer is non binary
        break
        


        










