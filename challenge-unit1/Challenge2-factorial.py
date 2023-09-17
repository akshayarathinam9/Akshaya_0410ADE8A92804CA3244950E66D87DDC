#challenge1-Implement a recursive function to calculate the factorial of a given number.
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: factorial of n is n times the factorial of (n-1)
    else:
        return n * factorial(n - 1)

# Example usage:
number = int(input("Enter the number:"))
result = factorial(number)
print(f"The factorial of {number} is {result}")
