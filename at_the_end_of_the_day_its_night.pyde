"Assignment 9 - Day/Night Scene, Julie Anne Camina, 87244@gscs.ca"

#func to setup size and the morning scene
def setup():
    size(300, 300)
    background(94, 148, 255)
    noStroke()
    morning_scene()

#func that makes sure canvas is redrawn
def draw():
    return

#func that draws morning scene (sun, 3 different coloured squares, and dirt ground)
def morning_scene():
    fill(255, 199, 44)
    ellipse(40, 40, 50, 50)
    fill(161, 78, 22)
    rect(0, 250, 300, 50)
    fill(255, 153, 51)
    rect(40, 200, 50, 50)
    fill(0, 255, 0)
    rect(120, 200, 50, 50)
    fill(153, 51, 255)
    rect(200, 200, 50, 50)

#func that draws night scene (moon, 3 darker coloured squares, night sky, darker coloured ground)
def night_scene():
    background(0, 0, 153)
    fill(250)
    ellipse(40, 40, 50, 50)
    fill(115, 54, 19)
    rect(0, 250, 300, 50)
    fill(204, 102, 0)
    rect(40, 200, 50, 50)
    fill(0, 200, 0)
    rect(120, 200, 50, 50)
    fill(102, 0, 204)
    rect(200, 200, 50, 50)

#func that changes scene from morning to night on key press    
def keyPressed():
    night_scene()
