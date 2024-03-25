import sys
import copy

# Swap the values W and B to play for black
W = 'B'
B = 'W'
x = 'x'
INF = float('inf')
num_positions_evaluated = 0  # Add this global variable to keep track of the count

def generateMovesOpening(board):
    return generateAdd(board)

def generateMovesMidgameEndgame(board):
    if board.count(W) == 3:
        return generateHopping(board)
    else:
        return generateMove(board)

def generateAdd(board):
    L = []
    for idx, pos in enumerate(board):
        if pos == "x":
            b = list(board) # Copy the board
            b[idx] = W
            if closeMill(idx, b):
                generateRemove(b, L)
            else:
                L.append(b)
    return L

def generateHopping(board):
    L = []
    for idx_a, pos_a in enumerate(board):
        if pos_a == W:
            for idx_b, pos_b in enumerate(board):
                if pos_b == "x":
                    b = list(board)
                    b[idx_a] = "x"
                    b[idx_b] = W
                    if closeMill(idx_b, b):
                        generateRemove(b, L)
                    else:
                        L.append(b)
    return L

def generateMove(board):
    L = []
    for idx, pos in enumerate(board):
        if pos == W:
            neighbors = get_neighbors(idx)
            for j in neighbors:
                if board[j] == "x":
                    b = list(board)
                    b[idx] = "x"
                    b[j] = W
                    if closeMill(j, b):
                        generateRemove(b, L)
                    else:
                        L.append(b)
    return L

def generateRemove(board, L):
    found = False
    for idx, pos in enumerate(board):
        if pos == B:
            if not closeMill(idx, board):
                found = True
                b = list(board)
                b[idx] = "x"
                L.append(b)
    if not found:
        L.append(board)

def get_neighbors(location):
    neighbors = {
        0: [1, 6],
        1: [0, 11],
        2: [7, 3],
        3: [2, 10],
        4: [8, 5],
        5: [4, 9],
        6: [0, 7, 18],
        7: [2, 6, 8, 15],
        8: [7, 4, 12],
        9: [5, 10, 14],
        10: [3, 9, 11,17],
        11: [1, 10, 20],
        12: [8, 13],
        13: [12, 16, 14],
        14: [13, 9],
        15: [7, 16],
        16: [13, 15, 17, 19],
        17: [16, 10],
        18: [6, 19],
        19: [18, 20, 16],
        20: [19, 11]
    }
    return neighbors.get(location, [])

def closeMill(j, board):
    C = board[j]
    mills = {
        0: [[6, 18]],
        1: [[11, 20]],
        2: [[7, 15]],
        3: [[10, 17]],
        4: [[8, 12]],
        5: [[9, 14]],
        6: [[0, 18], [7, 8]],
        7: [[2, 15], [6, 8]],
        8: [[6, 7], [4, 12]],
        9: [[10, 11], [5, 14]],
        10: [[9, 11],[3, 17]],
        11: [[1, 20], [9, 10]],
        12: [[8, 4], [14, 13]],
        13: [[12, 14], [16, 19]],
        14: [[9, 5], [12, 13]],
        15: [[2, 7], [16, 17]],
        16: [[15, 17], [13, 19]],
        17: [[15, 16], [3, 10]],
        18: [[0, 6], [19, 20]],
        19: [[13, 16], [18, 20]],
        20: [[18, 19], [1, 11]]
    }
    for mill in mills.get(j, []):
        if all(board[idx] == C for idx in mill):
            return True
    return False

def staticEstimationMidgameEndgame(board):
    global num_positions_evaluated
    num_positions_evaluated += 1
    numWhitePieces = board.count(W)
    numBlackPieces = board.count(B)
    L = generateMovesMidgameEndgame(board)
    numBlackMoves = len(L)
    
    if numBlackPieces <= 2: 
        return 10000
    elif numWhitePieces <= 2: 
        return -10000
    elif numBlackMoves == 0: 
        return 10000
    else: 
        return 1000 * (numWhitePieces - numBlackPieces) - numBlackMoves

def staticEstimationOpening(board):
    global num_positions_evaluated
    num_positions_evaluated += 1
    numWhitePieces = board.count(W)
    numBlackPieces = board.count(B)
    return numWhitePieces - numBlackPieces

def minimaxOpening(position, depth, isMax):
    if depth == 0:
        return staticEstimationOpening(position), position

    board_positions = generateMovesOpening(position)
    if isMax:
        maxEval = -INF
        maxPosition = None
        for pos in board_positions:
            evaluation, _ = minimaxOpening(pos, depth-1, False)
            if evaluation > maxEval:
                maxEval = evaluation
                maxPosition = pos
        return maxEval, maxPosition
    else:  
        minEval = INF
        minPosition = None
        for pos in board_positions:
            evaluation, _ = minimaxOpening(pos, depth-1, True)
            if evaluation < minEval:
                minEval = evaluation
                minPosition = pos
        return minEval, minPosition

def main():
    global num_positions_evaluated
    num_positions_evaluated = 0
    if len(sys.argv) != 4:
        print("Usage: python minimax_opening.py <input-board-file> <output-board-file> <depth>")
        return

    input_file, output_file, depth = sys.argv[1], sys.argv[2], int(sys.argv[3])

    with open(input_file, 'r') as f:
        position = list(f.read().strip())

    estimate, best_position = minimaxOpening(position, depth, True)

    with open(output_file, 'w') as f:
        f.write(''.join(best_position))

    print(f"Board Position: {''.join(best_position)}")
    print(f"Positions evaluated by static estimation: {num_positions_evaluated}.")
    print(f"MINIMAX estimate: {estimate}.")

if __name__ == "__main__":
    main()

