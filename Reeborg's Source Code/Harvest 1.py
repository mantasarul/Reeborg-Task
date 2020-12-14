def turn_right():
    for r in range(0,3):
        turn_left()
def move_x(x):
    for x in range(0,x):
        move()

turn_left()
move_x(2)
turn_right()
move_x(2)
def harvest_one_row():
    while object_here():
        if "carrot":
            take()
            move()
    else:
        turn_left()
        turn_left()
        move_x(6)
        turn_right()
        move()
        turn_right()
        
        
for r in range(0,6):
    harvest_one_row()

        

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
