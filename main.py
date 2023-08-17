import pygame, sys, math, board, util, ai, logic

pygame.init()

width = 800
height = 800
fps = 120

gameRunning = True

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Chess')

clock = pygame.time.Clock()

board = board.Board(screen)

ai = ai.AI()

def displayBoard(board):
    for x in range(8):
        for y in range(8):
            if board.board[util.getIndexFromRowCol(x, y)] is not None:
                print(type(board.board[util.getIndexFromRowCol(x, y)]).__name__ + " ", end="")
            else:
                print("    ")
        print("\n")


while gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                index = util.getIndexFromClick(pygame.mouse.get_pos())
                moveMade = board.userMove(index)
                

                if moveMade:
                    board.display()
                    pygame.display.flip()
                    result = logic.checkForCheckmate(board.board, board.turn, board.lastMove)
                    if result == 1:
                        print("White wins - Checkmate")
                        gameRunning = False
                    elif result == 2:
                        print("White draw - Stalemate")
                        gameRunning = False

                    (startIndex, endIndex), fitness = ai.minimax(board.board, 4, -math.inf, math.inf, True, board.lastMove)
                    # (startIndex, endIndex), fitness = ai.iterativeDeepening(board.board, 5, board.lastMove)

                    board.computerMove(startIndex, endIndex)
                    print("actual:", fitness)

                    result = logic.checkForCheckmate(board.board, board.turn, board.lastMove)
                    if result == 1:
                        print("Black wins - Checkmate")
                        gameRunning = False
                    elif result == 2:
                        print("Black draw - Stalemate")
                        gameRunning = False

                    # (startIndex, endIndex), fitness = ai.minimax(board.board, 4, -math.inf, math.inf, False, board.lastMove)
                    # print(startIndex, endIndex, fitness)
                    

    board.display()
    pygame.display.flip()
    clock.tick(fps)

board.display()
pygame.display.flip()
clock.tick(fps)