"Assignment 15 - Franks and Buns, Julie Anne Camina, 87244@gscs.ca"

#variables for how many franks/buns are in a pack, amounr of franks/buns that change depending on bns(buns) or frnk(frank amount), packs(total amount) of franks, buns, and hotdogs
franks = 0
buns = 0
bns = ""
frnk = ""
franks_in_pack = 12
buns_in_pack = 8
P_oF = franks
P_oB = buns
P_oH = ""
amount_ofFranks = ""
amount_ofBuns = ""

#setting up canvas size(350x300 px), return to redraw canvas everytime smth happens
def setup():
    size(350, 300)
    return

#colours bg to be white, makes text black, displays packs of buns/franks used, total amount of hotdogs made, makes franks, buns, franks_in_pack, and buns_in_pack into an integer
#also globalizes P_oF, P_oB, P_oH, franks, buns, franks_in_pack, buns_in_pack, amount_ofFranks, amount_ofBuns to be called on later
def draw():
    background(255)
    fill(0)
    text('pack(s) of franks', 40, 60)
    text('pack(s) of buns', 230, 60)
    text('hotdogs made', 135, 150)
    global P_oF, P_oB, P_oH, franks, buns, franks_in_pack, buns_in_pack, amount_ofFranks, amount_ofBuns
    franks = int(franks)
    buns = int(buns)
    franks_in_pack = int(franks_in_pack)
    buns_in_pack = int(buns_in_pack)
    text(P_oF, 70, 90)
    text(P_oB, 270, 90)
    text(P_oH, 170, 180)
    make_hotdogs()

#depending on what key is pressed(f, g, b, n) increases or decreases amount of buns/franks, changes P_oB/P_oF to display current amount of buns/franks
def keyPressed():
    global franks, frnk, P_oF, buns, bns, P_oB, amount_ofFranks, amount_ofBuns, franks_in_pack, buns_in_pack
    if key == 'f':
        frnk = (franks + 1)
        franks = frnk
        P_oF = frnk
        return amount_ofFranks
        
    if key == 'g':
        frnk = (franks - 1)
        franks = frnk
        P_oF = frnk
        return amount_ofFranks
        
    if key == 'b':
        bns = (buns + 1)
        buns = bns
        P_oB = bns
        return amount_ofBuns
        
    if key == 'n':
        bns = (buns - 1)
        buns = bns
        P_oB = bns
        return amount_ofBuns

#function that calculates amount of buns/ franks that are in each pack depending on user input, finds amount of hotdogs made and changes P_oH to display total amount of dogs.
def make_hotdogs():
    global P_oH
    amount_ofBuns = bns * buns_in_pack
    amount_ofFranks = frnk * franks_in_pack
    make_hotdogs = min(amount_ofBuns, amount_ofFranks)
    P_oH = make_hotdogs
    print(make_hotdogs)
    return make_hotdogs, P_oH
