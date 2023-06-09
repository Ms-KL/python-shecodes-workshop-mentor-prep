# Turtle Graphics Game – Space Turtle Chomp

# ! MODULE 1: 
#  https://tutorials.shecodes.com.au/python/space_turtle_chomp/part_1_space_turtle_chomp/

# ! MODULE 2:
# https://tutorials.shecodes.com.au/python/space_turtle_chomp/part_2__turn_baby_turn/

# ! MODULE 3:
# https://tutorials.shecodes.com.au/python/space_turtle_chomp/part_3__know_your_boundaries_turtle/

# ! MODULE 4:
# https://tutorials.shecodes.com.au/python/space_turtle_chomp/part_4__whats_the_turtle_chomping/

# ! MODULE 5:
# https://tutorials.shecodes.com.au/python/space_turtle_chomp/part_5__collisions_become_a_function/

# ! MODULE 6:
# https://tutorials.shecodes.com.au/python/space_turtle_chomp/part_6__setting_boundary_for_cabbage/

# ! MODULE 7:
# https://tutorials.shecodes.com.au/python/space_turtle_chomp/part_7__more_cabbage_more/

# ! MODULE 8:
# https://tutorials.shecodes.com.au/python/space_turtle_chomp/part_8__creating_space_and_sound/

# ! MODULE 9:
# https://tutorials.shecodes.com.au/python/space_turtle_chomp/part_9__keeping_score/

# ! MODULE 10:
# https://tutorials.shecodes.com.au/python/space_turtle_chomp/part_10__creating_your_opponent/

# ! MODULE 11:
# https://tutorials.shecodes.com.au/python/space_turtle_chomp/part_11__60_second_countdown/

# __________________________

import turtle
import math # ! STEP 4.5
import random # ! STEP 4.7
import winsound # ! STEP 8.6
import time # ! STEP 11.1

# ! STEP 1.5: setup screen
# Setup Screen
turtle.setup(650,650) # window size
wn = turtle.Screen() # alias for screen
wn.bgcolor('black') # ! STEP 8.4: change background color
wn.bgpic('assets/kbgame-bg.gif') # ! STEP 8.3: add background image

# ! STEP 7.6: stop screen from being jumpy due to refreshing of multiple foods.
# tells computer not to refresh screen each time and speeds up animation
wn.tracer(3)

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
player.speed(0) # 0 = fastest animation speed

# ! STEP 10.1: create opponent:
# Create opponent turtle
comp = turtle.Turtle()
comp.color('red')
comp.shape('turtle')
comp.penup()
comp.setposition(random.randint(-290, 290), random.randint(-290, 290))

# ! STEP 10.8: create competition score
# Create competition score
mypen2 = turtle.Turtle()
mypen2.color('red')
mypen2.hideturtle()


# Create variable score
score = 0 # ! STEP 9.1: create player score
comp_score = 0 # ! STEP 10.7

# ! STEP 7.1: create empty list to count for max number of cabbages
maxFoods = 10
foods = [] 

# ! STEP 7.2: for loop to count and move food until maxFoods number is reached
# this ends up foods.[1] = object, foods.[2] = object etc until max foods is reached
for count in range(maxFoods):
    new_food = turtle.Turtle()
    new_food.shapesize(.5) # ! STEP 8.4: reduce the size of food
    new_food.color("lightgreen")
    new_food.shape("circle")
    new_food.penup()
    new_food.speed(0)
    new_food.setposition(random.randint(-290, 290), random.randint(-290, 290))
    foods.append(new_food)

speed = 1 # ! STEP 1.7: set speed variable
# Set game time limit for 1 minute (6 * 10 seconds)
timeout = time.time() + 10*6 # ! STEP 10.2

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

# ! STEP 5.1: convert collision checking into function
def isCollision(t1, t2):
    '''
    If t1 and t2 are in the same location, they collide = True.
    
    Arguments:
    * t1 = turtle
    * t2 = food
    '''
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if d < 20:
        return True
    else:
        return False

# ! STEP 2.2: set keyboard binding
turtle.listen() # listen for keystroke (onkey method)
turtle.onkey(turn_left, 'Left')
turtle.onkey(turn_right, 'Right')
turtle.onkey(increase_speed, 'Up')

# ! STEP 2.8.b: decrease speed using down arrow
turtle.onkey(decrease_speed, 'Down')

