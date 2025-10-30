from sys import excepthook

P = [i + 1 for i in range(9)]

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

def make_move(player):
    user_input = collect_user_input()
    if not user_input:
        pass
        return 0
    if user_input not in range(1, 9):
        print("input must be an int between 1 and 9")
        return 0

    return 1

def switch(player):
    if player == "X":
        return "O"
    else:
        return "X"

Game_Over = False
print_board()
current_player = "X"
while not Game_Over:
    if make_move(current_player:
        print_board()
    current_player = switch(current_player)
