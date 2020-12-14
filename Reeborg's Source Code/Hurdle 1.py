from library import turn_right
from library import move_x
from library import left
from library import right

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()

        

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
def turn_right():
    for r in range(0,3):
        turn_left()
        
def move_x(x):
    for x in range(0,x):
        move()

def left():
    for r in range(0,2):
        turn_left()
        move()
        
def right():
    for r in range(0,2):
        turn_right()
        move()  
        
  