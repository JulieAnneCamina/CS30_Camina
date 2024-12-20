n_square = 25

def setup():
    size(400,400)
    return
    
def draw():
    noStroke()
    background(125)
    for i in range(n_square):
        if i % 2 == 0:
            fill(255)
        elif i % 2 == 1:
            fill(0)
        rect(0, i*n_square, 25, 25)
        
        if i % 2 == 0:
            fill(255)
        elif i % 2 == 1:
            fill(0)
        rect(i*n_square, 0, 25, 25)
    
def keyPressed():
    global n_square
    if key == '-':
        n_square = n_square - 2
        
    if key == '+':
        n_square = n_square + 1
