"Assignment 12 - Square of Number, Julie Anne Camina, 87244@gscs.ca"

#empty variables to be called on later, digit_string for inputted number by user, number = digit_sting turned into an integer, squared = digit_string squared, n1, n2, t1, t2 are a variables to show text depending on mouseClicked or keyPressed
digit_string = ""
number = ""
squared = ""
n1 = ""
t1 = ""
t2 = ""
n2 = ""


#setting up canvas to be 200x200 px, also returns to redraw canvas
def setup():
    size(200, 200)
    return

#globalizes and draws n1, n2, t1, t2 and draws background to be black
def draw():
    global n1, n2, t1, t2
    background(0)
    text(n1, 100, 40)
    text(t1, 20, 40)
    text(t2, 120, 40)
    text(n2, 135, 40)

#when mouse is clicked, makes inputted digits (digit_string) into an integer to be squared, also displayes text that says "The square of (input number) is (squared number), also clears digit_string to be reused by user
#also globalizes n1, n2, t1, t2, digit_string, number, squared
def mouseClicked():
    global digit_string, number, squared, n1, n2, t1, t2
    number = int(digit_string)
    squared = (number * number)
    t1 = "The square of"
    n1 = digit_string
    t2 = "is"
    n2 = squared
    digit_string = ""

#when a key(number) is pressed, shows what key the user pressed, also clears n1, n2, t2
#also globalizes n1, n2, t1, t2, digit_string and makes text white
def keyPressed():
    fill(255)
    global digit_string, n1, n2, t1, t2
    digit_string = (digit_string + key)
    t1 = digit_string
    n1 = ""
    t2 = ""
    n2 = ""


    
    




    
