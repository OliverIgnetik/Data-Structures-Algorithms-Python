
################ TIME COMPLEXITY ######################
# T = O(8^(N*N))

################ SPACE COMPLEXITY ######################
# S = O(N*N)

################ IMPLEMENTATION ######################

def genLegalMoves(x, y, visited, bdSize):
    newMoves = []
    # generic movesets
    moveOffsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
                   (1, -2), (1, 2), (2, -1), (2, 1)]
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        # check if each of the new moves are legal positions on the board
        if legalCoord(newX, bdSize) and legalCoord(newY, bdSize) and visited[newX][newY] == 0:
            newMoves.append((newX, newY))
    return newMoves


def legalCoord(x, bdSize):
    if x >= 0 and x < bdSize:
        return True
    else:
        return False


def KnightTour(visited, row, col, move, bdSize):
    # print out visited array when you are done
    if (move == bdSize**2):
        for i in range(bdSize):
            for j in range(bdSize):
                print('{:<3d}'.format(visited[i][j]), end=" ")
            print('\n')
        return True
    else:
        newPositions = genLegalMoves(row, col, visited, bdSize)
        for newMove in newPositions:
            new_row, new_col = newMove[0], newMove[1]
            move += 1
            visited[new_row][new_col] = move
            if (KnightTour(visited, new_row, new_col, move, bdsize)):
                return True
            # backtrack
            move -= 1
            visited[new_row][new_col] = 0

    return False


bdsize = 5
visited = [[0 for _ in range(bdsize)] for _ in range(bdsize)]

# start position
visited[0][0] = 1

print('KNIGHTS TOUR')
print('-' * 60)
KnightTour(visited, 0, 0, 1, bdsize)
