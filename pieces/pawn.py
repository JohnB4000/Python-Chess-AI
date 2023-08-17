from pieces import piece
from typing import List
import pygame


class Pawn(piece.Piece):
    def __init__(self, file: str):
        super().__init__(file)
        if self.colour == "w":
            self.validMove = -8
            self.validMoveFromStart = -16
            self.validCaptures = [-9, -7]
        elif self.colour == "b":
            self.validMove = 8
            self.validMoveFromStart = 16
            self.validCaptures = [9, 7]

    def getSymbol(self):
        return "P"

    def calculateValidMove(self, board: List[piece.Piece | None], startIndex: int, endIndex: int, lastMove: List[int], lastPieceWasPawn: bool) -> bool:
        startRow = startIndex // 8
        startCol = startIndex % 8
        endRow = endIndex // 8
        endCol = endIndex % 8

        rowDiff = abs(startRow - endRow)
        colDiff = abs(startCol - endCol)
        
        moveValue = endIndex - startIndex

        if board[endIndex] is None and board[startIndex + self.validMove] is None:
            if self.moved is False and moveValue == self.validMoveFromStart:
                return True
            elif moveValue == self.validMove:
                return True
            
        if moveValue in self.validCaptures and colDiff == 1:
            if board[endIndex] is not None:
                if board[endIndex].colour != self.colour:
                    return True
            elif lastPieceWasPawn and abs(lastMove[0] - lastMove[1]) == 16:
                if (self.colour == "w" and lastMove[1] == endIndex + 8) or (self.colour == "b" and lastMove[1] == endIndex - 8):
                    board[lastMove[1]] = None
                    return True
        return False