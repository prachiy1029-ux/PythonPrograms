def second_largest(numbers):
    unique_numbers = list(set(numbers))

    if len(unique_numbers) < 2:
        return "Invalid"

    unique_numbers.sort(reverse=True)

    return unique_numbers[1]


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    print("Second largest:", second_largest(numbers))