# ! STEP 1.8: move turtle
while True:

    # ! STEP 11.3
    # gametime goes up by 1 for each loop until it reaches 6
    # if gametime reaches 6 or if timeout variable above is less than the time its taken, stop the loop. 
    gametime = 0
    if gametime == 6 or time.time() > timeout:
        break
    gametime = gametime - 1


    # ! STEP 10.3
    player.forward(speed) # moves turtle at speed of 1
    comp.forward(2) # moves opponent turtle at speed of 2 # ! STEP 10.3

    # ! STEP 3.4: boundary detection & turtle bounce
    # boundary player checking x coordinate (bounce turtle off x/left and right edges)
    if player.xcor() > 290 or player.xcor() < -290:
        # ! STEP 3.5: change angle of turtle when it hits boundary
        player.right(120) # turn turtle around 100 degrees
        # ! STEP 8.7: play sound fx with boundary bounce
        winsound.PlaySound('assets/bounce.wav', winsound.SND_ASYNC)
    
    # boundary player checking y coordinate (bounce turtle off y/top and bottom edges)
    if player.ycor() > 290 or player.ycor() < -290:
        # ! STEP 3.5: change angle of turtle when it hits boundary
        player.right(180) # turn turtle around 100 degrees
        # ! STEP 8.7: play sound fx with boundary bounce
        winsound.PlaySound('assets/bounce.wav', winsound.SND_ASYNC)
    

    # ! STEP 10.5: replicate boundary checking to competitor
    # boundary comp checking x coordinate (bounce turtle off x/left and right edges)
    if comp.xcor() > 290 or comp.xcor() < -290:
        comp.right(100) # turn turtle around 100 degrees
        winsound.PlaySound('assets/bounce.wav', winsound.SND_ASYNC)
    
    # boundary comp checking y coordinate (bounce turtle off y/top and bottom edges)
    if comp.ycor() > 290 or comp.ycor() < -290:
        comp.right(100) # turn turtle around 100 degrees
        winsound.PlaySound('assets/bounce.wav', winsound.SND_ASYNC)

    # ! STEP 7.3: move food as many times as there are foods in the food list
    # Move food around
    for food in foods:
        food.forward(3)

    # ! STEP 7.3: indent -->
        # ! STEP 6.6: change angle of food when it hits boundary (bounce food off edges)
        # Boundary Food Checking x coordinate
        if food.xcor() > 290 or food.xcor() < -290:
            food.right(180)
            # ! STEP 8.7: play sound fx with boundary bounce
            winsound.PlaySound('assets/bounce.wav', winsound.SND_ASYNC)

        # Boundary Food Checking y coordinate
        if food.ycor() > 290 or food.ycor() < -290:
            food.right(180) 
            # ! STEP 8.7: play sound fx with boundary bounce
            winsound.PlaySound('assets/bounce.wav', winsound.SND_ASYNC)
        
        # ! STEP 7.4: Move and indent
        if isCollision(player, food):
            food.setposition(random.randint(-290, 290), random.randint(-290, 290))
            food.right(random.randint(0, 360))
            # ! STEP 8.7: play sound fx when turtle collides with food
            winsound.PlaySound('assets/chomp.wav', winsound.SND_ASYNC)
            score +=1 # ! STEP 9.2: add score for every collision

            # ! STEP 9.3: draw the score for every collision
            # Draw the score on the screen
            mypen.undo() #! STEP 9.4: undo previous draw to stop layering
            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(-290, 310)
            scorestring ="Score: %s" % score
            mypen.write(scorestring, False, align='left', font=('Arial', 14, 'normal'))
        
        # ! STEP 10.10: duplicate collision checking for comp
        if isCollision(comp, food):
            food.setposition(random.randint(-290, 290), random.randint(-290, 290))
            food.right(random.randint(0, 360))
            winsound.PlaySound('assets/chomp.wav', winsound.SND_ASYNC)
            comp_score +=1 
            mypen2.undo() 
            mypen2.penup()
            mypen2.hideturtle()
            mypen2.setposition(200, 305)
            scorestring ="Score: %s" % score
            mypen2.write(scorestring, False, align='left', font=('Arial', 14, 'normal'))

# ! STEP 11.5: Declare winner or loser
if (int(score) > int(comp_score)):
    mypen.setposition(0, 0)
    mypen.color("yellow")
    mypen.write("Game Over: You WIN", False, align="center", font=("Arial", 28, "normal"))
else:
    mypen.setposition(0, 0)
    mypen.color("yellow")
    mypen.write("Game Over: You LOSE", False, align="center", font=("Arial", 28, "normal"))

delay = input("Press Enter to finish.")




# ! ----------- Replaced Code:

# # ! STEP 4.1: create food --> REPLACED WITH STEP 7.2
# food = turtle.Turtle()
# food.color('lightgreen')
# food.shape('circle') # cabbage for turtle to eat and gain points
# food.penup()
# food.speed(0) # immediately draw food on screen

# # ! STEP 4.3: set food position --> REPLACED WITH STEP 4.10
# # food.setposition(-100, 100) # set position of food (instead of same position as turtle) --> REPLACE with STEP 4.10

# # ! STEP 4.10: set food position to random position on screen --> REPLACED WITH STEP 7.2
# food.setposition(random.randint(-290, 290), random.randint(-290, 290)) # random position on screen (away from border and turtle)
    
    # # ! STEP 4.6: collision checking --> REMOVED and REPLACED WITH STEP 5.2
    # # calculate distance between turtle and food
    # # this formula is the distance formula between two points and uses pythagorean theorem
    # d = math.sqrt( 
    #         math.pow( # square root of sum of squares
    #             player.xcor() # x coordinate
    #                 -food.xcor(),2) # square of x coordinate
    #         + 
    #         math.pow( # square root of sum of squares
    #             player.ycor() # y coordinate
    #                 -food.ycor(),2)) # square of y coordinate
    
    # if d < 20: # if distance is less than 20 pixels

    #     # food.hideturtle() # hide food when turtle eats it --> REMOVED AND REPLACED WITH STEP 4.8

    #     # ! STEP 4.8: move turtle after eating food  --> REMOVED and REPLACED WITH STEP 5.2
    #     food.setposition(random.randint(-290, 290), random.randint(-290, 290)) # move food to random position on screen (away from border and turtle)

    # # ! STEP 5.2: collision checking using new function from step 5.1 (replaced steps 4.6 + 4.8)
    #     # ! STEP 6.3: have food move fom a random position ---> MOVED. SEE STEP 7.4
    # if isCollision(player, food):
    #     food.setposition(random.randint(-290, 290), random.randint(-290, 290))
    #     food.right(random.randint(0, 360))


    # ! STEP 6.1: move food around screen --> REPLACED WITH STEP 7.3
    # ! STEP 6.4: make food move faster (From 1 to 3) --> REPLACED WITH STEP 7.3
    # food.forward(4)

# ! RUN to test

# __________________________



