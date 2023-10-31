***RUN THE MAIN.PY FILE***



INITIALISATION
    string : the binary stream
    binary_list[] : the binary stream in integer array
    length : the length of binary stream
    n : voltage limit

WORKING 
    volt_list[] : the binary stream in voltage array form
    square_list[] : (usually the y axis) manipulating volt_list in graph form depending on the respective time
    time_list[] : the limiting time for the square_list[]
    rand_noise[] : (usually the y axis) manipulating volt_list in graph FOR NOISE form depending on the respective time
    noise_time[] : the limiting time for rand_noise[]

main.py : all the functions called
plot.py : algorithm for plotting the graph of high vs low signals
noise.py : inserts noise inside the graph
graph.py : main matplotlib code to execute and print all the graphs using the lists from plot.py and noise.py
decoding.py : decodes the graph with noise and finds the error percentage