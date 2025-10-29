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

def make_move():
    user_input = input("Select a position [1-9]")
    while type(user_input) != int and user_input not in range(1, 9):
        print("input must be an int between 1 and 9")
        user_input = input("Select a position [1-9]")


Game_Over = False
while not Game_Over:
    print_board()
    current_player = "X"
    make_move()
