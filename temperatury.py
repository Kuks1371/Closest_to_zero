import math
import random

num_temp = int(input("Number of temperatures to analyze: "))
max_temp = input("Maximum limit temperature: ")
min_temp = input("Minimum limit temperature: ")
temperatures = [random.randint(int(min_temp), int(max_temp)) for x in range(num_temp)]
#temperatures = [input() or import pandas; df = pandas.read_csv('filepath')]
#Here you can specify temperatures to search amongst, by simply using input() or reading from an outside file.
positive_temperatures = []
negative_temperatures = []

if num_temp > 0:
    for i in temperatures:
        if i >= 0:
            positive_temperatures.append(i)
        else:
            negative_temperatures.append(i)
    print("All temperatures: " + str(temperatures))
    if len(positive_temperatures) > 0:
        positive_result = min(positive_temperatures)
    else:
        positive_result = math.inf
    if len(negative_temperatures) > 0:
        negative_result = max(negative_temperatures)
    else:
        negative_result = -math.inf
    if abs(negative_result) == positive_result: #If a positive and negative temperature is equally close to zero,
        print("Temperature closest to 0: " + str(positive_result)) # then choose positive. 
    elif abs(negative_result) < positive_result:
        print("Temperature closest to 0: " + str(negative_result))
    else:
        print("Temperature closest to 0: " + str(positive_result))   
else:
    print("No temperatures given!")


