
n = int(input("Enter a non-negative integer: "))

if n < 0:
    print("Please enter a non-negative integer.")
else:
  
    factorial = 2
    for i in range(2, n + 1):
        factorial *= i
    
  
    print("Factorial of",  ":", factorial)
