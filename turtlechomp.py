# Turtle Graphics Game – Space Turtle Chomp

import turtle

# ! MODULE 1: 
#  https://tutorials.shecodes.com.au/python/space_turtle_chomp/part_1_space_turtle_chomp/

# ! MODULE 2:
# https://tutorials.shecodes.com.au/python/space_turtle_chomp/part_2__turn_baby_turn/

# __________________________

# ! STEP 1.5: setup screen
turtle.setup(650,650) # window size
wn = turtle.Screen() # alias for screen
wn.bgcolor('navy') #background colour

# ! STEP 1.6: create player turtle
player = turtle.Turtle()
player.color('darkorange')
player.shape('turtle')
player.penup() # won't leave a line as the turtle moves

# ! STEP 1.7: set speed variable
speed = 1

# ! STEP 2.3: define functions for moving turtle
def turn_left():
    player.left(30) # move turtle by 30 degrees when left arrow is pressed

def turn_right():
    player.right(30) # move turtle by 30 degrees when right arrow is pressed

def increase_speed():
    global speed # moving out of local function into global environment
    speed += 1 # increase speed by 1 with every keystroke up

# ! STEP 2.2: set keyboard binding
turtle.listen() # listen for keystroke (onkey method)
turtle.onkey(turn_left, 'Left')
turtle.onkey(turn_right, 'Right')
turtle.onkey(increase_speed, 'Up')

# ! STEP 1.8: move turtle
while True:
    player.forward(speed) # moves turtle at speed of 1

# ! RUN to test

# __________________________



