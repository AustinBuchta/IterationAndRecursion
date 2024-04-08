def iterative_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n - 1)

def main():
    numbers = [0, 5, 10, 25, 50, 100]
    for num in numbers:
        iterative_result = iterative_factorial(num)
        recursive_result = recursive_factorial(num)
        print(f"Factorial of {num}! using iterative method = {iterative_result}")
        print(f"Factorial of {num}! using recursive method = {recursive_result}")
        print()

if __name__ == "__main__":
    main()