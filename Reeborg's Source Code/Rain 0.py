from library import turn_right
from library import move_x
from library import turn_around

for r in range(0,6):
    move()
build_wall()
turn_around()
for r in range(0,5):
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
        
def turn_around():
    turn_left()
    turn_left()  