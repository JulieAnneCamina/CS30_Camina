"Assignment 10 - Pin tail on donkey, Julie Anne Camina, 87244@gscs.ca"

#func that sets up the bg, size of canvas and draws the donkey immediately when program starts
def setup():
    background(153)
    size(400, 400)
    draw_donkey()

#func that makes sure canvas is redrawn
def draw():
    return

#func that draws donkey
def draw_donkey():
    fill(131, 68, 32)
    rect(130, 160, 40, 40)
    rect(145, 220, 20, 55)
    rect(155, 220, 20, 55)
    rect(220, 220, 20, 55)
    rect(230, 220, 20, 55)
    ellipse(200, 200, 140, 60)
    ellipse(150, 125, 15, 55)
    ellipse(160, 125, 15, 55)
    ellipse(130, 155, 80, 40)

#func that draws donkey's tail on mouse's (x,y) coords
def donkey_tail():
    fill(196, 109, 59)
    rect(mouseX, mouseY, 10, 40)
    fill(255, 0, 0)
    ellipse(mouseX, mouseY, 10, 10)

#func that draws donkey tail on mouse press
def mousePressed():
    donkey_tail()

#func that erases all donkey's tails on screen
def keyPressed():
    background(153)
    draw_donkey()
    

    
    
