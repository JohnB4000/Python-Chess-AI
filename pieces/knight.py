from pieces import piece
from typing import List
import pygame


class Knight(piece.Piece):
    def __init__(self, file: str):
        super().__init__(file)
    
    def getSymbol(self):
        return "N"

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

        if (rowDiff == 2 and colDiff == 1) or (rowDiff == 1 and colDiff == 2):
            return True
        return False