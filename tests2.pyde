a = 1
b = 1

def setup():
    size(150, 90)
    background(0)
    
def draw_target(row, column):
    ellipse(column*30-15, row*30-15, 30, 30)
    
def layout_targets():
    global a, b
    for i in range(a):
        for j in range(b):
            if i == 0:
                fill(255,0,0)
            else:
                fill(0, 0, 255)
            draw_target(i+1, j+1)
            
def draw():
    layout_targets()
    
def keyPressed():
    global a, b
    if key == '-':
        a = a + 1
        b = b + 1
        print(a, b)
        return
        
    if key == 'k':
        a = a - 1
        b = b - 1
        print(a, b)
        return
        
