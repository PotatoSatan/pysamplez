import random
chessBoard = {'1a': None, '1b': None, '1c': None, '1d': None, '1e': None, '1f': None, '1g': None, '1h': None,
              '2a': None, '2b': None, '2c': None, '2d': None, '2e': None, '2f': None, '2g': None, '2h': None,
              '3a': None, '3b': None, '3c': None, '3d': None, '3e': None, '3f': None, '3g': None, '3h': None,
              '4a': None, '4b': None, '4c': None, '4d': None, '4e': None, '4f': None, '4g': None, '4h': None,
              '5a': None, '5b': None, '5c': None, '5d': None, '5e': None, '5f': None, '5g': None, '5h': None,
              '6a': None, '6b': None, '6c': None, '6d': None, '6e': None, '6f': None, '6g': None, '6h': None,
              '7a': None, '7b': None, '7c': None, '7d': None, '7e': None, '7f': None, '7g': None, '7h': None,
              '8a': None, '8b': None, '8c': None, '8d': None, '8e': None, '8f': None, '8g': None, '8h': None}


validPieces = [ 'wpawn', 'wrook', 'wknight', 'wbishop', 'wqueen', 'wking',
                'bpawn', 'brook', 'bknight', 'bbishop', 'bqueen', 'bking']

print("Enter a chess piece starting with white\n"
      "Pieces should begin with either a 'w' or 'b' to represent white or black.\n"
      "followed by the pieces' name 'pawn' 'king' 'queen' 'bishop' 'rook' e.g. wpawn, wking : ")
turn = 0     # checks if it's black or white's turn
wking = 0
wqueen = 0
wbishop = 0
wknight = 0
wrook = 0
wpawn = 0


randomWhitePawnSlot = ['2a', '2b', '2c', '2d', '2e', '2f', '2g', '2h']
randomBPawnSlot = ['7a', '7b', '7c', '7d', '7e', '7f', '7g', '7h']
def PawnCaller(randomKey):
    randomWPawnSlot = ['2a', '2b', '2c', '2d', '2e', '2f', '2g', '2h']
    randomKey = random.choice(randomWPawnSlot)
    return randomKey


while True:
    chessKey = input()
    if chessKey == 'wpawn':
        for i in range(0,8):
            for checking in randomWhitePawnSlot():
                if checking in chessBoard and chessBoard[checking] is None:
                    chessBoard[checking] = chessKey
                    break
        else:
            print('Max white pawns reached, try a new piece.')
    print(chessBoard)
