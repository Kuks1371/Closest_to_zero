import math
import random

num_temp = int(input("Number of temperatures to analyze: "))
max_temp = input("Maximum limit temperature: ")
min_temp = input("Minimum limit temperature: ")
temperatures = [random.randint(int(min_temp), int(max_temp)) for x in range(num_temp)]
positive_temperatures = []
negative_temperatures = []
if num_temp > 0:
    for i in temperatures:
        t = int(i) 
        if t >= 0:
            positive_temperatures.append(t)
        else:
            negative_temperatures.append(t)
    print("All temperatures: " + str(temperatures))
    if len(positive_temperatures) > 0:
        positive_result = min(positive_temperatures)
    else:
        positive_result = math.inf
    if len(negative_temperatures) > 0:
        negative_result = max(negative_temperatures)
    else:
        negative_result = -math.inf
    if abs(negative_result) == positive_result:
        print("Temperature closest to 0: " + str(positive_result))
    elif abs(negative_result) < positive_result:
        print("Temperature closest to 0: " + str(negative_result))
    else:
        print("Temperature closest to 0: " + str(positive_result))   
else:
    print("Temperature closest to 0: 0")


