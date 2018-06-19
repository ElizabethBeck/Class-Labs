import random
import math         # needed for gcd
array = []          # empty list

a = -100     # FIX
b = 100
x = random.randint(-100, 100 )  # Return a random integer a <= x <= b.
print("random integer x == ", x)

j = 0
n = 25                          # size of the array
while (j < n):                  # populate the array using the while loop
    x = random.randint(a, b )   # Return a random integer  a <= x <= b.
    array.append(x)             #APPEND adds to a list
    j = j + 1

print("array == ",array)    # 2
print("array length is ", len(array))    #  (2) now print the array
array.sort()                      # sort array
sub = []                     # subsequence
sub = array[12]   
sub2 = array[12:26]             #  create a subsequence start at 2 end at 5
sub3 = array[0:12]
avg = sum(array)/25
print("Array average is: ", avg) #3
even = 0
odd = 0
for a in array:
	if a % 2 == 0:
		even = even + 1
	else:
		odd = odd + 1
print("The number of even integers:", even) #4
print("The number of odd integers: ", odd) #5
pos = 0 
neg = 0
for a in array:
	if a > 0:
		pos = pos + 1
	else: 
		neg = neg + 1
print("Number of positive integers: ", pos) #6
print("Number of negative integers: ", neg) #7
print ('Median:', sub)             #  (8)
print("Integers above or equal to median: ", sub2) # 9
print("Integers below median: ", sub3) #10
s = int(input("Enter an integer: "))
print("Is ", s, " in the array? ", array.count(s)) #11
big = max(array)
small = min(array)
print("Largest integer:", big) #12
print("Smallest: ", small) #13
                      
array.reverse()                   # reverse the array
print("Integers sorted in reverse order:")
print(array) #14
def gcd(small, big):
    if big == 0:
    	return small
    else:
    	return int(gcd(big, small % big))
GCD = gcd(small, big)
print("Greatest common denomenator: ", GCD)


