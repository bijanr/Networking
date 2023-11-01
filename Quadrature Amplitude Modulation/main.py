from qam_list import *
bit_length = int(input('Enter the n-bit QAM: '))
def Split():
    pass
Binary_Generator(bit_length)
Append_Binary(bit_length)
Plotting(bit_length)


print("Binary" + "                  " + "Gray" )
for i in range(bit_length):
    for j in range(len(gray_code[i])):
        print(binary_sequence[i][j], end='' )
    print(end='                      ')
    for j in range(len(gray_code[i])):
        print(gray_code[i][j], end='' )
        
    print('')

print("The Signal Space Coordinates : ")
for i in range(len(x)):
    print(f"( ", end = '')
    j = 0
    k = 0
    while(j<len(gray_first[1])):
        print(f"{gray_first[i][j]}", end = '')
        j += 1
    print(f", ", end = '')
    while(k<len(gray_second[1])):
        print(f"{gray_second[i][k]}", end = '')
        k += 1
    print(f" )      ", end = '')
    print(f"( {x[i]} , {y[i]} ) ")