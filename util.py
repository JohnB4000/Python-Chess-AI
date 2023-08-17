import math, pygame, logic
from typing import Tuple, Union, List
from pieces import piece, pawn, queen, king


def displayImage(screen: pygame.Surface, image: pygame.Surface, position: Tuple[int, int]) -> None:
    screen.blit(image, position)
    
def getIndexFromClick(position: int) -> int:
    x, y = position
    return math.floor(x/100) + (math.floor(y/100) * 8)

def getIndexFromRowCol(row: int, col: int) -> int:
    return col + (row * 8)

def calculatePosition(index: int) -> Tuple[int, int]:
    return ((index % 8) * 100, (index // 8) * 100)

def locateKing(board: List[piece.Piece | None], turn: str, heldPieceIndex: int) -> int:
    for x in range(64):
        if checkForFriend(board, turn, x, king.King):
            return x 
    return heldPieceIndex
            
def checkForPiece(board: List[piece.Piece | None], index: int) -> bool:
    return False if board[index] is None else True

def checkForEnemy(board: List[piece.Piece | None], turn: str, index: int, types: Union[piece.Piece, Tuple[piece.Piece]]) -> bool:
    if checkForPiece(board, index):
        return True if board[index].getColour() != turn and isinstance(board[index], types) else False
    
def checkForFriend(board: List[piece.Piece | None], turn: str, index: int, types: Union[piece.Piece, Tuple[piece.Piece]]) -> bool:
    if checkForPiece(board, index):
        return True if board[index].getColour() == turn and isinstance(board[index], types) else False

def checkForPromotion(screen: pygame.Surface, piece: piece.Piece, index: int) -> piece.Piece:
    if (piece.getColour() == "w" and index < 8 or piece.getColour() == "b" and index > 55) and isinstance(piece, pawn.Pawn):
        return queen.Queen(piece.getColour()[0]+"Queen.png")
    return piece