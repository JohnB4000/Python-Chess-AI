from __future__ import annotations
import pygame
from typing import Tuple, List


class Piece:
    def __init__(self, file: str):
        self.file = file
        self.colour = file[0]
        self.moved = False
        self.rightValidMoves = [1, 2, 3, 4, 5, 6, 7]
        self.leftValidMoves = [-1, -2, -3, -4, -5, -6, -7]
        self.aboveValidMoves = [-8, -16, -24, -32, -40, -48, -56]
        self.belowValidMoves = [8, 16, 24, 32, 40, 48, 56]
        self.aboveRightValidMoves = [-7, -14, -21, -28, -35, -42, -49]
        self.aboveLeftValidMoves = [-9, -18, -27, -36, -45, -54, -63]
        self.belowRightValidMoves = [9, 18, 27, 36, 45, 54, 63]
        self.belowLeftValidMoves = [7, 14, 21, 28, 35, 42, 49]

    def display(self, screen: pygame.Surface, position: Tuple[int, int]) -> None:
        screen.blit(pygame.transform.scale(pygame.image.load('assets/'+self.file), (100, 100)), position)

    def getColour(self) -> str:
        return self.colour
    
    def getMoved(self) -> str:
        return self.moved
    
    def setMoved(self) -> None:
        self.moved = True
        
    def checkEmptyBetween2Points(self, board: List[Piece | None], startIndex: int, endIndex: int, possibleMoves: List[int]) -> bool:
        moveValue = endIndex - startIndex
        x = 0
        while moveValue != possibleMoves[x]:
            if board[startIndex + possibleMoves[x]] != None:
                return False
            else:
                x += 1
        return True