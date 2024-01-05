def nrz_i_encoding_4ary(data):
    encoded_signal = []
    current_level = 0  # Initial signal level

    for bit in data:
        current_level ^= int(bit)  # XOR operation to invert the level for 1, leave unchanged for 0
        encoded_signal.append(current_level)

    return encoded_signal

def main():
    data = input("Enter binary data (e.g., 101010): ")
    
    # Validate input
    if not all(bit in '01' for bit in data):
        print("Invalid input. Please enter binary data.")
        return

    # Perform 4-ary NRZ-I encoding
    encoded_signal = nrz_i_encoding_4ary(data)

    print("Input Binary Data:", data)
    print("4-ary NRZ-I Encoded Signal:", encoded_signal)

if __name__ == "__main__":
    main()
