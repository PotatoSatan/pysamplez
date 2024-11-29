import random
chessBoard = {'1a': '', '1b': '', '1c': '', '1d': '', '1e': '', '1f': '', '1g': '', '1h': '',
              '2a': '', '2b': '', '2c': '', '2d': '', '2e': '', '2f': '', '2g': '', '2h': '',
              '3a': '', '3b': '', '3c': '', '3d': '', '3e': '', '3f': '', '3g': '', '3h': '',
              '4a': '', '4b': '', '4c': '', '4d': '', '4e': '', '4f': '', '4g': '', '4h': '',
              '5a': '', '5b': '', '5c': '', '5d': '', '5e': '', '5f': '', '5g': '', '5h': '',
              '6a': '', '6b': '', '6c': '', '6d': '', '6e': '', '6f': '', '6g': '', '6h': '',
              '7a': '', '7b': '', '7c': '', '7d': '', '7e': '', '7f': '', '7g': '', '7h': '',
              '8a': '', '8b': '', '8c': '', '8d': '', '8e': '', '8f': '', '8g': '', '8h': ''}

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
        for checking in randomWhitePawnSlot:
            if checking in chessBoard and chessBoard[checking] is None:
                chessBoard[randomWhitePawnSlot] = chessKey

    print(chessBoard)
