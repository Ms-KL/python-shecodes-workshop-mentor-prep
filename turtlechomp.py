# Turtle Graphics Game – Space Turtle Chomp

import turtle

# ! STEP 4.5: import math module
import math

# ! STEP 4.7: import random module
import random

# ! MODULE 1: 
#  https://tutorials.shecodes.com.au/python/space_turtle_chomp/part_1_space_turtle_chomp/

# ! MODULE 2:
# https://tutorials.shecodes.com.au/python/space_turtle_chomp/part_2__turn_baby_turn/

# ! MODULE 3:
# https://tutorials.shecodes.com.au/python/space_turtle_chomp/part_3__know_your_boundaries_turtle/

# ! MODULE 4:
# https://tutorials.shecodes.com.au/python/space_turtle_chomp/part_4__whats_the_turtle_chomping/
# __________________________

# ! STEP 1.5: setup screen
turtle.setup(650,650) # window size
wn = turtle.Screen() # alias for screen
wn.bgcolor('navy') #background colour

# ! STEP 3.2: draw border
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300,-300) # bottom left corner
mypen.pendown()
# ! STEP 3.5: change border thickness and color
mypen.pensize(6)
mypen.color('yellow')
mypen.speed(0) # fastest speed (instant draw of border - remove to see border being drawn)
for side in range(4): # draw square (repeat loop/side 4 times)
    mypen.forward(600) # length of square
    mypen.left(90) # angle of square
mypen.hideturtle() # hide turtle

# ! STEP 1.6: create player turtle
player = turtle.Turtle()
player.color('darkorange')
player.shape('turtle')
player.penup() # won't leave a line as the turtle moves

# ! STEP 2.7: fix turtle from jumping when arrow keys are pressed
player.speed(0) # 0 = fasted animation speed

# ! STEP 4.1: create food 
food = turtle.Turtle()
food.color('lightgreen')
food.shape('circle') # cabbage for turtle to eat and gain points
food.penup()
food.speed(0) # immediately draw food on screen

# ! STEP 4.3: set food position
# food.setposition(-100, 100) # set position of food (instead of same position as turtle) --> REPLACE with STEP 4.10

# ! STEP 4.10: set food position to random position on screen
food.setposition(random.randint(-290, 290), random.randint(-290, 290)) # random position on screen (away from border and turtle)

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

# ! STEP 2.8.a: decrease speed using down arrow
def decrease_speed():
    global speed # moving out of local function into global environment
    speed -= 1 # increase speed by 1 with every keystroke up

# ! STEP 2.2: set keyboard binding
turtle.listen() # listen for keystroke (onkey method)
turtle.onkey(turn_left, 'Left')
turtle.onkey(turn_right, 'Right')
turtle.onkey(increase_speed, 'Up')

# ! STEP 2.8.b: decrease speed using down arrow
turtle.onkey(decrease_speed, 'Down')

# ! STEP 1.8: move turtle
while True:
    player.forward(speed) # moves turtle at speed of 1

    # ! STEP 3.4: boundary detection & turtle bounce
    # boundary player checking x coordinate (bounce turtle off x/left and right edges)
    if player.xcor() > 290 or player.xcor() < -290:
        # ! STEP 3.5: change angle of turtle when it hits boundary
        player.right(100) # turn turtle around 100 degrees
    
    # boundary player checking y coordinate (bounce turtle off y/top and bottom edges)
    if player.ycor() > 290 or player.ycor() < -290:
        # ! STEP 3.5: change angle of turtle when it hits boundary
        player.right(100) # turn turtle around 100 degrees
    
    # ! STEP 4.6: collision checking
    # calculate distance between turtle and food
    # this formula is the distance formula between two points and uses pythagorean theorem
    d = math.sqrt( 
            math.pow( # square root of sum of squares
                player.xcor() # x coordinate
                    -food.xcor(),2) # square of x coordinate
            + 
            math.pow( # square root of sum of squares
                player.ycor() # y coordinate
                    -food.ycor(),2)) # square of y coordinate
    
    if d < 20: # if distance is less than 20 pixels

        # food.hideturtle() # hide food when turtle eats it --> REMOVED AND REPLACED WITH STEP 4.8

        # ! STEP 4.8: move turtle after eating food
        food.setposition(random.randint(-290, 290), random.randint(-290, 290)) # move food to random position on screen (away from border and turtle)

# ! RUN to test

# __________________________



