def character_frequency(text):
    frequency = {}

    for character in text:
        if character in frequency:
            frequency[character] += 1
        else:
            frequency[character] = 1

    return frequency


if __name__ == "__main__":
    text = input("Enter a string: ")
    print("Character frequency:", character_frequency(text))