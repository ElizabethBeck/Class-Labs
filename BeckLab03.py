import random
a = -50
b = 50
x = random.randint(a,b) 
y = random.randint(a,b)
z = random.randint(a,b)
w = random.randint(a,b)
list1 = (x, y, z, w)
print('The integers are:', list1)
maximum = max(w, x, y, z)
print("The maximum integer:", maximum)
minimum = min(w, x, y, z)
print("The minimum integer:", minimum)
even = 0
odd = 0
for n in list1:
	if n % 2 == 0:
		even = even + 1
	else:
		odd = odd + 1
print("The number of even integers is: ", even)
print("The number of odd integers is: ", odd)
integers_between = 0
for n in list1:
	if 0 < n < 50:
		integers_between = integers_between + 1
print("The number of integers greater than 0 but less than 50: ", integers_between)
positive = 0 
negative = 0
for n in list1:
	if n >= 0:
		positive = positive + 1
	else:
		negative = negative + 1 
print("The number of positive integers is: ", positive
	)
print("The number of negative integers is: ", negative)
avg_maxmin = (max(list1) + min(list1))/ 2
print("The average of the smallest and largest integers: ", avg_maxmin)
general_avg = (x + y + z + w)/4
print("The average of the four integers is: ", general_avg) 




# your code will require 4 statements similar to (1) above
