from library import turn_right
from library import move_x
from library import turn_around

def up_3_steps():
    for r in range(0,3):
        turn_left()
        move()
        turn_right()
        move_x(2)
        
def down_3_steps():
    for r in range(0,3):
        move_x(2)
        turn_left()
        move()
        turn_right()
        
take()
up_3_steps()

while object_here():
    take()
put("star")
turn_around()
down_3_steps()
    

        


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