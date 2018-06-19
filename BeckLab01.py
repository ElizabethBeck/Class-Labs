integer_1 = int(input("Enter one integer: "))
integer_2 = int(input("Enter one integer: "))
integer_3 = int(input("Enter one more integer: "))
print("You put in:", integer_1, integer_2, integer_3)
added = integer_1 + integer_2 + integer_3
print("Sum =", added)
product = integer_1 * integer_2 * integer_3
print("Product =", product)
power = added**integer_1
print("Sum to the power of the first integer:", power)
sum_divided_int2 = added / integer_2
print("Sum divided by second integer: ", sum_divided_int2)
sum_divided_int3 = added // integer_3
print("Sum divided by integer 3:", sum_divided_int3)
remainder = added % integer_1
print("Remainder of sum divided by integer 1:", remainder)
highest = max(integer_1, integer_2, integer_3)
print("The largest integer is:", highest)
smallest = min(integer_1, integer_2, integer_3)
print("The smallest integer is:", smallest)
average = added/3
print("Average of the integers:", average)
average_2 = (added - smallest)/2
average_3 = (added - highest)/2
print("Average of the largest integers", average_2, "Average of the smallest integers:", average_3)
print("Ellie")
print("Computer Scinence")