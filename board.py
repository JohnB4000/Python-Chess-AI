import pygame, util, logic
from pieces import pawn, knight, bishop, rook, queen, king


class Board:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.image = pygame.transform.scale(pygame.image.load('assets/WhiteBackgroundBoard.png'), (800, 800))
        self.lastMoveImage = pygame.transform.scale(pygame.image.load('assets/lastMove.png'), (100, 100))
        self.heldPiece = None
        self.heldPieceIndex = None
        self.lastMove = None
        self.lastMovePiece = None
        self.board = None
        self.turn = None
        self.setup()


    def turnPlayed(self) -> None:
        self.turn = "w" if self.turn == "b" else "b"


    def display(self) -> None:
        self.screen.blit(self.image, (0,0))
        if self.lastMove != None:
            util.displayImage(self.screen, self.lastMoveImage, util.calculatePosition(self.lastMove[0]))
            util.displayImage(self.screen, self.lastMoveImage, util.calculatePosition(self.lastMove[1]))
        for i in range(len(self.board)):
            if self.board[i] is not None:
                position = util.calculatePosition(i)
                self.board[i].display(self.screen, position)
        if self.heldPiece is not None:
            self.showPossibleMoves()
            util.displayImage(self.screen, self.lastMoveImage, util.calculatePosition(self.heldPieceIndex))
            x, y = pygame.mouse.get_pos()
            self.heldPiece.display(self.screen, (x-50, y-50))

    
    def showPossibleMoves(self) -> None:
        for x in range(64):
            if logic.checkForValidMove(self.board, self.turn, self.heldPiece, self.heldPieceIndex, x, self.heldPiece, self.heldPieceIndex, self.lastMove):
                util.displayImage(self.screen, self.lastMoveImage, util.calculatePosition(x))


    def userMove(self, index: int) -> bool:
        if self.heldPiece is None and util.checkForPiece(self.board, index):
            self.heldPiece = self.board[index]
            self.heldPieceIndex = index
            self.board[index] = None
        elif self.heldPiece is not None:
            if self.heldPieceIndex == index:
                self.board[index] = self.heldPiece
                self.heldPiece = None
                return False
            if logic.checkForValidMove(self.board, self.turn, self.heldPiece, self.heldPieceIndex, index, self.heldPiece, self.heldPieceIndex, self.lastMove):
                if logic.checkForCastling(self.board, self.heldPiece, self.heldPieceIndex, index, self.heldPieceIndex) and isinstance(self.heldPiece, king.King):
                    if index - self.heldPieceIndex == 2:
                        self.board[61 if self.turn == "w" else 5] = self.board[63 if self.turn == "w" else 7]
                        self.board[63 if self.turn == "w" else 7] = None
                    elif index - self.heldPieceIndex == -2:
                        self.board[59 if self.turn == "w" else 3] = self.board[56 if self.turn == "w" else 0]
                        self.board[56 if self.turn == "w" else 0] = None
                else:
                    self.heldPiece = util.checkForPromotion(self.screen, self.heldPiece, index)
                self.board[index] = self.heldPiece
                self.heldPiece = None
                if self.heldPieceIndex != index:
                    self.lastMove = [self.heldPieceIndex, index]
                    self.lastMovePiece = self.board[index]
                    self.board[index].setMoved()
                    self.turnPlayed()
                    return True
        return False
    
    
    def computerMove(self, startIndex: int, endIndex: int) -> None:
        if logic.checkForCastling(self.board, self.board[startIndex], startIndex, endIndex, self.heldPieceIndex) and isinstance(self.board[startIndex], king.King):
            if endIndex - startIndex == 2:
                self.board[61 if self.turn == "w" else 5] = self.board[63 if self.turn == "w" else 7]
                self.board[63 if self.turn == "w" else 7] = None
            elif endIndex - startIndex == -2:
                self.board[59 if self.turn == "w" else 3] = self.board[56 if self.turn == "w" else 0]
                self.board[56 if self.turn == "w" else 0] = None
        else:
            self.board[endIndex] = util.checkForPromotion(self.screen, self.board[startIndex], endIndex)
        self.board[endIndex] = self.board[startIndex]
        self.board[startIndex] = None
        self.lastMove = [startIndex, endIndex]
        self.lastMovePiece = self.board[endIndex]
        self.board[endIndex].setMoved()
        self.turnPlayed()


    def setup(self):
        self.board = [None for i in range(64)]
        self.turn = "w"
        for i in range(8):
            self.board[8+i] = pawn.Pawn("bPawn.png")
            self.board[48+i] = pawn.Pawn("wPawn.png")
        self.board[0] = rook.Rook("bRook.png")
        self.board[1] = knight.Knight("bKnight.png")
        self.board[2] = bishop.Bishop("bBishop.png")
        self.board[3] = queen.Queen("bQueen.png")
        self.board[4] = king.King("bKing.png")
        self.board[5] = bishop.Bishop("bBishop.png")
        self.board[6] = knight.Knight("bKnight.png")
        self.board[7] = rook.Rook("bRook.png")
        self.board[56] = rook.Rook("wRook.png")
        self.board[57] = knight.Knight("wKnight.png")
        self.board[58] = bishop.Bishop("wBishop.png")
        self.board[59] = queen.Queen("wQueen.png")
        self.board[60] = king.King("wKing.png")
        self.board[61] = bishop.Bishop("wBishop.png")
        self.board[62] = knight.Knight("wKnight.png")
        self.board[63] = rook.Rook("wRook.png")

        # self.board[1] = pawn.Pawn("bPawn.png")
        # self.board[61] = pawn.Pawn("wPawn.png")
        # self.board[0] = knight.Knight("bKnight.png")
        # self.board[20] = rook.Rook("bRook.png")
        # self.board[7] = rook.Rook("bRook.png")
        # self.board[63] = rook.Rook("wRook.png")
        # self.board[62] = knight.Knight("wKnight.png")
        # self.board[6] = bishop.Bishop("bBishop.png")
        # self.board[63] = bishop.Bishop("wBishop.png")
        # self.board[5] = queen.Queen("bQueen.png")
        # self.board[59] = queen.Queen("wQueen.png")
        # self.board[7+8] = king.King("bKing.png")
        # self.board[58-8] = king.King("wKing.png")
        # self.self.board[14] = pawn.Pawn("bPawn.png")