# Create a python program capable of greeting a user based on the time of day.
# The program should use the time module to get the current hour (in 24-hour format).
# Based on the hour provided, the program should greet the user with "Good morning", "Good afternoon", or "Good evening".

import time
current_time=time.localtime() # Gets the current local time.
print("Current hour:", current_time.tm_hour) # current_time.tm_hour prints the current hour.

hour = current_time.tm_hour
if (hour>=0 and hour<6):
    print("Good Midnight!")
elif (hour>=6 and hour<12):
    print("Good Morning!")
elif(hour>=12 and hour<15):
    print("Good Noon!")
elif(hour>=15 and hour<17):
    print("Good Afternoon!")
elif(hour>=17 and hour<20):
    print("Good Evening!")
else:
    print("Good Night!")