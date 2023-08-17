import util, copy
from typing import List
from pieces import piece, pawn, knight, bishop, rook, queen, king
import inspect

def checkForValidMove(board: List[piece.Piece | None], turn: str, piece: piece.Piece, startIndex: int, endIndex: int, heldPiece: piece.Piece, heldPieceIndex: int, lastMove: List[int]) -> bool:
    if endIndex < 0 or endIndex > 63:
        return False
    if isinstance(piece, pawn.Pawn):
        validMove = piece.calculateValidMove(board, startIndex, endIndex, lastMove, isinstance(turn, pawn.Pawn))
    else:
        validMove = piece.calculateValidMove(board, startIndex, endIndex)
    if not validMove and not checkForCastling(board, piece, startIndex, endIndex, heldPieceIndex):
        return False
    temp = board[endIndex]
    board[endIndex] = piece
    board[startIndex] = None
    if checkForCheck(board, piece.getColour(), heldPieceIndex, util.locateKing(board, turn, heldPieceIndex)):
        board[startIndex] = piece if heldPiece is None else None
        board[endIndex] = temp
        return False
    board[startIndex] = piece if heldPiece is None else None
    board[endIndex] = temp
    return True


def checkForCheck(board: List[piece.Piece | None], turn: str, heldPieceIndex: int, index: int) -> bool:
    row = index // 8
    col = index % 8

    if turn == "w":
        pawnChecks = [util.getIndexFromRowCol(row-1, col-1), util.getIndexFromRowCol(row-1, col+1)]
    else:
        pawnChecks = [util.getIndexFromRowCol(row+1, col-1), util.getIndexFromRowCol(row+1, col+1)]
    for check in pawnChecks:
        if check >= 0 and check <= 63 and check // 8 in [row-1, row+1]:
            if util.checkForEnemy(board, turn, check, pawn.Pawn):
                return True
            
    directions = [+8, -8, +1, -1, +9, -9, +7, -7]
    for direction in directions:
        indexToCheck = index + direction
        rowDiff = abs(index // 8 - indexToCheck // 8)
        colDiff = abs(index % 8 - indexToCheck % 8)
        while indexToCheck >= 0 and indexToCheck <= 63:
            if abs(direction) == 1 and (indexToCheck // 8 != row or ((indexToCheck+1) % 8 == 0 and direction == -1) or (indexToCheck % 8 == 0 and direction == 1)):
                break
            elif abs(direction) in [9, 7] and rowDiff != colDiff:
                break
            if abs(direction) in [8, 1] and util.checkForEnemy(board, turn, indexToCheck, (queen.Queen, rook.Rook)):
                return True
            elif abs(direction) in [9, 7] and util.checkForEnemy(board, turn, indexToCheck, (queen.Queen, bishop.Bishop)):
                return True
            elif util.checkForPiece(board, indexToCheck):
                break
            indexToCheck += direction
            rowDiff = abs(index // 8 - indexToCheck // 8)
            colDiff = abs(index % 8 - indexToCheck % 8)

    knightChecks = [-17, -15, -10, -6, 6, 10, 15, 17]
    for position in knightChecks:
        indexToCheck = index + position
        rowDiff = abs(index // 8 - indexToCheck // 8)
        colDiff = abs(index % 8 - indexToCheck % 8)
        if indexToCheck >= 0 and indexToCheck <= 63:
            if (rowDiff == 2 and colDiff == 1 or rowDiff == 1 and colDiff == 2) and util.checkForEnemy(board, turn, indexToCheck, knight.Knight):
                return True
    return False


def checkForCastling(board: List[piece.Piece | None], piece: piece.Piece, startIndex: int, endIndex: int, heldPieceIndex: int) -> bool:
    if not isinstance(piece, king.King) or checkForCheck(board, piece.getColour(), heldPieceIndex, util.locateKing(board, piece.getColour(), heldPieceIndex)):
        return False
    rowDiff =  endIndex // 8 - startIndex // 8
    colDiff = endIndex % 8 - startIndex % 8
    replaceWithNone = False

    if board[startIndex] is None:
        board[startIndex] = piece
        replaceWithNone = True
    if not piece.getMoved() and rowDiff == 0:
        if colDiff == 2 and util.checkForFriend(board, piece.getColour(), 63 if piece.getColour() == "w" else 7, rook.Rook) and not util.checkForPiece(board, 62 if piece.getColour() == "w" else 6) and not util.checkForPiece(board, 61 if piece.getColour() == "w" else 5):
            if not castleAndCheckForCheck(board, piece.getColour(), startIndex, 62, 6, heldPieceIndex) or not castleAndCheckForCheck(board, piece.getColour(), startIndex, 61, 5, heldPieceIndex):
                board[startIndex] = None if replaceWithNone else piece
                return False
            board[startIndex] = None if replaceWithNone else piece
            return True
        elif colDiff == -2 and util.checkForFriend(board, piece.getColour(), 56 if piece.getColour() == "w" else 0, rook.Rook) and not util.checkForPiece(board, 57 if piece.getColour() == "w" else 1) and not util.checkForPiece(board, 58 if piece.getColour() == "w" else 2) and not util.checkForPiece(board, 59 if piece.getColour() == "w" else 3):
            if not castleAndCheckForCheck(board, piece.getColour(), startIndex, 58, 2, heldPieceIndex) or not castleAndCheckForCheck(board, piece.getColour(), startIndex, 59, 3, heldPieceIndex):
                board[startIndex] = None if replaceWithNone else piece
                return False
            board[startIndex] = None if replaceWithNone else piece
            return True
    board[startIndex] = None if replaceWithNone else piece
    return False


def castleAndCheckForCheck(originalBoard: List[piece.Piece | None], turn: str, startIndex: int, endWhite: int, endBlack: int, heldPieceIndex: int) -> bool:
    board = copy.deepcopy(originalBoard)
    if util.checkForPiece(board, endWhite if turn == "w" else endBlack):
        return False
    board[endWhite if turn == "w" else endBlack] = board[startIndex]
    board[startIndex] = None

    if checkForCheck(board, turn, heldPieceIndex, util.locateKing(board, turn, heldPieceIndex)):
        return False
    return True

def checkForCheckmate(board: List[piece.Piece | None], turn: str, lastMove: List[int]) -> int:
    for x in range(64):
        if util.checkForFriend(board, turn,x, piece.Piece):
            for y in range(64):
                if checkForValidMove(board, turn, board[x], x, y, None, None, lastMove):
                    return 0
    if checkForCheck(board, turn, None, util.locateKing(board, turn, None)):
        return 1    
    return 2

