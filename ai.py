import math, copy, random, util, logic, time
from typing import List, Tuple
from pieces import piece, pawn, knight, bishop, rook, queen, king

class AI:
    def __init__(self):
        self.pawnValue = 200
        self.knightValue = 640
        self.bishopValue = 660
        self.rookValue = 1000
        self.queenValue = 18000
        self.kingValue = 40000

        self.wPawnPositionalValue = [0,  0,  0,  0,  0,  0,  0,  0,
                                    50, 50, 50, 50, 50, 50, 50, 50,
                                    10, 10, 20, 30, 30, 20, 10, 10,
                                    5,  5, 10, 25, 25, 10,  5,  5,
                                    0,  0,  0, 20, 20,  0,  0,  0,
                                    5, -5,-10,  0,  0,-10, -5,  5,
                                    5, 10, 10,-20,-20, 10, 10,  5,
                                    0,  0,  0,  0,  0,  0,  0,  0]
        self.wKnightPositionalValue = [-50,-40,-30,-30,-30,-30,-40,-50,
                                    -40,-20,  0,  0,  0,  0,-20,-40,
                                    -40,  0, 10, 15, 15, 10,  0,-40,
                                    -30,  5, 15, 20, 20, 15,  5,-30,
                                    -30,  0, 15, 20, 20, 15,  0,-30,
                                    -40,  5, 10, 15, 15, 10,  5,-40,
                                    -40,-20,  0,  5,  5,  0,-20,-40,
                                    -50,-40,-30,-30,-30,-30,-40,-50]
        self.wBishopPositionalValue = [-20,-10,-10,-10,-10,-10,-10,-20,
                                    -10,  0,  0,  0,  0,  0,  0,-10,
                                    -10,  0,  5, 10, 10,  5,  0,-10,
                                    -10,  5,  5, 10, 10,  5,  5,-10,
                                    -10,  0, 10, 10, 10, 10,  0,-10,
                                    -10, 10, 10, 10, 10, 10, 10,-10,
                                    -10,  5,  0,  0,  0,  0,  5,-10,
                                    -20,-10,-10,-10,-10,-10,-10,-20]
        self.wRookPositionalValue = [0,  0,  0,  0,  0,  0,  0,  0,
                                    5, 10, 10, 10, 10, 10, 10,  5,
                                    -5,  0,  0,  0,  0,  0,  0, -5,
                                    -5,  0,  0,  0,  0,  0,  0, -5,
                                    -5,  0,  0,  0,  0,  0,  0, -5,
                                    -5,  0,  0,  0,  0,  0,  0, -5,
                                    -5,  0,  0,  0,  0,  0,  0, -5,
                                    0,  0,  0,  5,  5,  0,  0,  0]
        self.wQueenPositionalValue = [-20,-10,-10, -5, -5,-10,-10,-20,
                                    -10,  0,  0,  0,  0,  0,  0,-10,
                                    -10,  0,  5,  5,  5,  5,  0,-10,
                                    -5,  0,  5,  5,  5,  5,  0, -5,
                                    0,  0,  5,  5,  5,  5,  0, -5,
                                    -10,  5,  5,  5,  5,  5,  0,-10,
                                    -10,  0,  5,  0,  0,  0,  0,-10,
                                    -20,-10,-10, -5, -5,-10,-10,-20]
        self.wKingPositionalValue = [-30,-40,-40,-50,-50,-40,-40,-30,
                                    -30,-40,-40,-50,-50,-40,-40,-30,
                                    -30,-40,-40,-50,-50,-40,-40,-30,
                                    -30,-40,-40,-50,-50,-40,-40,-30,
                                    -20,-30,-30,-40,-40,-30,-30,-20,
                                    -10,-20,-20,-20,-20,-20,-20,-10,
                                    20, 20,  0,  0,  0,  0, 20, 20,
                                    20, 30, 10,  0,  0, 10, 30, 20]
        
        self.bPawnPositionalValue = [0,  0,  0,  0,  0,  0,  0,  0,
                                    5, 10, 10,-20,-20, 10, 10,  5,
                                    5, -5,-10,  0,  0,-10, -5,  5,
                                    0,  0,  0, 20, 20,  0,  0,  0,
                                    5,  5, 10, 25, 25, 10,  5,  5,
                                    10, 10, 20, 30, 30, 20, 10, 10,
                                    50, 50, 50, 50, 50, 50, 50, 50,
                                    0,  0,  0,  0,  0,  0,  0,  0]
        self.bKnightPositionalValue = [-50,-40,-30,-30,-30,-30,-40,-50
                                    -40,-20,  0,  5,  5,  0,-20,-40,
                                    -40,  5, 10, 15, 15, 10,  5,-40,
                                    -30,  0, 15, 20, 20, 15,  0,-30,
                                    -30,  5, 15, 20, 20, 15,  5,-30,
                                    -40,  0, 10, 15, 15, 10,  0,-40,
                                    -40,-20,  0,  0,  0,  0,-20,-40,
                                    -50,-40,-30,-30,-30,-30,-40,-50,]
        self.bBishopPositionalValue = [-20,-10,-10,-10,-10,-10,-10,-20,
                                    -10,  5,  0,  0,  0,  0,  5,-10,
                                    -10, 10, 10, 10, 10, 10, 10,-10,
                                    -10,  0, 10, 10, 10, 10,  0,-10,
                                    -10,  5,  5, 10, 10,  5,  5,-10,
                                    -10,  0,  5, 10, 10,  5,  0,-10,
                                    -10,  0,  0,  0,  0,  0,  0,-10,
                                    -20,-10,-10,-10,-10,-10,-10,-20]
        self.bRookPositionalValue = [0, 0, 0, 5, 5, 0, 0, 0,
                                    -5, 0, 0, 0, 0, 0, 0, -5,
                                    -5, 0, 0, 0, 0, 0, 0, -5,
                                    -5, 0, 0, 0, 0, 0, 0, -5,
                                    -5, 0, 0, 0, 0, 0, 0, -5,
                                    -5, 0, 0, 0, 0, 0, 0, -5,
                                    5, 10, 10, 10, 10, 10, 10, 5,
                                    0, 0, 0, 0, 0, 0, 0, 0]
        self.bQueenPositionalValue = [-20,-10,-10, -5, -5,-10,-10,-20,
                                    -10, 0, 0, 0, 0, 0, 0,-10,
                                    0, -5, 5, 5, 5, 5, 0,-10,
                                    -5, 0, 5, 5, 5, 5, 0,-10,
                                    -5, 0, 5, 5, 5, 5, 0, 0,
                                    -10, 0, 5, 5, 5, 5, 5,-10,
                                    -10, 0, 0, 0, 0, 5, 0,-10,
                                    -20,-10,-10, -5, -5,-10,-10,-20]
        self.bKingPositionalValue = [20, 30, 10,  0,  0, 10, 30, 20,
                                    20, 20,  0,  0,  0,  0, 20, 20,
                                    -10,-20,-20,-20,-20,-20,-20,-10,
                                    -20,-30,-30,-40,-40,-30,-30,-20,
                                    -30,-40,-40,-50,-50,-40,-40,-30,
                                    -30,-40,-40,-50,-50,-40,-40,-30,
                                    -30,-40,-40,-50,-50,-40,-40,-30,
                                    -30,-40,-40,-50,-50,-40,-40,-30]
        
        self.pieceKeys = {}
        for pieceType in ["K", "Q", "R", "B", "N", "P"]:
            for i in range(64):
                self.pieceKeys[(pieceType, i)] = random.getrandbits(64)
        self.squareKey = random.getrandbits(64)
        self.transpostionTable = {}


    def iterativeDeepening(self, board: List[piece.Piece | None], targetDepth: int, lastMove: List[int]) -> Tuple[Tuple[int], int]:
        currentDepth = 1
        bestMove = None
        bestAlpha = -math.inf
        bestBeta = math.inf
        while currentDepth <= targetDepth:
            move, score = self.minimax(board, currentDepth, bestAlpha, bestBeta, True, lastMove)
            if move is not None:
                if currentDepth % 2 == 0:
                    bestBeta = score
                else: 
                    bestAlpha = score
                bestMove = move
            currentDepth += 1
            print(bestMove, bestAlpha)
        return bestMove, bestAlpha


    def minimax(self, originalBoard: List[piece.Piece | None], currentDepth: int, alpha: int, beta: int, aiTurn: bool, lastMove: List[int]) -> Tuple[Tuple[int], int]:
        if currentDepth == 0 or logic.checkForCheckmate(originalBoard, "b" if aiTurn else "w", lastMove):
            return None, self.compareToTranspostionTable(originalBoard, "b" if aiTurn else "w")
        
        if aiTurn:
            maxEval = -math.inf
            bestMove = None
            for move in self.generateAllPossibleMoves(originalBoard, "b", lastMove):
                board = self.makeMove(originalBoard, move)
                eval = self.minimax(board, currentDepth-1, alpha, beta, False, lastMove)[1]
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
                if eval > maxEval:
                    maxEval = eval
                    bestMove = move
            return bestMove, maxEval
        else:
            minEval = math.inf
            bestMove = None
            for move in self.generateAllPossibleMoves(originalBoard, "w", lastMove):
                board = self.makeMove(originalBoard, move)
                eval = self.minimax(board, currentDepth-1, alpha, beta, True, lastMove)[1]
                beta = min(beta, eval)
                if beta <= alpha:
                    break
                if eval < minEval:
                    minEval = eval
                    bestMove = move
            return bestMove, minEval

    def generateAllPossibleMoves(self, board: List[piece.Piece | None], turn: str, lastMove: List[int]) -> Tuple[int]:
        for x in range(64):
            if util.checkForFriend(board, turn, x, piece.Piece):
                for y in range(64):
                   if logic.checkForValidMove(board, turn, board[x], x, y, None, None, lastMove):
                        yield (x, y)

    def fitnessFunction(self, board: List[piece.Piece | None], turn: str) -> int:
        fitness = 0

        whiteMaterial = self.countMaterial(board, "w")
        blackMaterial = self.countMaterial(board, "b")
        fitness += blackMaterial - whiteMaterial if turn == "w" else whiteMaterial - blackMaterial

        whitePositionalScore = self.getPositionalScore(board, "w")
        blackPositionalScore = self.getPositionalScore(board, "b")
        fitness += blackPositionalScore - whitePositionalScore if turn == "w" else whitePositionalScore - blackPositionalScore
        
        fitness += self.getProtectedScore(board, turn)
        fitness += self.getAttackScore(board, turn)
        fitness += self.getAttackedScore(board, turn)

        fitness += 5 if logic.checkForCheck(board, turn, None, util.locateKing(board, turn, None)) else 0
        
        return fitness
    
    def countMaterial(self, board: List[piece.Piece | None], turn: str):
        material = 0
        for x in range(64):
            if util.checkForFriend(board, turn, x, pawn.Pawn):
                material += self.pawnValue
            elif util.checkForFriend(board, turn, x, knight.Knight):
                material += self.knightValue
            elif util.checkForFriend(board, turn, x, bishop.Bishop):
                material += self.bishopValue
            elif util.checkForFriend(board, turn, x, rook.Rook):
                material += self.rookValue
            elif util.checkForFriend(board, turn, x, queen.Queen):
                material += self.queenValue
            elif util.checkForFriend(board, turn, x, king.King):
                material += self.kingValue
        return material
    
    def getPositionalScore(self, board: List[piece.Piece | None], turn: str):
        score = 0
        for x in range(64):
            if turn == "w":
                if util.checkForFriend(board, turn, x, pawn.Pawn):
                    score += self.wPawnPositionalValue[x]
                elif util.checkForFriend(board, turn, x, knight.Knight):
                    score += self.wKnightPositionalValue[x]
                elif util.checkForFriend(board, turn, x, bishop.Bishop):
                    score += self.wBishopPositionalValue[x]
                elif util.checkForFriend(board, turn, x, rook.Rook):
                    score += self.wRookPositionalValue[x]
                elif util.checkForFriend(board, turn, x, queen.Queen):
                    score += self.wQueenPositionalValue[x]
                elif util.checkForFriend(board, turn, x, king.King):
                    score += self.wKingPositionalValue[x]
            else:
                if util.checkForFriend(board, turn, x, pawn.Pawn):
                    score += self.bPawnPositionalValue[x]
                elif util.checkForFriend(board, turn, x, knight.Knight):
                    score += self.bKnightPositionalValue[x]
                elif util.checkForFriend(board, turn, x, bishop.Bishop):
                    score += self.bBishopPositionalValue[x]
                elif util.checkForFriend(board, turn, x, rook.Rook):
                    score += self.bRookPositionalValue[x]
                elif util.checkForFriend(board, turn, x, queen.Queen):
                    score += self.bQueenPositionalValue[x]
                elif util.checkForFriend(board, turn, x, king.King):
                    score += self.bKingPositionalValue[x]
        return score
    
    def getProtectedScore(self, board: List[piece.Piece | None], turn: str):
        score = 0
        for x in range(64):
            if logic.checkForCheck(board, "w" if turn == "b" else "b", None, x):
                if util.checkForFriend(board, turn, x, pawn.Pawn):
                    score += self.pawnValue / 10
                elif util.checkForFriend(board, turn, x, knight.Knight):
                    score += self.knightValue / 10
                elif util.checkForFriend(board, turn, x, bishop.Bishop):
                    score += self.bishopValue / 10
                elif util.checkForFriend(board, turn, x, rook.Rook):
                    score += self.rookValue / 10
                elif util.checkForFriend(board, turn, x, queen.Queen):
                    score += self.queenValue / 10
                elif util.checkForFriend(board, turn, x, king.King):
                    score += self.kingValue / 10
        return score

    def getAttackScore(self, board: List[piece.Piece | None], turn: str):
        score = 0
        for x in range(64):
            if logic.checkForCheck(board, "w" if turn == "w" else "b", None, x):
                if util.checkForEnemy(board, turn, x, pawn.Pawn):
                    score += self.pawnValue / 10
                elif util.checkForEnemy(board, turn, x, knight.Knight):
                    score += self.knightValue / 10
                elif util.checkForEnemy(board, turn, x, bishop.Bishop):
                    score += self.bishopValue / 10
                elif util.checkForEnemy(board, turn, x, rook.Rook):
                    score += self.rookValue / 10
                elif util.checkForEnemy(board, turn, x, queen.Queen):
                    score += self.queenValue / 10
                elif util.checkForEnemy(board, turn, x, king.King):
                    score += self.kingValue / 10
        return score
    
    def getAttackedScore(self, board: List[piece.Piece | None], turn: str):
        score = 0
        for x in range(64):
            if logic.checkForCheck(board, "w" if turn == "w" else "b", None, x):
                if util.checkForFriend(board, turn, x, pawn.Pawn):
                    score -= self.pawnValue / 10
                elif util.checkForFriend(board, turn, x, knight.Knight):
                    score -= self.knightValue / 10
                elif util.checkForFriend(board, turn, x, bishop.Bishop):
                    score -= self.bishopValue / 10
                elif util.checkForFriend(board, turn, x, rook.Rook):
                    score -= self.rookValue / 10
                elif util.checkForFriend(board, turn, x, queen.Queen):
                    score -= self.queenValue / 10
                elif util.checkForFriend(board, turn, x, king.King):
                    score -= self.kingValue / 10
        return score
    
    def hashBoard(self, board: List[piece.Piece | None]):
        h = 0
        for i, piece in enumerate(board):
            if piece:
                h ^= self.pieceKeys[(piece.getSymbol(), i)]
        h ^= self.squareKey
        return h
    
    def compareToTranspostionTable(self, board: List[piece.Piece | None], turn: str):
        hash = self.hashBoard(board)
        if hash in self.transpostionTable:
            return self.transpostionTable[hash]
        fitness = self.fitnessFunction(board, turn)
        self.transpostionTable[hash] = fitness
        return fitness
            

    def makeMove(self, board: List[piece.Piece | None], move: Tuple[int]) -> List[piece.Piece | None]:
        newBoard = copy.deepcopy(board)
        newBoard[move[1]] = newBoard[move[0]]
        newBoard[move[0]] = None
        return newBoard