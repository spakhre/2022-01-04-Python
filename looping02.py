#!/usr/bin/env python3

# open file in read mode - with avoids the need to of close() statement
with open("dnsservers.txt", "r") as dnsfile:

# create list of lines
    dnslist = dnsfile.readlines()

# loop over lines
    for svr in dnslist:
# print and end without a newline
        print(svr, end="")  # the line we read ALREADY contains a \n (newline)
print("\nend of with demo1\n----------------------")

# open file in read mode; avoids the need to create dnslist
with open("dnsservers.txt", "r") as dnsfile:
    # indent to keep the dnsfile object open
    # loop across the lines in the file
    for svr in dnsfile:    # we never created a list of lines to store in memory
        #print and end without a newline
        print(svr, end="")


# writes to 2 more files based on the domain
with open("dnsservers.txt", "r") as dnsfile:   # 'r' is read mode
    # indent to keep the dnsfile object open
    # loop across the lines in the file
    for svr in dnsfile:
        svr = svr.rstrip('\n') # remove newline char if exists
                               # would exists on all but last line
        # IF the string svr ends with 'org'
        if svr.endswith('org'):
            with open("org-domain.txt", "a") as srvfile:  # 'a' is append mode
                srvfile.write(svr + "\n")
        # ELSE-IF the string svr ends with 'com'
        elif svr.endswith('com'):
            with open("com-domain.txt", "a") as srvfile:  # 'a' is append mode
                srvfile.write(svr + "\n")
