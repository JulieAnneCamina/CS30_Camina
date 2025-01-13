foods = ["Bread", "Doughnut", "Muffin", "COOKIE"]
price = [5, 2, 3, 1]
order = []
a = [""]
cost = 0

def setup():
    size(500, 500)
    return

def cookies(x, y):
    fill(220, 145, 94)
    ellipse(x - 35, y + 45, 50, 50)
    fill(0)
    ellipse(x-35, y+45, 10, 10)
    ellipse(x-55, y+50, 10, 10)
    ellipse(x-20, y+35, 10, 10)
    ellipse(x-30, y+62, 10, 10)
    ellipse(x-45, y+28, 10, 10)
    
def monster(x, y):
    fill(51, 153, 255)
    ellipse(x, y + 90, 145, 190)
    fill(51, 153, 255)
    ellipse(x, y - 10, 110, 70)
    fill(255)
    ellipse(x - 15, y - 40, 30, 30)
    ellipse(x + 15, y - 40, 30, 30)
    fill(0)
    ellipse(x - 15, y - 45, 10, 10)
    ellipse(x + 15, y - 30, 10, 10)
    ellipse(x, y , random(40, 70), random(20, 30))

def menu():
    fill(0)
    textSize(20)
    text('MENU', 90, 80)
    textSize(11)
    text(foods[0], 90, 110)
    text(": $", 120, 110)
    text(price[0], 135, 110)
    text(foods[1], 90, 125)
    text(": $", 145, 125)
    text(price[1], 160, 125)
    text(foods[2], 90, 140)
    text(": $", 125, 140)
    text(price[2], 140, 140)
    text(foods[3], 90, 155)
    text(": $", 135, 155)
    text(price[3], 150, 155)

def userOrder():
    global order
    fill(0)
    textSize(20)
    text('YOUR ORDER', 300, 80)
    textSize(11)
    text(min(a), 300, 110)
    
def keyPressed():
    global order, cost, a
    if key == 'b':
        a.pop("")
        order.append(foods[0])
        a.append(foods[0])
        cost = cost + 5
        print(order)
    elif key == 'd':
        order.append(foods[1])
        a.append(foods[1])
        cost = cost + 2
        print(order)
    elif key == 'm':
        order.append(foods[2])
        a.append(foods[2])
        cost = cost + 3
        print(order)
    elif key == 'c':
        order.append(foods[3])
        a.append(foods[3])
        cost = cost + 1
        print(order)
    elif key == 'u':
        order.pop()
        print(order)

def draw():
    global a
    background(255)
    monster(100, 400)
    cookies(135, 370)
    menu()
    userOrder()
    line(250, 0, 250, 500)
    text('Cost: $', 400, 470)
    text(cost, 450, 470)
