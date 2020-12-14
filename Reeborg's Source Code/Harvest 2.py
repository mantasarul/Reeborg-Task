def turn_right():
    for r in range(0,3):
        turn_left()
def move_x(x):
    for x in range(0,x):
        move()

turn_left()
move_x(2)
turn_right()
move()
def harvest_one_row():
    
    for r in range(0,7):
        while object_here():
            take()
        else:
            move()
    turn_left()
    turn_left()
    move_x(7)
    turn_right()
    move()
    turn_right()
    #pass
        
for r in range(0,6):
    harvest_one_row()

        

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
