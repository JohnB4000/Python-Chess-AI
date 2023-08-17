from pieces import piece
from typing import List
import pygame


class Queen(piece.Piece):
    def __init__(self, file: str):
        super().__init__(file)

    def getSymbol(self):
        return "Q"

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
        
        moveValue = endIndex - startIndex
        
        result = False
        if startRow == endRow and startCol != endCol or startRow != endRow and startCol == endCol:
            if moveValue in self.rightValidMoves:
                result = self.checkEmptyBetween2Points(board, startIndex, endIndex, self.rightValidMoves)
            elif moveValue in self.leftValidMoves:
                result = self.checkEmptyBetween2Points(board, startIndex, endIndex, self.leftValidMoves)
            elif moveValue in self.aboveValidMoves:
                result = self.checkEmptyBetween2Points(board, startIndex, endIndex, self.aboveValidMoves)
            elif moveValue in self.belowValidMoves:
                result = self.checkEmptyBetween2Points(board, startIndex, endIndex, self.belowValidMoves)
        if rowDiff == colDiff:
            if moveValue in self.aboveRightValidMoves:
                result = self.checkEmptyBetween2Points(board, startIndex, endIndex, self.aboveRightValidMoves)
            elif moveValue in self.aboveLeftValidMoves:
                result = self.checkEmptyBetween2Points(board, startIndex, endIndex, self.aboveLeftValidMoves)
            elif moveValue in self.belowRightValidMoves:
                result = self.checkEmptyBetween2Points(board, startIndex, endIndex, self.belowRightValidMoves)
            elif moveValue in self.belowLeftValidMoves:
                result = self.checkEmptyBetween2Points(board, startIndex, endIndex, self.belowLeftValidMoves)
        return result