from library import turn_right
from library import move_x
from library import turn_around

move()
turn_right()
move()

while not at_goal():
    if not wall_on_right():
        turn_right()
        build_wall()
        turn_left()
    elif front_is_clear():
        move()
    else:
        turn_left()
        
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
        
def turn_around():
    turn_left()
    turn_left()  