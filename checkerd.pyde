size(200, 200)

def draw_black_square(x, y):
    fill(0)
    rect(x, y, 50, 50)
    
def draw_white_square(x, y):
    noStroke()
    fill(255)
    rect(x, y, 50, 50)

draw_white_square(0, 0)
draw_black_square(50, 0)
draw_white_square(100, 0)
draw_black_square(150, 0)
draw_black_square(0, 50)
draw_white_square(50, 50)
draw_black_square(100, 50)
draw_white_square(150, 50)
draw_white_square(0, 100)
draw_black_square(50, 100)
draw_white_square(100, 100)
draw_black_square(150, 100)
draw_black_square(0, 150)
draw_white_square(50, 150)
draw_black_square(100, 150)
draw_white_square(150, 150)
