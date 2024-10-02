"Assignment 12 - House Placemen, Julie Anne Camina, 87244@gscs.ca"

#func that sets up canvas to be 400x400 px, makes sure canvas is redrawn via return
def setup():
    size(400, 400)
    return

#func that colours bg to be dark green, draws func draw_woods, and func draw_house based on mouse's (x,y) coords   
def draw():
    background(10, 110, 10)
    draw_woods()
    draw_house(mouseX, mouseY)

#func that draws a 10x40 brown rectangle based on specified coords, and green circle based on specified (x+4, y) coords
def draw_tree(x, y):
    fill(108, 44, 11)
    rect(x, y, 10, 40)
    fill(55, 166, 55)
    ellipse(4 + x, y, 40, 40)

#func that draws a white 70x50 rectangle, a red 20x30 rectangle on top, and a blue trangle; that follows mouse's (x,y) coords
def draw_house(x, y):
    fill(255)
    rect(x - 30, y - 10, 70, 50)
    fill(255, 0, 0)
    rect(x - 5, 10 + y, 20, 30)
    fill(0, 0, 225)
    triangle(x - 30, y - 10, x + 5, y - 40, x + 40, y - 10)

#func that draws a 150x80 blue circle, and calls on func draw_trees 5 times on different (x,y) coords
def draw_woods():
    fill(51, 166, 233)
    ellipse(290, 290, 150, 80)
    draw_tree(350, 50)
    draw_tree(100, 30)
    draw_tree(60, 250)
    draw_tree(200, 300)
    draw_tree(300, 200)
    
