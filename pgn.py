from pathlib import Path
from chess import pgn


def side_to_move_first(game):
    first_move = str(game.mainline_moves())
    if first_move[1:4] == "...":
        return "black"
    else:
        return "white"


def save_game(game, file):
    print(game, file=file, end="\n\n")

input_path = Path("./input")
input_files = input_path.glob("*.pgn")

for f in input_files:
    filename = f.stem
    try:
        with open(f, mode="rt") as pgn_file, open(
            f"./output/{filename}-white.pgn", mode="wt"
        ) as white_file, open(
            f"./output/{filename}-black.pgn", mode="wt"
        ) as black_file:
            while True:
                print("----------------------------------------")
                game = pgn.read_game(pgn_file)
                if game:
                    print(game.mainline_moves())
                    side = side_to_move_first(game)
                    print(f"{side} to move")
                    if side == "white":
                        save_game(game, white_file)
                    elif side == "black":
                        save_game(game, black_file)
                    # print(game.headers)
                else:
                    break
    except OSError as e:
        print(e)
