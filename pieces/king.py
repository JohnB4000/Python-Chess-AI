from pieces import piece, rook
from typing import List
import pygame, util


class King(piece.Piece):
    def __init__(self, file: str):
        super().__init__(file)

    def getSymbol(self):
        return "K"

    def calculateValidMove(self, board: List[piece.Piece | None], startIndex: int, endIndex: int) -> bool:
        if util.checkForFriend(board, self.colour, endIndex, piece.Piece):
            return False
    
        startRow = startIndex // 8
        startCol = startIndex % 8
        endRow = endIndex // 8
        endCol = endIndex % 8

        rowDiff = abs(startRow - endRow)
        colDiff = abs(startCol - endCol)

        if self.kingNearby(board, endIndex, endRow, endCol):
            return False
        
        if rowDiff in [0, 1] and colDiff in [0, 1]:
            return True
        return False
    
    def kingNearby(self, board: List[piece.Piece | None], endIndex: int, endRow: int, endCol: int) -> bool:
        indexesToCheck = []
        if endRow != 0:
            indexesToCheck.append(-8)
        if endRow != 7:
            indexesToCheck.append(8)
        if endCol != 0:
            indexesToCheck.append(-1)
        if endCol != 7:
            indexesToCheck.append(1)
        if endRow != 0 and endCol != 0:
            indexesToCheck.append(-9)
        if endRow != 0 and endCol != 7:
            indexesToCheck.append(-7)
        if endRow != 7 and endCol != 0:
            indexesToCheck.append(7)
        if endRow != 7 and endCol != 7:
            indexesToCheck.append(9)

        for index in indexesToCheck:
            if isinstance(board[endIndex + index], King) and self.colour != board[endIndex + index].colour:
                return True
        return False