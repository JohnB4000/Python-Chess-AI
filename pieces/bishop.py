from pieces import piece
from typing import List
import pygame


class Bishop(piece.Piece):
    def __init__(self, file: str):
        super().__init__(file)

    def getSymbol(self):
        return "B"

    def calculateValidMove(self, board: List[piece.Piece | None], startIndex: int, endIndex: int) -> bool:
        if board[endIndex] is not None:
            if board[endIndex].colour == self.colour:
                return False
    
        startRow = startIndex // 8
        startCol = startIndex % 8
        endRow = endIndex // 8
        endCol = endIndex % 8

        rowDiff = abs(startRow - endRow)
        colDiff = abs(startCol - endCol)
        
        if rowDiff != colDiff:
            return False
        
        moveValue = endIndex - startIndex
        
        if moveValue in self.aboveRightValidMoves:
            return self.checkEmptyBetween2Points(board, startIndex, endIndex, self.aboveRightValidMoves)
        elif moveValue in self.aboveLeftValidMoves:
            return self.checkEmptyBetween2Points(board, startIndex, endIndex, self.aboveLeftValidMoves)
        elif moveValue in self.belowRightValidMoves:
            return self.checkEmptyBetween2Points(board, startIndex, endIndex, self.belowRightValidMoves)
        elif moveValue in self.belowLeftValidMoves:
            return self.checkEmptyBetween2Points(board, startIndex, endIndex, self.belowLeftValidMoves)     
        return False