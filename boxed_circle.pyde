"Assignment 14, Julie Anne Camina, 87244@gscs.ca"

#variables that is the size of the circle(d), and the border width/height
d = 50
border = 50

#sets up size of canvas and makes shapes have no outline
def setup():
    size(400, 300)
    noStroke()
   
#draws background, 2 blue borders on left side and bottom, draws a 50x50 yellow circle that follows mouse
def draw():
    background(0, 0, 0)
    fill(0, 0, 225)
    global border
    rect(0, 0, border, height)
    rect(0, 250, width, border)
    fill(255, 255, 0)
    ellipse(max(mouseX, 75, d), min(mouseY, 225, 230), d, d)
    
