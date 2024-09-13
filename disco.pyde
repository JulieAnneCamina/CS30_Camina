"Assignment 8 - Disco Towers, Julie Anne Camina, 87244@gscs.ca"

#func to setup normal tower, size and colour of canvas
def setup():
    size(255, 255)
    background(57, 67, 134)
    draw_tower()
    fill(255, 255, 0)
    draw_windows()

#func that makes sure canvas is redrawn
def draw():
    return

#func that draws tower
def draw_tower():
    fill(107, 108, 118)
    rect(70, 0, 120, 255)

#func that draws windows
def draw_windows():
    rect(80, 20, 40, 60)
    rect(140, 20, 40, 60)
    rect(80, 100, 40, 60)
    rect(140, 100, 40, 60)
    rect(80, 180, 40, 60)
    rect(140, 180, 40, 60)

#func that changes windows colour on mouse click and based on x,y coords of mouse
def mouseClicked():
    fill(mouseY, mouseX, 0)
    draw_windows()
