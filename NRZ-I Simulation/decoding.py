def ErrorPercentage(rand_noise,  volt_list, count):
    
    
    decoded_binary = []
    for i in range(len(count)):
        if(count[i] >0):
            decoded_binary.append(1)
        elif(count[i] <0):
            decoded_binary.append(0)
    encoded_binary = []
    for i in range(len(volt_list)):
        if(volt_list[i] > 0):
            encoded_binary.append(1)
        elif(volt_list[i] < 0):
            encoded_binary.append(0)
    print(f"The original bitstream( NRZ-I): {(encoded_binary)}")
    print(f"The recieved bitstream( NRZ-I): {(decoded_binary)}")

    error = 0
    for i in range(len(encoded_binary)):
        if(encoded_binary[i] != decoded_binary[i]):
            error += 1
    
    percentage = ( error / len(encoded_binary) ) * 100
    print(f"Error percentage = {(percentage)}")
