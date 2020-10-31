import tic_tac_board as engine
from player import Human, RandomComputer


def play(players, verbose=True):
    board = engine.Board()
    if verbose:
        print(board)
        print()
    move_num = 0
    active_player = 0
    while True:
        move = players[active_player].get_move()
        status = board.move_and_check(move[0], move[1], players[active_player].get_mark())
        while status == "invalid":
            if verbose:
                print("Invalid move")
            move = players[active_player].get_move()
            status = board.move_and_check(move[0], move[1], players[active_player].get_mark())

        move_num += 1
        if verbose:
            print(move_num)
            print(board)
        if status == players[active_player].get_mark():
            if verbose:
                print("{0} WINS!".format(players[active_player].get_name()))
            return players[active_player].get_name(), move_num
        elif status == "draw":
            if verbose:
                print("It's a draw!")
            return "DRAW", move_num
        elif status == "valid":
            active_player = (active_player + 1) % 2


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = RandomComputer("Computer_X", "X")
    b = RandomComputer("Computer_O", "O")

    for _ in range(10):
        print(play([a, b], False))
