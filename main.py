from sys import excepthook

P = {
    1: 1,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 6,
    7: 7,
    8: 8,
    9: 9
}
board = {}
def refresh_board():
    global board
    board = f""" ___ ___ ___
| {P[1]} | {P[2]} | {P[3]} |
|___|___|___|
| {P[4]} | {P[5]} | {P[6]} |
|___|___|___|
| {P[7]} | {P[8]} | {P[9]} |
|___|___|___|"""



while True:
    refresh_board()
    print(board)
    try:
        User_Input = int(input("Please select a number from the board to place an X"))
        P[User_Input] = 'X'
    except ValueError:
        print("Please enter a number 1-10")


