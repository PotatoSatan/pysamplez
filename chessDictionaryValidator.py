import sys, time

chessBoard = {'1a': None, '1b': None, '1c': None, '1d': None, '1e': None, '1f': None, '1g': None, '1h': None,
              '2a': None, '2b': None, '2c': None, '2d': None, '2e': None, '2f': None, '2g': None, '2h': None,
              '3a': None, '3b': None, '3c': None, '3d': None, '3e': None, '3f': None, '3g': None, '3h': None,
              '4a': None, '4b': None, '4c': None, '4d': None, '4e': None, '4f': None, '4g': None, '4h': None,
              '5a': None, '5b': None, '5c': None, '5d': None, '5e': None, '5f': None, '5g': None, '5h': None,
              '6a': None, '6b': None, '6c': None, '6d': None, '6e': None, '6f': None, '6g': None, '6h': None,
              '7a': None, '7b': None, '7c': None, '7d': None, '7e': None, '7f': None, '7g': None, '7h': None,
              '8a': None, '8b': None, '8c': None, '8d': None, '8e': None, '8f': None, '8g': None, '8h': None}


def printChessboard(theBoard):
    for row in range(1, 9):
        print(theBoard[f'{row}a'], theBoard[f'{row}b'], theBoard[f'{row}c'], theBoard[f'{row}d'],
              theBoard[f'{row}e'], theBoard[f'{row}f'], theBoard[f'{row}g'], theBoard[f'{row}h'])


printChessboard(chessBoard)

validPieces = ['wpawn', 'wrook', 'wknight', 'wbishop', 'wqueen', 'wking',
               'bpawn', 'brook', 'bknight', 'bbishop', 'bqueen', 'bking']

print("Enter a chess piece starting with white\n"
      "Pieces should begin with either a 'w' or 'b' to represent white or black.\n"
      "followed by the pieces' name 'pawn' 'king' 'queen' 'bishop' 'rook' e.g. wpawn, wking : ")
turn = 0  # checks if it's black or white's turn
wking = 0
wqueen = 0
wbishop = 0
wknight = 0
wrook = 0
wpawn = 0

bking = 0
bqueen = 0
bbishop = 0
bknight = 0
brook = 0
bpawn = 0

piececounter = 0

WhitePawnSlot = ['2a', '2b', '2c', '2d', '2e', '2f', '2g', '2h']
WhiteRookSlot = ['1a', '1h']
WhiteKnightSlot = ['1b', '1g']
WhiteBishopSlot = ['1c', '1f']

BlackPawnSlot = ['7a', '7b', '7c', '7d', '7e', '7f', '7g', '7h']
BlackRookSlot = ['8a', '8h']
BlackKnightSlot = ['8b', '8g']
BlackBishopSlot = ['8c', '8f']


def isValidPiece():
    if wchessKey not in validPieces:
        return 0
    else:
        return 1


def myTurnNow():
    if turn == 0:
        print("White's turn.")
    elif turn == 1:
        print("Black's turn.")


