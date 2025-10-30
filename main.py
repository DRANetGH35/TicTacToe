from sys import excepthook

P = [i  for i in range(1, 10)]

def print_board():
    print(f""" ___ ___ ___
| {P[0]} | {P[1]} | {P[2]} |
|___|___|___|
| {P[3]} | {P[4]} | {P[5]} |
|___|___|___|
| {P[6]} | {P[7]} | {P[8]} |
|___|___|___|""")

def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

def collect_user_input():
    try:
        return int(input("Select a position [1-9]"))
    except ValueError:
        print("Must be an integer")
        return None

def check_win(player):
    #check rows
    for i in range(3):
        if P[i] == player and P[i + 1] == player and P[i + 2] == player:
            return 1
    #check columns
    for i in range(3):
        if P[i] == player and P[i + 3] == player and P[i + 6] == player:
            return 1
    return 0

def make_move(player):
    user_input = collect_user_input()
    if not user_input:
        pass
        return 0
    if user_input not in range(1, 9):
        print("input must be an int between 1 and 9")
        return 0
    P[user_input - 1] = player
    return 1

def switch(player):
    if player == "X":
        return "O"
    else:
        return "X"

Game_Over = False
current_player = "X"
print_board()
while not Game_Over:

    if make_move(current_player):
        print_board()
        if check_win(current_player):
            Game_Over = True
            print(f"{current_player} wins!")
        current_player = switch(current_player)


