def setup():
    size(500, 500)
    background(255)

def pink_circle():
    stroke(204, 0, 102)
    fill(255, 0, 127)
    ellipse(mouseX, mouseY, 10, 10)
    
def purple_circle():
    stroke(102, 0, 204)
    fill(153, 51, 255)
    ellipse(mouseX, mouseY, 10, 10)

def draw():
    purple_circle()
    
def mouseClicked():
    pink_circle()
    
def keyPressed():
    purple_circle()


def draw():
    return
