def primes_in_range(start, end):
    primes = []

    for number in range(start, end + 1):
        if number >= 2:
            is_prime = True

            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:
                    is_prime = False
                    break

            if is_prime:
                primes.append(number)

    return primes


if __name__ == "__main__":
    start = int(input("Enter start: "))
    end = int(input("Enter end: "))

    print("Prime numbers:", primes_in_range(start, end))