while True:
    if piececounter == 32:
        print('Chessboard already full, ending game.')
        printChessboard(chessBoard)
        sys.exit()
    else:
        if turn == 0:
            print("White's turn.")
            wchessKey = input()
            if wchessKey.startswith('w'):
                if wchessKey in validPieces:
                    turn += 1
                    if wchessKey == 'wpawn':
                        if wpawn == 8:
                            print('Max white pawns reached, try a new piece.')
                            continue
                        for i in WhitePawnSlot:
                            if i in chessBoard and chessBoard[i] is None:
                                chessBoard[i] = wchessKey
                                wpawn += 1
                                piececounter += 1
                                printChessboard(chessBoard)
                                break
                    elif wchessKey == 'wrook':
                        if wrook == 2:
                            print('Max white rooks reached, try a new piece.')
                            continue
                        for i in WhiteRookSlot:
                            if i in chessBoard and chessBoard[i] is None:
                                chessBoard[i] = wchessKey
                                wrook += 1
                                piececounter += 1
                                printChessboard(chessBoard)
                                break
                    elif wchessKey == 'wbishop':
                        if wbishop == 2:
                            print('Max white bishops reached, try a new piece.')
                            continue
                        for i in WhiteBishopSlot:
                            if i in chessBoard and chessBoard[i] is None:
                                chessBoard[i] = wchessKey
                                wbishop += 1
                                piececounter += 1
                                printChessboard(chessBoard)
                                break
                    elif wchessKey == 'wknight':
                        if wknight == 2:
                            print('Max white knights reached, try a new piece.')
                            continue
                        for i in WhiteKnightSlot:
                            if i in chessBoard and chessBoard[i] is None:
                                chessBoard[i] = wchessKey
                                wknight += 1
                                piececounter += 1
                                printChessboard(chessBoard)
                                break
                    elif wchessKey == 'wking':
                        if wking == 1:
                            print('Max white king reached, try a new piece.')
                            continue
                        else:
                            chessBoard['1d'] = wchessKey
                            wking += 1
                            piececounter += 1
                            printChessboard(chessBoard)
                    elif wchessKey == 'wqueen':
                        if wqueen == 1:
                            print('Max white queen reached, try a new piece.')
                            continue
                        else:
                            chessBoard['1e'] = wchessKey
                            wqueen += 1
                            piececounter += 1
                            printChessboard(chessBoard)
                else:
                    print('Not a valid chess piece.')
                    continue
            else:
                print('Not a white piece, try again.')
                continue
            # black
        else:
            print("Black's turn.")
            bchessKey = input()
            if bchessKey.startswith('b'):
                if bchessKey in validPieces:
                    turn = 0
                    if bchessKey == 'bpawn':
                        if bpawn == 8:
                            print('Max black pawns reached, try a new piece.')
                            continue
                        for i in BlackPawnSlot:
                            if i in chessBoard and chessBoard[i] is None:
                                chessBoard[i] = bchessKey
                                bpawn += 1
                                piececounter += 1
                                printChessboard(chessBoard)
                                break
                    elif bchessKey == 'brook':
                        if brook == 2:
                            print('Max black rooks reached, try a new piece.')
                            continue
                        for i in BlackRookSlot:
                            if i in chessBoard and chessBoard[i] is None:
                                chessBoard[i] = bchessKey
                                brook += 1
                                piececounter += 1
                                printChessboard(chessBoard)
                                break
                    elif bchessKey == 'bbishop':
                        if bbishop == 2:
                            print('Max black bishops reached, try a new piece.')
                            continue
                        for i in BlackBishopSlot:
                            if i in chessBoard and chessBoard[i] is None:
                                chessBoard[i] = bchessKey
                                bbishop += 1
                                piececounter += 1
                                printChessboard(chessBoard)
                                break
                    elif bchessKey == 'bknight':
                        if bknight == 2:
                            print('Max black knights reached, try a new piece.')
                            continue
                        for i in BlackKnightSlot:
                            if i in chessBoard and chessBoard[i] is None:
                                chessBoard[i] = bchessKey
                                bknight += 1
                                piececounter += 1
                                printChessboard(chessBoard)
                                break
                    elif bchessKey == 'bking':
                        if bking == 1:
                            print('Max black king reached, try a new piece.')
                            continue
                        else:
                            chessBoard['8d'] = bchessKey
                            bking += 1
                            piececounter += 1
                            printChessboard(chessBoard)
                    elif bchessKey == 'bqueen':
                        if wqueen == 1:
                            print('Max black queen reached, try a new piece.')
                            continue
                        else:
                            chessBoard['8e'] = bchessKey
                            bqueen += 1
                            piececounter += 1
                            printChessboard(chessBoard)
                else:
                    print('Not a valid chess piece.')
                    continue
            else:
                print('Not a black piece, try again.')
                continue
