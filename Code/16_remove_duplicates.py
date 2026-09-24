def remove_duplicates(numbers):
    unique_numbers = []

    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)

    return unique_numbers


if __name__ == "__main__":
    numbers = list(map(int, input("Enter numbers separated by space: ").split()))
    print("List without duplicates:", remove_duplicates(numbers))