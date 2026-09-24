def is_palindrome_string(text):
    text = text.lower()

    reversed_text = ""

    for character in text:
        reversed_text = character + reversed_text

    return text == reversed_text


if __name__ == "__main__":
    text = input("Enter a string: ")

    if is_palindrome_string(text):
        print("Palindrome")
    else:
        print("Not Palindrome")