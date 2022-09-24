import random
from HANGMAN_WORDS import word_list

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)
chosen_word = random.choice(word_list)
print(f'Pssst, the solution is {chosen_word}.')
lives = 6
display = []
count = len(chosen_word)
for n in range(count):
    display.append("_")
print(display)
display_text = "".join(display)

end_of_game = False


def check():
    n = 0
    for _ in display:
        if chosen_word[n] == guess:
            display[n] = guess
        n += 1

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for letter in chosen_word:
        if letter == guess:
            check()
    if guess not in chosen_word:
        lives -= 1
    elif lives <= 0:
        break
        print("You lose")
    print(" ".join(display))

    if "_" not in display:
        end_of_game = True
        print("You Win")

    print(stages[lives])