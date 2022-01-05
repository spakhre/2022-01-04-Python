#!/usr/bin/env python3

# create the string hostname
hostname = "MTG"
# test logic with the `if` statement
# what to do if this statement is found to be true
if hostname == "MTG":
    print("The hostname was found to be MTG")


#!/usr/bin/env python3
hostname = input("What value should we set for hostname?")
## Notice how the next line has changed
## here we use the str.lower() method to return a lowercase string
## if hostname.lower() == "mtg":
   ## print("The hostname was found to be mtg")
    ##print(hostname,  "matches the name")

print("exiting the program")



#!/usr/bin/env python3
ipchk = input("Apply an IP address: ") # this line now prompts the user for input

# if user set IP of gateway
if ipchk == "192.168.70.1":
   print("Looks like the IP address of the Gateway was set: " + ipchk + " This is not recommended.")
elif ipchk: # if any data is provided, this will test true
   print("Looks like the IP address was set: " + ipchk) # indented under if
else: # if data is NOT provided
   print("You did not provide input.") # indented under else

