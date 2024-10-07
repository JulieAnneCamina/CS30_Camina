"Assignment 11 - Model-View-Controller, Julie Anne Camina, 87244@gscs.ca"

#variables for background colour, circle colour, x & y coords, etc
bg = 255
b = bg
c = 50
d = 255
cg = d
x = 150
y = 150

#setting up canvas to be 300x300 px, returns to redraw canvas
def setup():
    size(300, 300)
    return

#globalizes b, draws background and blue_circle
def draw():
    global b
    background(b, 0, 0)
    blue_circle()

#function that globalizes d, x, y for colour, and (x, y) coords of the circle
def blue_circle():
    global d, x, y
    fill(0, 0, d)
    ellipse(x, y, 60, 60)

#changes circle's coords depending on where mouse is clicked on canvas    
def mouseClicked():
    global x, y
    x = mouseX
    y = mouseY
    blue_circle()

#globalizes bg, b, c, cg, d, changes colour of background depending if d or r is pressed, changes circle colour depending if b or n is pressed
def keyPressed():
    global bg, b, c, cg, d
    if key == 'd':
        b = bg - c
        bg = b
        
    if key == 'r':
        b = bg + c
        bg = b
        
    if key == 'n':
        d = cg - c
        cg = d
        
    if key == 'b':
        d = cg + c
        cg = d
