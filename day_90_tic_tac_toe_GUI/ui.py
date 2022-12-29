from turtle import *
from main import *
import random

window = Screen()
window.title("Tic Tac Toe")
window.setup(width=635, height=425)
window.bgpic("images/board.gif")
window.addshape("images/pencil.gif")

# current_player either 1/2
player = 1
boxes = []
game_on = True
winner = None

# print(window.window_width(), int(0.3*window.window_width()))

# screen lines
vertical_one = (-60.00, 160.00)
vertical_two = (60.00, 160.00)
horizontal_one = (-240, 50)
horizontal_two = (-240, -50)

# grids
grid = [ (-150, 50), (-35, 50), (70, 50)
,(-150, -60), (-35, -60), (70, -60)
,(-150, -165), (-35, -165), (70, -165)]


def draw_vert():
    pen.seth(270)
    pen.pd()
    pen.forward(320)
    pen.pu()

def draw_hori():
    pen.seth(0)
    pen.pd()
    pen.forward(480)
    pen.pu()

def draw_lines():
    # this function draw the lines on the board at the beggining of the game
    pen.setpos(vertical_one)
    draw_vert()
    pen.goto(vertical_two)
    draw_vert()
    pen.setpos(horizontal_one)
    draw_hori()
    pen.goto(horizontal_two)
    draw_hori()


def animate(winner):
    if winner == 1:
        t = Turtle()
        t.pu()
        window.bgpic("images/heart_woman.gif")
        hideturtle()
        window.update()
    elif winner == 2:
        t = Turtle()
        # showturtle()
        t.pu()
        t.goto(0 , -80)
        t.pd()
        t.color("red")
        t.begin_fill()
        t.fillcolor("red")
        t.setheading(140)
        t.forward(180)
        t.circle(-90 , 200)

        t.seth(60)

        t.circle(-90 , 200)
        t.forward(180)
        t.end_fill()

        t.goto(-0 , 147)
        t.color("white")
        t.speed(4)
        t.pensize(9)
        t.seth(300)
        t.forward(60)
        t.seth(200)
        t.forward(80)
        t.seth(340)
        t.forward(100)
        t.seth(190)
        t.forward(90)
        t.seth(330)
        t.forward(60)
        t.seth(190)
        t.forward(50)
        t.seth(340)
        t.forward(50)
        t.seth(245)
        t.forward(40)
    else:
        t = Turtle()
        # showturtle()
        t.pu()
        t.goto(0,-80)
        t.pd()
        t.color("red")
        t.begin_fill()
        t.fillcolor("red")
        t.setheading(140)
        t.forward(180)
        t.circle(-90, 200)

        t.seth(60)

        t.circle(-90 , 200)
        t.forward(180)
        t.end_fill()


def check_winner(player):
    global game_on
    global winner

    # if length is 9 all boxes are filled its a draw
    # print (f"Game on {game_on}, Boxes: {len(boxes)}")
    if len(boxes) == 9:
        game_on = False
        winner = "Draw"

    # check winner when at least 4 pieces are placed because we are using set length to get winner
    if len(boxes) > 4:
        pieces = ['O', 'X']
        piece = pieces[player-1]
        # print(player, piece)
        winner = get_winner(player, piece)
        # print("Winner: ",winner)
        if winner != None:
            game_on = False

    #     draw animation when the game is over or drew
    if game_on != True:
        animate(winner)



def pick_random_box():
    return random.choice(range(1,10))


def play(box_num):
    global player
    global boxes
    global game_on
    global winner

    # animate when there is a winner
    if winner != None:
        animate()

    # # if the boxes list has 9 items it is a draw
    # if len(boxes) == 9:
    #     #     draw
    #     game_on = False
    #     winner = "Draw"

    if game_on:
        # playing occurs when the game is not won nor drew
        if player == 1:
            piece = "O"
            color_ = "white"
            fontsize = 100

        elif player == 2:
            piece = "X"
            color_ = "red"
            fontsize = 100

        box = grid[box_num-1]

        # if box is clicked ignore
        if box not in boxes:
            boxes.append(box)
            # print("Appended" , box_num-1)
            pen.goto(box)
            pen.color(color_)
            pen.write(piece , font=("Chalkduster" , fontsize , "bold"))
            mark_point(box_num-1, piece)
            check_winner(player)
            if player == 1:
                player = 2
                #     automate computer choices, these choices are random and devoid of logic for now
                #     conitnue picking until the chosen grid is not selected
                pick = True
                if game_on == False:
                    pick = False
                while pick:
                    computer_choice = pick_random_box()
                    # print("while choice" , computer_choice)
                    if grid[computer_choice - 1] not in boxes:
                        pick = False
                    play(computer_choice)
            else:
                player = 1
        else:

            # do not click already clicked button logic
            pass
            # print("No you can't do that")

def logic(x,y):
    # draw on corresponfing coordianates
    # print(x , y)
    # print(x<-70.0 , x>-167.0 , y<149.0 , y>60.0 )
    if x<-70.0 and x>-167.0 and y<149.0 and y>60.0:
        play(box_num=1)
    elif x < -70.0 and x > -167.0 and y < 40.0 and y > -39.0:
        play(box_num=4)
    elif x < -70.0 and x > -167.0 and y < -63.0 and y > -146.0:
        play(box_num=7)
#     second row
    elif x>-49.0 and x<52.0 and y<149.0 and y>60.0:
        play(box_num=2)
    elif x>-49.0 and x<52.0 and y < 40.0 and y > -39.0:
        play(box_num=5)
    elif x>-49.0 and x<52.0  and y < -63.0 and y > -146.0:
        play(box_num=8)
# last_row
    elif x>71.0 and x<165.0 and y<149.0 and y>60.0:
        play(box_num=3)
    elif x>71.0 and x<165.0 and y < 40.0 and y > -39.0:
        play(box_num=6)
    elif x>71.0 and x<165.0 and y < -63.0 and y > -146.0:
        play(box_num=9)

def write_label():
    # this function only write myhandle int he bottom corner
    p = Turtle()
    p.shape()
    hideturtle()
    p.pu()
    p.hideturtle()
    p.goto(220, -190)
    pensize(5)
    p.pd()
    p.color("white")
    p.write("@your_gardener" , font=("Arial", 10, "normal"))

    p.pu()
    p.goto(900, 790)

write_label()

#use pencil for animation
pen = Turtle()
pen.shape("images/pencil.gif")
pen.pensize(15)
pen.pu()

draw_lines()
pen.hideturtle()


# this is the logic behind clicking always listening for clicks and running the method called logic()
onscreenclick(logic, 1, False)

# canvas = getcanvas()
# x,y = canvas.winfo_pointerxy()
# print(pen.position())

window.mainloop()
