import matplotlib.pyplot as plt
import numpy as np
from plot import *

def Exit():
    print('Invalid binary string! ')

string = input('Enter the Binary string : ')
length = len(string)
binary_list = [int(i) for i in string]
n = 5

choice = input("Press 1 for heavy noise and 2 for low noise : ")
if(choice == '1'):
    maxfreq = 11
    minfreq = 5
    maxamp = 6
    minamp = -4
elif(choice == '2'):
    maxfreq = 10
    minfreq = 3
    maxamp = 6
    minamp = -2
else:
    print("Wrong choice! Default noise generated.")
    maxfreq = 10
    minfreq = 3
    maxamp = 6
    minamp = -2 

for i in range(len(binary_list)):
    if(binary_list[i] == 0 or binary_list[i] == 1 ):
        Plot(string, n, minfreq, maxfreq, minamp, maxamp)      # plots function if the number is binary
        break
    else:
        Exit()  #exits if the integer is non binary
        break