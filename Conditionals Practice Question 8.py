# Smart Traffic Signal Helper

traffic_signal=input("Enter Traffic signal colour(Red/Yellow/Green):")
if(traffic_signal=="Red"):
    print("STOP! Do not proceed")
elif(traffic_signal=="Yellow"):
    speed=int(input("Enter your vehicle speed:"))
    if(speed>40):
        print("SLOW DOWN! Prepare to stop.")
    else:
        print("Proceed with Caution")
elif(traffic_signal=="Green"):
    print("G0! Clear to move")
else:
    print("Invalid Colour! Enter Red/Yellow/Green")