from pieces import piece
from typing import List
import pygame


class Rook(piece.Piece):
    def __init__(self, file: str):
        super().__init__(file)

    def getSymbol(self):
        return "R"

    def calculateValidMove(self, board: List[piece.Piece | None], startIndex: int, endIndex: int) -> bool:
        if board[endIndex] is not None:
            if board[endIndex].colour == self.colour:
                return False
    
        startRow = startIndex // 8
        startCol = startIndex % 8
        endRow = endIndex // 8
        endCol = endIndex % 8
        
        if startRow != endRow and startCol != endCol:
            return False
        
        moveValue = endIndex - startIndex
        
        if moveValue in self.rightValidMoves:
            return self.checkEmptyBetween2Points(board, startIndex, endIndex, self.rightValidMoves)
        elif moveValue in self.leftValidMoves:
            return self.checkEmptyBetween2Points(board, startIndex, endIndex, self.leftValidMoves)
        elif moveValue in self.aboveValidMoves:
            return self.checkEmptyBetween2Points(board, startIndex, endIndex, self.aboveValidMoves)
        elif moveValue in self.belowValidMoves:
            return self.checkEmptyBetween2Points(board, startIndex, endIndex, self.belowValidMoves)       
        return False