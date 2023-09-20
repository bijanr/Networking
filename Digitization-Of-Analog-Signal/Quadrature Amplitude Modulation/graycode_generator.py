import math
binary_list = []
binary_sequence = []
gray_code = []
gray_first = []
gray_second = []

lim = 0
def Binary_Generator(bit_length):
    bin_lim = math.sqrt(bit_length) # finding the max digit in the binary series
    for i in range(bit_length):
        binary_list.append(format(i,'b'))
    
#appending bits from front using Divide and C0nquer Approach
#th number of divisions is equal to the bits appended
def Append_Binary(bit_length):
    bit = bit_length/2
    i = 0
    count = 1
    while(bit > 1):
        count = count +1
        for i in range(int(bit)):
            # appending the list with 0
            binary_list[i] = "0" + binary_list[i]
        bit = bit//2

    for i in range(bit_length):
            binary_sequence.append(list(map(int, str(binary_list[i]))))     # converting the numbers into 2d list
    lim = len(binary_sequence[i])
    Gray_Code(bit_length,lim)



# converting binary sequence into greycode

def xor_c(a,b):
    pass

def Gray_Code(bit_length, lim):
    for i in range(bit_length):
        xor_list = []
        xor_list.append(binary_sequence[i][0])
        for j in range(1,lim):
            xor_list.append(int(xor_c(binary_sequence[i][j-1], binary_sequence[i][j])))
        gray_code.append(xor_list)  
    Split(bit_length)
               
               
def xor_c(a,b):
    return '0' if(a == b) else '1'

def Split(bit_length):
    limit = int(len(gray_code[1])/2)
    for i in range(len(gray_code)):
        j = 0
        gray_f = []
        gray_s = []
        while(j<limit):
            gray_f.append(gray_code[i][j])
            gray_s.append(gray_code[i][j+limit])
            j += 1
        gray_first.append(gray_f)
        gray_second.append(gray_s)
    
    

    
