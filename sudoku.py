# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
#matrix = [[6, 0, 9, 8, 0, 7, 0, 0, 0],
#          [0, 0, 0, 6, 0, 0, 0, 0, 1],
#          [0, 3, 5, 0, 0, 2, 0, 7, 0],
#          [0, 6, 8, 0, 0, 0, 1, 0, 2],
#          [3, 0, 0, 0, 0, 5, 0, 0, 0],
#          [0, 0, 0, 2, 0, 0, 3, 6, 0],
#          [8, 5, 4, 7, 2, 0, 6, 9, 0],
#          [0, 0, 0, 5, 9, 0, 0, 0, 8],
#          [2, 0, 6, 4, 3, 0, 7, 1, 5]]
          #matrix = [[4, 5, 3, 8, 2, 6, 1, 9, 7],
#          [8, 9, 2, 5, 7, 1, 6, 3, 4],
#          [1, 6, 7, 4, 9, 3, 5, 2, 8],
#          [7, 1, 4, 9, 5, 2, 8, 6, 3],
#          [5, 8, 6, 1, 3, 7, 2, 4, 9],
#          [3, 2, 9, 6, 8, 4, 7, 5, 1],
#          [9, 3, 5, 2, 1, 8, 4, 7, 6],
#          [6, 7, 1, 3, 4, 5, 9, 8, 2],
#          [2, 4, 8, 7, 6, 9, 3, 1, 5]]

          
matrix = [[8, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 3, 8, 6, 7, 5, 4, 9],
          [4, 7, 0, 5, 0, 3, 2, 6, 0],
          [0, 0, 0, 0, 5, 0, 9, 8, 1],
          [0, 6, 8, 9, 0, 0, 0, 0, 0],
          [7, 0, 1, 3, 4, 0, 0, 2, 0],
          [6, 0, 0, 0, 7, 0, 0, 0, 4],
          [0, 0, 7, 0, 0, 9, 0, 0, 0],
          [0, 3, 0, 0, 8, 0, 0, 1, 2]]

def isValid(matrix):
    for i in matrix:
        for y in range(1, 10):
            if y not in i:
                return False
    for y in range (0, 9):
        column = set()
        for i in range(0, 9):
            column.add(matrix[i][y])
        for z in range(1, 10):
            if z not in column:
                return False
    for i in [0, 3, 6]:
        for j in [0, 3, 6]:
            submatrixSet = submatrix(i, j)
            for z in range(1, 10):
                if z not in submatrixSet:
                    return False
    return True
def submatrix(x, y):
    submatrixSet = set()
    for i in range(0, 3):
        for j in range(0, 3):
            submatrixSet.add(matrix[x+i][y+j])
    return submatrixSet
    
def solve(matrix):
    findZeroResult = findzero(matrix) 
    if findZeroResult == None:
        return isValid(matrix)
    (x, y) = findZeroResult
    for i in range(1, 10):
        matrix[x][y] = i
        if solve(matrix):
            return True
        else:
            matrix[x][y] = 0
    
    
def findzero(matrix):
    for i in range(0, 9):
        for y in range(0, 9):
            if matrix[i][y] == 0:
                return (i, y)
    return None
solve(matrix)
print(matrix)