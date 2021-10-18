# a121_catch_a_turtle.py
# import statements
from os import pipe
import turtle 
import random
import leaderboard as lb

# game configuration
turtle_color=["blue", "green", "red", "yellow", "orange", "purple", "black"]
turtle_size=5
turtle_shape=["turtle", "circle", "square", "arrow", "triangle"]
score=1
font_setup=("arial",20,"normal")
timer=5
counter_interval=1000
timer_up=False
leaderboard_file_name = "a122_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = input("Enter Your Name: ")

def manage_leaderboard():
    global leader_scores_list
    global leader_names_list
    global score
    global MrTurtle

        # load all the leaderboard records into the lists
    lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

    # TODO
    if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
        lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
        lb.draw_leaderboard(leader_names_list, leader_scores_list, True, MrTurtle, score)

    else:
        lb.draw_leaderboard(leader_names_list, leader_scores_list, False, MrTurtle, score)


# initialize turtle
MrTurtle=turtle.Turtle()
MrTurtle.fillcolor(random.choice(turtle_color))
MrTurtle.shape(random.choice(turtle_shape))
MrTurtle.shapesize(turtle_size)
MrTurtle.penup()

score_writer=turtle.Turtle()
score_writer.penup()
score_writer.goto(-200,200)
score_writer.hideturtle()

timer2=turtle.Turtle()
timer2.penup()
timer2.goto(200,200)
timer2.hideturtle()

# game functions
def turtle_clicked(x,y):
    MrTurtle.hideturtle()
    MrTurtle.fillcolor(random.choice(turtle_color))
    MrTurtle.shape(random.choice(turtle_shape))
    if timer_up:
        MrTurtle.hideturtle()
    else:
        score_writer.clear()
        score_writer.write(score, font=font_setup)
        update_score()
        MrTurtle.hideturtle()
        change_position()
        MrTurtle.showturtle()

def change_position():
    MrTurtle.hideturtle()
    new_ypos=random.randint(-125,125)
    new_xpos=random.randint(-175,175)
    MrTurtle.goto(new_xpos,new_ypos)
    MrTurtle.setheading(random.randint(1,360))
    MrTurtle.showturtle()

def update_score():
    global score
    score+=1

def countdown():
    global timer,timer_up
    timer2.clear()
    if(timer<=0):
        timer2.write("Time's up!",font=font_setup)
        timer_up=True
        MrTurtle.hideturtle()
        manage_leaderboard()
    else:
        timer2.write("Timer: "+str(timer),font=font_setup)
        timer-=1
        timer2.getscreen().ontimer(countdown,counter_interval)

# events
MrTurtle.onclick(turtle_clicked)

wn=turtle.Screen()
wn.ontimer(countdown,counter_interval)
wn.mainloop()
