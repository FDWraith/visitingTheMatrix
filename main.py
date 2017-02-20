from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

print_matrix(matrix)

add_edge( matrix, 0, 250, 0, 500, 250, 0)
add_edge( matrix, 250, 0, 0, 250, 500, 0)

print_matrix(matrix) 

draw_lines( matrix, screen, color )

identMatrix = new_matrix()
ident( identMatrix )

print_matrix( identMatrix )

newMatrix = new_matrix()
ident( newMatrix )
scalar_mult( newMatrix, 7 )

print_matrix( newMatrix )

matrix_mult( identMatrix, newMatrix )

print_matrix( newMatrix )

matrix_mult( identMatrix, matrix )

print_matrix( matrix )

matrix_mult( newMatrix, matrix )

print_matrix( matrix )

display(screen)
