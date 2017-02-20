import math


def print_matrix( matrix ):
    finString = ""
    for row in matrix:
        finString += "| "
        for col in row:
            finString += str(col) + " "
        finString += "|\n"
    print(finString)

def ident( matrix ):
    for row in range( len( matrix ) ):
        for col in range( len( matrix[row] ) ):
            if row == col:
                matrix[row][col] = 1
            else:
                matrix[row][col] = 0

def scalar_mult( matrix, s ):
    for row in range( len( matrix ) ):
        for col in range( len( matrix[row] ) ):
            matrix[row][col] = matrix[row][col] * s;

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    for col in range( len( m2[0] ) ):
        for row in range( len( m2 ) ):
            m2[row][col] = multRowCol( m1[row], m2, col)
    
    
def multRowCol( m1Row, m2, m2Col ):
    sum = 0;
    for index in range( len( m1Row ) ):
        sum += m1Row[index] * m2[index][m2Col];
    return sum;

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
