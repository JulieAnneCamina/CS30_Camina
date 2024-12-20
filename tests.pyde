n_checks = 2
row = 4
column = 4

def setup():
    size(400,400)
    background(125)
    return
    
def draw():
    noStroke()
    b_w()
    
def draw_target(row, column):
    rect(column*25-50, row*25-50, 25, 25)
    
def b_w():
    global n_checks
    for i in range(row+column):
        for j in range(row+column):
            if i % 2 == 0 and j % 2 == 1:
                fill(255)
            elif i % 2 == 1 and j % 2 == 0:
                fill(0)
        draw_target(n_checks+i, n_checks+j)
    
def keyPressed():
    global n_checks, row, column
    
    if key == '+':
        n_checks = n_checks - 1
        column = column - 1
        row = row - 1
        return
    if key == '-':
        n_checks = n_checks - 1
        column = column + 1
        row = row + 1
        return
