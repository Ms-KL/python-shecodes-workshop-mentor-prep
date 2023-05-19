# Turtle Graphics Game – Space Turtle Chomp

import turtle

# ! MODULE 1: 
#  https://tutorials.shecodes.com.au/python/space_turtle_chomp/part_1_space_turtle_chomp/

# ! STEP 5: setup screen
turtle.setup(650,650) # window size
wn = turtle.Screen() # alias for screen
wn.bgcolor('navy') #background colour

# ! STEP 6: create player turtle
player = turtle.Turtle()
player.color('darkorange')
player.shape('turtle')
player.penup() # won't leave a line as the turtle moves

# ! STEP 7: set speed variable
speed = 1

# ! STEP 8: move turtle
while True:
    player.forward(speed) # moves turtle at speed of 1

# ! RUN to test

# __________________________


