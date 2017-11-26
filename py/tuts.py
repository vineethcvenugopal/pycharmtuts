num1, num2 = input('Enter 2 numbers: ').split()

num1 = int(num1)
num2 = int(num2)

sum = num1 + num2

difference = num1 - num2

quotient = num1 / num2

remainder = num1 % num2

#Print Results

print("{} + {} = {}".format(num1, num2, sum))
print("{} - {} = {}".format(num1, num2, difference))
print("{} / {} = {}".format(num1, num2, quotient))
print("{} % {} = {}".format(num1, num2, remainder))
