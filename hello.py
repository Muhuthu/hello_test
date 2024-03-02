def factorial(n):
	if n == 0:
		return 0;
	else:
		return n * factorial(n-1)

number = int(input("Enter integer: "))
result = factorial(number)
print(f"Factorial of {number} is {result}" )
