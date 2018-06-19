x = int(input("Enter the number of years "))
s= 0  # initialize seconds variable 

# this is a comment
#the following if...else structure is used to illustrate the syntax note the indentation
if (x >= 0):        # valid year input >= 0
    # calculations here to compute s with user input y 
    s = x*365*24*60*60
    print(" the number of seconds in ", x, " years is  ", s )
else:               # s <= 0
    print(" Invalid input for years ", x )