import matplotlib.pyplot as plt
import numpy as np
from plot import *

def Exit():
    print('Invalid binary string! ')

string = input('Enter the Binary string : ')
length = len(string)
binary_list = [int(i) for i in string]
n = 5
nrz_i = []  #nrzl graph
current_level = 0
for bit in string:
    current_level ^= int(bit)
    nrz_i.append(current_level)
print(nrz_i)

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

if not all(bit in '01' for bit in string):
    Exit()
    exit()
else:
    Plot(nrz_i, n, minfreq, maxfreq, minamp, maxamp)      # plots function if the number is binary
    exit(0)
