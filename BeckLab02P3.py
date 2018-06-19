T = 1.08   # tax for each day
F = 5.00 # one time fee
R = 100  # room rate
d = int(input("Enter the number of days stayed at the hotel "))
c = 0  # initialize cost variable
if (d > 0):        # days > 0
    # calculations here to compute the solution
    c = T*(R*d) + F   
    print(" the cost for ", d, " days  is  ", c )
else:    # here m is <= 300           # s <= 0
    print(" Invalid entry for days ", d )