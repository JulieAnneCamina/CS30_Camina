"Assignment 6, Julie Anne Camina, 87244@gscs.ca"

#making canvas white and 500x500
size(500, 500)
background(255)

#function that draws a red 10x10 circle on (x,y) coords
def b1(x, y):
    fill(255, 0, 0)
    ellipse(x, y, 10, 10)

#function that draws a green 10x10 circle on (x,y) coords
def b2(x, y):
    fill(0, 255, 0)
    ellipse(x, y, 10, 10)

#function that draws a blue 10x10 circle on (x,y) coords
def b3(x, y):
    fill(0, 0, 255)
    ellipse(x, y, 10, 10)
    
#function that draws 2 circles stacked on each other on (x,y) coords
def draw_ear(x, y):
    ellipse(x, y, 50, 50)
    ellipse(x, y, 30, 30)

#function that colours a shape in grayscale
def primary_colour(pc):
    fill(pc)

#function that colours a shape in rgb
def secondary_colour(sc1, sc2, sc3):
    fill(sc1, sc2, sc3)

#function that makes a 10x10 black circle on (x,y) coords
def draw_eye(x, y):
    stroke(0)
    fill(0)
    ellipse(x, y, 10, 10)

#function that makes a 40x40 circle on (x,y) coords
def draw_handfoot(x, y):
    ellipse(x, y, 40, 40)

#function that draws shapes w/ primary_colour & secondary_colour to fill shapes w/ colour, draws 2 rectangles and calls on func draw_handfoot to draw arms
def draw_arms(pc, sc1, sc2, sc3):
    primary_colour(pc)
    rect(120, 150, 100, 15)
    rect(260, 150, 100, 15)
    secondary_colour(sc1, sc2, sc3)
    draw_handfoot(350, 160)
    draw_handfoot(125, 160)

#function that draws shapes w/ primary_colour & secondary_colour to fill shapes w/ colour, draws 2 rectangles and calls on func draw_handfoot to draw legs
def draw_legs(pc, sc1, sc2, sc3):
    primary_colour(pc)
    rect(200, 270, 15, 100)
    rect(250, 270, 15, 100)
    secondary_colour(sc1, sc2, sc3)
    draw_handfoot(205, 355)
    draw_handfoot(260, 355)

#function that draws shapes w/ primary_colour to fill shapes w/ colour, draws 1 rectangle, circle and func b1, b2, b3 to draw body & buttons
def draw_body(pc):
    primary_colour(pc)
    ellipse(235, 210, 100, 165)
    rect(195, 190, 80, 50)
    b1(220, 210)
    b2(235, 210)
    b3(250, 210)

#function that draws shapes w/ primary_colour to fill shapes w/ colour, draws circle and calls on func draw_eye to make face
def draw_head(pc):
    primary_colour(pc)
    draw_ear(190, 80)
    draw_ear(280, 80)
    ellipse(235, 80, 95, 95)
    draw_eye(215, 85)
    draw_eye(255, 85)

#function that draws shapes w/ functions primary_colour, secondary_colour, draw_arms, draw_legs, draw_body, draw_head to make monkey
def draw_beep_boopers(pc, sc1, sc2, sc3):
    secondary_colour(sc1, sc2, sc3)
    primary_colour(pc)
    draw_arms(pc, sc1, sc2, sc3)
    draw_legs(pc, sc1, sc2, sc3)
    draw_body(pc)
    draw_head(pc)
    

#calls on func draw_beep_boopers to make monkey, colours monkey using specified colours
draw_beep_boopers(200, 200, 160, 0)
