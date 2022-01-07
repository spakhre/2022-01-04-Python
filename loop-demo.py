for i in range(4):
    print(i)

## output with space in one line
for x in range(10):
    print(x, end=",")

for z in range(10):
    print(z)

fruitbowl = ["apple", "pear", "grapes"]
for fruit in fruitbowl:
    print(fruit)

## direct our output to an external file. The output of the print function is send to the standard output stream (sys.stdout) by default.
foo = open("ourfile.txt","w")
for fruit in fruitbowl:
    print(fruit, file=foo)

foo.close()

#!/usr/bin/env python3


# create the list called vendors
vendors = ["cisco", "juniper", "big_ip", "f5", "arista"]
# loop across the list vendors
for x in vendors:
    print("The vendor is:" + x)  # each time through the loop print value of x
print("\nOur loop has ended.")  # when the loop ends print this




# create a list of strings
vendors = ["cisco", "juniper", "big_ip", "f5", "arista", "alta3", "zach", "stuart"]
# create a second list of strings
approved_vendors = ["cisco", "juniper", "big_ip"]
# loop across the list called vendors
for x in vendors:
    print("\nThe vendor is " + x, end="")   # newline, print current vendor, and end without newline
    if x not in approved_vendors:   # if x does not appear within the list approved_vendors
        print(" - NOT AN APPROVED VENDOR!", end="")
print("\nOur loop has ended.") # print when loop has finished

#!/usr/bin/python3
"""RZFeeser | Alta3 Research
   Printing dictionary data stored as lists to the screen"""


def main():
    """On this farm there was a..."""

    # this is the data we want to loop across
    # it is a list containing 3 dictionaries
    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]


    # each time through the loop
    # farm will be equal to one of the dict within the list "farms"
    for farm in farms:
        #print(farm)   # this might be a good "first step" after developing the loop
        print(farm.get("name", "Unknown Farm"), end=":\n")  # this is like saying, "farm['name']"
                                                 # only it will not return an error
        for agri in farm.get("agriculture"):     # from a single "farm" get the list from the key "agriculture"
            print("  -", agri)                   # each time through the list "agriculture", print out an item

if __name__ == "__main__":
    main()
