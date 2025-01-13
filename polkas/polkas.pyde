dotX = []
dotY = []
r = [255, 255, 255]
g = [255, 255, 255]
b = [255, 255, 255]

def setup():
    size(400, 400)
    return
                                 
def mousePressed():
    global dotX ,dotY
    dotX.append(mouseX)
    dotY.append(mouseY)
    
def keyPressed():
    global r, g ,b
    if key == 'p':
        randomNum1 = int(random(0, 256))
        randomNum2 = int(random(0, 256))
        randomNum3 = int(random(0, 256))
        r.remove(r[0])
        g.remove(g[0])
        b.remove(b[0])
        r.append(randomNum1)
        g.append(randomNum2)
        b.append(randomNum3)
        return
        
def draw():
    global dotX, dotY, r, g, b
    for i in range(len(dotX)):
        fill(min(r), min(g), min(b))
        ellipse(dotX[i], dotY[i], 20, 20)
    print(dotX, dotY)
    print(r, g, b)
