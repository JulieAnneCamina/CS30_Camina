"Assignment 7, Julie Anne Camina, 87244@gscs.ca"

#func to make canvas 300x300 px
def setup():
    size(300, 300)

#func that draws 100x100 px blue circle on mouse's x,y coords
def big_circle():
    fill(84, 168, 252)
    ellipse(mouseX, mouseY, 100, 100)

#func that draws 50x50 px green circle on top of big_circle on mouse's x,y coords
def small_circle():
    fill(80, 240, 68)
    ellipse(mouseX, mouseY, 50, 50)

#func that calls on big_circle & small_circle to make a singular copy of circles to follow the mouse
def draw():
    background(40)
    big_circle()
    small_circle()

    

    
