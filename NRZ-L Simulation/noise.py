from graph import *
from decoding import *
import random

def NoiseGen(volt_list, n, string, minfreq, maxfreq, minamp, maxamp):

    
    
    frequency = []
    noise_time = []
    for i in range(len(volt_list)):     # random frequency for each bits generator
        if(volt_list[i] == n):
            frequency.append(random.randint(minfreq,maxfreq))
        else:
            frequency.append(random.randint(minfreq,maxfreq) * -1)
            
    rand_noise = []
    count = []
    for i in range(len(frequency)):   # random noise values based upon each frequency
        temp = 0
        sum = 0
        if(frequency[i] < 0):
            for j in range(abs(frequency[i])):
                temp = random.uniform(minamp, maxamp * -1)
                rand_noise.append(temp)
                sum += temp
                temp = 0
            count.append(sum)
            sum = 0
        else:
            for j in range(abs(frequency[i])):
                temp = random.uniform(minamp, maxamp)
                rand_noise.append(temp)
                sum += temp
                temp = 0
            count.append(sum)
            sum = 0
    inc = 0
    i = 0
    while(i < (len(rand_noise)-1) ):    # time generator
        if((rand_noise[i] > 0 and rand_noise[i+1] > 0) or (rand_noise[i] < 0 and rand_noise[i+1] < 0) ):
            noise_time.append(inc)
            inc = inc + 1
            i = i + 1
        elif((rand_noise[i] > 0 and rand_noise[i+1] < 0) or (rand_noise[i] < 0 and rand_noise[i+1] > 0) ):
            noise_time.append(inc)
            noise_time.append(inc)
            i = i + 2
            inc = inc + 1
    
    noise_time.append(inc)

    ErrorPercentage(rand_noise,  volt_list, count)
    Graph_Gen_Noise(rand_noise, noise_time, string)

    
    
    
    