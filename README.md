# PGN Tools

I needed to split some PGN files based on whether it was white or black to move first (tactics exercises). I couldn't see that Chessbase, ChessX, or SCID would let me do this, so I wrote a quick Python script to do the job.

Currently it just reads all PGN files from a `./input/` directory, and splits them into `output/*-white.pgn` and `output/*-black.pgn` files. One pair of files will be generated for each input file.

At some point I will clean this up to use command-line arguments, and probably add more tools should I need them.

Uses [Python Chess](https://python-chess.readthedocs.io/en/latest/) for the PGN parsing.
