### Must copy/paste raw code into codeskulptor.org in Chrome browser to run###
# Implementation of classic arcade game Pong



import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
score1=0
score2=0
paddle1_pos = [HALF_PAD_WIDTH, HEIGHT/2]
paddle2_pos =  [WIDTH-HALF_PAD_WIDTH,HEIGHT/2]
paddle1_vel = 0 
paddle2_vel = 0 
ball_pos = [WIDTH/2, HEIGHT/2]

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    if direction == True:
        ball_vel = [-random.randrange(4,8), -random.randrange(1, 3)]
    else:
        ball_vel = [random.randrange(4,8), -random.randrange(1, 3)]
    
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints

    #reset score
    score1=0
    score2=0
    paddle1_pos = [HALF_PAD_WIDTH, HEIGHT/2]
    paddle2_pos =  [WIDTH-HALF_PAD_WIDTH,HEIGHT/2]
    paddle1_vel = 0 
    paddle2_vel = 0 
    
    #start game
    spawn_ball(LEFT)
    
def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    

    
    # update ball
    ball_pos[0] = ball_pos[0] + ball_vel[0]
    ball_pos[1] = ball_pos[1] + ball_vel[1]
        
    #keep ball on screen    
    #bounces ball off top and bottom
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1]>= HEIGHT - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    #ball on left
    if ball_pos[0] <= (PAD_WIDTH+BALL_RADIUS):
        #bounce off paddle
        if ball_pos[1] >= (paddle1_pos[1]-PAD_HEIGHT/2) and ball_pos[1] <= (paddle1_pos[1]+PAD_HEIGHT/2):
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] = 1.1* ball_vel[0]
        #lose left player
        else:
            score2 += 1
            LEFT = False
            spawn_ball(LEFT)
    #ball on right
    if ball_pos[0] >= WIDTH-(PAD_WIDTH+BALL_RADIUS):
        #bounce 
        if ball_pos[1] >= (paddle2_pos[1]-PAD_HEIGHT/2) and ball_pos[1] <= (paddle2_pos[1]+PAD_HEIGHT/2):
            ball_vel[0] = -ball_vel[0]
            ball_vel[0] = 1.1* ball_vel[0]
        #lose
        else:
            score1 += 1
            LEFT = True
            spawn_ball(LEFT)
               
        
        
    # draw ball
    c.draw_circle(ball_pos, BALL_RADIUS, 5, "Purple", "Purple")
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos[1] = paddle1_pos[1] + paddle1_vel
    paddle2_pos[1] = paddle2_pos[1] + paddle2_vel
    
    if paddle1_pos[1] > (HEIGHT-PAD_HEIGHT/2):
        paddle1_pos[1] = (HEIGHT-PAD_HEIGHT/2)
    elif paddle1_pos[1] < (PAD_HEIGHT/2):
        paddle1_pos[1] = (PAD_HEIGHT/2)
    
    if paddle2_pos[1] > (HEIGHT-PAD_HEIGHT/2):
        paddle2_pos[1] = (HEIGHT-PAD_HEIGHT/2)
    elif paddle2_pos[1] < (PAD_HEIGHT/2):
        paddle2_pos[1] = (PAD_HEIGHT/2)

    # draw paddles
    
    c.draw_line((paddle1_pos[0], paddle1_pos[1]+PAD_HEIGHT/2), (paddle1_pos[0], paddle1_pos[1]-PAD_HEIGHT/2), PAD_WIDTH, 'Orange')
    c.draw_line((paddle2_pos[0], paddle2_pos[1]+PAD_HEIGHT/2), (paddle2_pos[0], paddle2_pos[1]-PAD_HEIGHT/2), PAD_WIDTH, 'Green')
    
    # draw scores
   
    c.draw_text(str(score1), [140,50], 36, "White")
    c.draw_text(str(score2), [440,50], 36, "White")
    
    #keyboard inputs
    
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -10
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 10
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -10
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 10

    
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Reset game', new_game)

# start frame
new_game()
frame.start()
