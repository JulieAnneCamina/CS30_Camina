""" Assignment 5 - Checkerboard """

#making canvas white and 200x200
size(200, 200)
background(255)

#function that draws a black square on (x, y) coords
def draw_black_square(x, y):
    fill(0)
    rect(x, y, 50, 50)

#calls function draw_black_square to specified coords
draw_black_square(50, 0)
draw_black_square(150, 0)
draw_black_square(0, 50)
draw_black_square(100, 50)
draw_black_square(50, 100)
draw_black_square(150, 100)
draw_black_square(0, 150)
draw_black_square(100, 150)
