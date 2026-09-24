def check_vowel_consonant(character):
    character = character.lower()

    if character in "aeiou":
        return "Vowel"
    elif character.isalpha():
        return "Consonant"
    else:
        return "Invalid"


if __name__ == "__main__":
    character = input("Enter a character: ")
    print(check_vowel_consonant(character))