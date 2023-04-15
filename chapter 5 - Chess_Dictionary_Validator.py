'''Chess Dictionary Validator
In this chapter, we used the dictionary value {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop',
'5h': 'bqueen', '3e': 'wking'} to represent a chess board. Write a function named isValidChessBoard()
that takes a dictionary argument and returns True or False depending on if the board is valid.

A valid board will have exactly one black king and exactly one white king.
Each player can only have at most 16 pieces,
at most 8 pawns, and
all pieces must be on a valid space from '1a' to '8h';
The piece names begin with either a 'w' or 'b' to represent white or black,
followed by 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'.
This function should detect when a bug has resulted in an improper chess board.'''

board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking',
         '2a': 'bpawn', '2b': 'bpawn', '2c': 'bpawn', '2d': 'bpawn', '2e': 'bpawn',
         '4a': 'wbishop', '4b': 'wbishop', '7a': 'wpawn'}
def dec_analysis(chess_board: dict, colour: str)-> dict:
    dec = {}
    for piece in chess_board.values():
        if piece[0] == colour:
            dec.setdefault(piece, 0)
            dec[piece] += 1
    return dec

dec_analysis(board, 'b')
dec_analysis(board, 'w')

def piece_counter(dec_colour: dict) -> int:
    count = 0
    for amount in dec_colour.values():
        count += amount
    return count

def is_valid_chessboard(chess_board: dict):
    valid_numbers = '12345678'
    valid_letters = 'abcdefgh'
    valid_colors = 'bw'
    valid_pieces = ['king', 'queen', 'rock', 'bishop', 'knight', 'pawn']
    # 1. Have exactly one black king and exactly one white king.
    if dec_analysis(board, 'b').get('bking', 0) != 1 or dec_analysis(board, 'w').get('wking', 0) != 1:
        print('Not exactly one king error')
        return False
    # 2. Each player can only have at most 16 pieces.
    if piece_counter(dec_analysis(board, 'b')) > 16 or piece_counter(dec_analysis(board, 'w')) > 16:
        print('Too many pieces error')
        return False
    # 3. Each player have at most 8 pawns.
    if dec_analysis(board, 'b')['bpawn'] > 8 or dec_analysis(board, 'w')['wpawn'] > 8:
        print('Too many pawns error')
        return False
    # 4. All pieces must be on a valid space from '1a' to '8h';
    for space in board.keys():
        if space[0] not in valid_numbers or space[1] not in valid_letters:
            print('Invalid space error')
            return False
    # 5. The piece names begin with either a 'w' or 'b' to represent white or black and
    for piece in board.values():
        if piece[0] not in valid_colors:
            print('Invalid colours of pieces error')
            return False
    # 6. Awailable pices names 'pawn', 'knight', 'bishop', 'rook', 'queen', or 'king'.
    for piece in board.values():
        if piece[1:] not in valid_pieces:
            print('Invalid piece names')
            return False
    print('Chess board is Valid. Everything is ok')

is_valid_chessboard(board)
