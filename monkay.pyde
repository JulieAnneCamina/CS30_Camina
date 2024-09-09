size(500, 500)

def colour_pc():
    stroke(0)
    fill(160, 160, 160)
    
def sc1():
    stroke(153, 0, 0)
    fill(255, 0, 0)
    
def sc2():
    stroke(0, 153, 0)
    fill(0, 255, 0)
    
def sc3():
    stroke(0, 0, 153)
    fill(0, 0, 255)

def draw_ear(x, y):
    ellipse(x, y, 50, 50)
    ellipse(x, y, 30, 30)
    
def draw_eye(x, y):
    stroke(0)
    fill(0)
    ellipse(x, y, 10, 10)
    
def b1(x, y):
    sc1()
    ellipse(x, y, 10, 10)
    
def b2(x, y):
    sc2()
    ellipse(x, y, 10, 10)
    
def b3(x, y):
    sc3()
    ellipse(x, y, 10, 10)
    
def draw_arms():
    colour_pc()
    rect(110, 150, 100, 20)
    rect(260, 150, 100, 20)

def draw_body():
    colour_pc()
    ellipse(235, 210, 100, 165)
    rect(195, 190, 80, 50)
    b1(220, 210)
    b2(235, 210)
    b3(250, 210) 
    
def draw_head():
    colour_pc()
    draw_ear(190, 80)
    draw_ear(280, 80)
    ellipse(235, 80, 95, 95)
    draw_eye(215, 85)
    draw_eye(255, 85)
    










draw_arms()
draw_head()
draw_body()
