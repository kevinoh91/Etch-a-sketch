from turtle import Turtle, Screen
import random


def check_winner(turtles):
    for turtle in turtles:
        if turtle.xcor() >= 230:
            winner = turtle.pencolor()
            return winner
    return False

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Place a bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtles.append(turtle)

y = -125
for turtle in turtles:
    turtle.penup()
    turtle.goto(x=-230, y=y)
    y += 50

if user_bet:
    is_race_on = True

while is_race_on:
    if check_winner(turtles) != False:
        winner = check_winner(turtles)
        is_race_on = False
        print(f"The winner of the turtle race is {winner}. ")


    for turtle in turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)




screen.exitonclick()
