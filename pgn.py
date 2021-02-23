from chess import pgn


def side_to_move_first(game):
    first_move = str(game.mainline_moves())
    if first_move[1:4] == "...":
        return "black"
    else:
        return "white"


for filename in ("bain-pins",):
    try:
        with open(f"./files/{filename}.pgn", mode="rt") as pgn_file:
            while True:
                print("----------------------------------------")
                game = pgn.read_game(pgn_file)
                if game:
                    print(game.mainline_moves())
                    print(f"{side_to_move_first(game)} to move")
                    # print(game.headers)
                else:
                    break
    except OSError as e:
        print(e)
