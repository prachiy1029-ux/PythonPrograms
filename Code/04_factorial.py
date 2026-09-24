def factorial(number):
    if number < 0:
        return "Invalid"

    result = 1
    for i in range(1, number + 1):
        result *= i

    return result


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print("Factorial:", factorial(number))