#!/usr/bin/env python3

message = "Based on your wind speed. You are in "

##Built based on m/s
wind_speed = int(input("What is the current windSpeed?"))

#
if wind_speed >= 70:
    message = message + 'Category 5.'
elif 58 <= wind_speed <= 69:
    message = message + 'Category 4.'
elif 50 <= wind_speed <= 57:
    message = message + 'Category 3.'
elif 43 <= wind_speed <= 49:
    message = message + 'Category 2.'
elif 33 <= wind_speed <= 42:
    message = message + 'Category 1.'
else:
    message = 'Wind speed is less than 32.'
print(message)
