import random

def play():
    user = input("What\'s your choice? 'r' for rock, 'p' for paper, 's' for scissors")
    computer = random.choice(['r', 'p', 'r'])
    if user == computer:
        return 'It\'s a tie'
    # r > s, s > p, p > r
    def is_win(player, opponent):
       # return true if player wins
       # r > s, s > p, p > r
       if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
           or (player == 'p' and opponent == 'r'):
           return True
    if is_win(user, computer):
        return "Congratulations you\'re the winner of this round"
    if is_win(computer, user):
        return "Nice try but not good enough"
    

print(play())