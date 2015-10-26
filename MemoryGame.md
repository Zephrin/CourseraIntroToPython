# implementation of card game - Memory

import simplegui
import random

#initialize variables
pos=0
exposed = []
image = simplegui.load_image('https://dl.dropboxusercontent.com/u/15519798/Pumpkin.jpg')
clicks=0
state=0
turns=0
labelturns=""
for x in range(16):
    exposed.append(False)

# helper function to initialize globals
def new_game():
    global cards, exposed, turns,state
    cards = range(0,8) + range (0,8)
    random.shuffle(cards)
    #print cards
    
    #define exposed cards
    for x in range(16):
        exposed[x]=(False)
    turns=0
    label.set_text("Turns = "+str(turns))
    state=0
        
def checkcard(clickspot):
    global exposed, state
    for x in range(16):
        if clickspot[0]//50 == x:
            if not exposed[clickspot[0]//50]:
                exposed[x] = True   
                state +=1
                return x
            else:
                state=0
                return x

# define event handlers
def mouseclick(clickspot):
    global clicks, exposed, card1, card2, state, turns
    
    if state ==0:
        #card1 = checkcard(clickspot)
        for x in range(16):
            if clickspot[0]//50 == x:
                if not exposed[clickspot[0]//50]:
                    exposed[x] = True   
                    state =1
                    card1 = x
                                    
    elif state==1:
        #card2 = checkcard(clickspot)
        for x in range(16):
            if clickspot[0]//50 == x:
                if not exposed[clickspot[0]//50]:
                    exposed[x] = True   
                    state = 2
                    card2 = x        
    else:
        if cards[card1] == cards[card2]:
            #print "yay"
        else:
            exposed[card1] = False
            exposed[card2] = False
        
        for x in range(16):
            if clickspot[0]//50 == x:
                if not exposed[clickspot[0]//50]:
                    exposed[x] = True   
                    state = 1
                    card1 = x 
                else:
                    state = 0
                    
             
        turns += 1
        
        label.set_text("Turns = "+str(turns))
        
        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global pos
    for num in cards:
        
        if exposed[pos]:
            canvas.draw_text(str(num), (5+pos*50, 80), 88, 'Red')
        else:
            canvas.draw_image(image, (1224/2, 2448/2), (1224, 2448), (25+pos*50, 50), (45,95))
            canvas.draw_polygon([[1+pos*50, 1], [49+pos*50, 1], [49+pos*50, 99], [1+pos*50, 99]], 2, 'White')
        #loops position of drawing numbers
        pos +=1
        if pos == 16:
            pos = 0
   
    
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", new_game)
label = frame.add_label("Turns = 0")


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
