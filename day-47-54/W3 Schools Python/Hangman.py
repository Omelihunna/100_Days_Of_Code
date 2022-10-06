import random
import string

from WORDS import words

def get_valid_word(words):
    word = random.choice(words) #randomly chooses word from list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    #Get User Input
    while len(word_letters) > 0:
        #letters used
        print("you have used these letters: ", " ".join(used_letters))

    #What the current words is
    word_list = [letter if letter in used_letters else '-' for letter in word]
    print("Current Word: ", ' '.join(word_list))
    user_letter = input("Guess a letter: ").upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if used_letters in word_letters:
            word_letters.remove(used_letters)
    elif user_letter in used_letters:
        print("You have already used that character. Please try again")

    else:
        print("Invalid Character, Please try again")

user_input = input("Type Something")
print(user_input)
