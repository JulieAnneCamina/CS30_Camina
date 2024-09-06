""" Assignment 4 - Functions and Abstractions """

#function that draws a square at defined coords (50, 50)
def draw_fixed_square():
    rect(50, 50, 50, 50)
    
#function that draws a circle on coords (x, y) with a diameter of (d)
def draw_circle(x, y, d):
    ellipse(x, y, d, 100)

#function that draws 3 circles on top of each other on coords (x, y)
def draw_concentric_circles(x, y):
    ellipse(x, y, 90, 90)
    ellipse(x, y, 60, 60)
    ellipse(x, y, 30, 30)
    
#function calls to draw a square, a singular circle, and a stack of 3 circles
size(350, 350)
draw_fixed_square()
draw_circle(250, 250, 100)
draw_concentric_circles(250, 100)
