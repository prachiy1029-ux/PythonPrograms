def find_duplicates(numbers):
    duplicates = []

    for number in numbers:
        if numbers.count(number) > 1 and number not in duplicates:
            duplicates.append(number)

    return duplicates


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))

    print("Duplicate elements:", find_duplicates(numbers))