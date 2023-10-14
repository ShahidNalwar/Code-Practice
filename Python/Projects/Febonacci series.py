# Function to generate Fibonacci series up to n terms
def generate_fibonacci(n):
    fibonacci_series = []
    a, b = 0, 1

    for i in range(n):
        fibonacci_series.append(a)
        a, b = b, a + b

    return fibonacci_series

# Number of terms you want in the series
n = int(input("Enter the number of terms: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    fibonacci_series = generate_fibonacci(n)
    print("Fibonacci Series:")
    for term in fibonacci_series:
        print(term, end=" ")
