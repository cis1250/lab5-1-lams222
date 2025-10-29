#!/usr/bin/env python3

# Word frequency exercise
# TODO: (Read detailed instructions in the Readme file)

import re

#This is a function that checks if a text qualifies as a sentence. You do not need to modify this!
def is_sentence(text):
    # Check if the text is not empty and is a string
    if not isinstance(text, str) or not text.strip():
        return False

    # Check for starting with a capital letter
    if not text[0].isupper():
        return False

    # Check for ending punctuation
    if not re.search(r'[.!?]$', text):
        return False

    # Check if it contains at least one word (non-whitespace characters)
    if not re.search(r'\w+', text):
        return False

    return True

# FUNCTION 1: Get and validate sentence
def get_sentence():
    while True:
        user_input = input("Enter a sentence: ")

        if is_sentence(user_input):
            return user_input
        else:
            print("Invalid sentence. Must start with a capital letter, include at least one word, and end with . ! or ?\n")


# FUNCTION 2: Calculate frequencies
def calculate_frequencies(sentence):
    words = []
    frequencies = []

    # Remove punctuation at end, then split
    sentence = sentence[:-1]      # remove last punctuation mark
    split_words = sentence.split()  # split into words

    for word in split_words:
        word = word.lower()   # normalize

        # Check if already in words list
        if word in words:
            index = words.index(word)
            frequencies[index] += 1
        else:
            words.append(word)
            frequencies.append(1)

    return words, frequencies


# FUNCTION 3: Print frequencies
def print_frequencies(words, frequencies):
    print("\nWord Frequencies:")
    for i in range(len(words)):
        print(f"{words[i]} : {frequencies[i]}")
    print()


# Main function controlling the program
def main():
    sentence = get_sentence()
    words, frequencies = calculate_frequencies(sentence)
    print_frequencies(words, frequencies)


# Run main
if __name__ == "__main__":
    main()
