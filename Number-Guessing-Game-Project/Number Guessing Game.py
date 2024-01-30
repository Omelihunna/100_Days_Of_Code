import random
logo = """  ________                                                           ___.                 
 /  _____/ __ __   ____   ______ ______ _____      ____  __ __  _____\_ |__   ___________ 
/   \  ___|  |  \_/ __ \ /  ___//  ___/ \__  \    /    \|  |  \/     \| __ \_/ __ \_  __ \
\    \_\  \  |  /\  ___/ \___ \ \___ \   / __ \_ |   |  \  |  /  Y Y  \ \_\ \  ___/|  | \/
 \______  /____/  \___  >____  >____  > (____  / |___|  /____/|__|_|  /___  /\___  >__|   
        \/            \/     \/     \/       \/       \/            \/    \/     \/       
                                                                                         """
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
computer_guess =random.randint(1, 100)
lives = 0

def difficulty_check():
    global lives
    if difficulty == "easy":
        lives = 10
        if computer_guess >= 10:
            print(f"The starting digit of the number is {computer_guess // 10}")
    elif difficulty == "hard":
        lives = 5

def continuity():
    global lives
    while lives != 0:
        print(f"You have {lives} attempts remaining to guess a number.")
        user_guess = int(input("Make a guess: "))
        lives -= 1
        if user_guess != 0:
            int(user_guess)
            if user_guess < computer_guess:
                if computer_guess - user_guess <= 3:
                    print("Smoking Hot, but a little too low")
                else:
                    print("Too Low")
            elif user_guess > computer_guess:
                if user_guess - computer_guess <= 3:
                    print("Smoking Hot, but a little too high")
                else:
                    print("Too High")
            elif user_guess == computer_guess:
                print("You Win")
                return

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
difficulty_check()
continuity()
