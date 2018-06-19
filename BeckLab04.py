rate1 = 5  # $5 rate
rate2 = 4
rate3 = 2

fee = 0.0       # initialize  
m = int(input(" Please enter number of minutes parked..."))
if (0 < m and m <= 60 ):      	#table 1
    if (m == 60):
    	print("Parking fee for ", m, "minutes is $ 5")
    else:
    	hrs = int(m/60) + 1
    	fee = hrs*rate1
    	print("Parking fee for ", m, " minutes is $", fee)
elif (m > 60 and m <= 300):    	# table 2
    if m == 300:
    	print("we are in table 2 fee is $ 20")	
    else:
    	hrs = int(m/60) + 1
    	fee = hrs*rate2
    	print('we are in table 2 fee is $', fee)
elif ( m > 300):			# table 3 
    hrs = int(m/60) + 1
    fee = hrs*rate3
    print('we are in table 3 fee = $', fee)
else:
    print("error  negative minutes", m )