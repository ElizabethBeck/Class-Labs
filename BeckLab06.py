import random
# Initialize array
myArray = []
a = 0
b = 1
size = 50	
j = 0
n =1000		
# Populate array with size = 25 random integers in the range 0 - 1
#and repeat for n times
while (j < n):
    for k in range(size):
        randNum = random.randint(a,b)
        myArray.insert(k, randNum)
    j = j + 1

# Display array  size
print("size of my array is :", len(myArray))
# printmyArray  10 values per line 
k = 0
sub = []
while (k < len(myArray) ):
    sub = myArray[k: k+10]
    print("...",k, sub)
    k = k+10

ones = myArray.count(b)			#place holder code only FIX 
zeros = myArray.count(a)			# place holder code FIX  
print(" number of 1 is: ", ones)
print(" number of 0 is: ", zeros)

# mean and standard deviation (sd) calculations here
#EXAMPLE ONLY
mean = 25000	
sd = 111.8		
print("=====================")
print('mean of My Array:', mean, " sd (standard deviation: ", sd)
print (" mean +-sd:  ",mean + sd, "  " , mean - sd )
print ("the mean number of 1's is within mean +- sd ?")     
# need to answer this 
range1 = mean + sd 
range2 = mean - sd 
if range2 <= ones <= range1:
	print("Yes")
else:
	print("No")

# compare the number of 1’s (variable zeros calculated above 
# to see if it is within the range mean +– sd….
