import time
from turtle import Screen,Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from playsound import playsound

screen = Screen()
screen.addshape('C:/Users/bardz/Downloads/nar.gif')
screen.addshape('C:/Users/bardz/Downloads/db.gif')
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player=Player()
carmanager=CarManager()
scoreboard=Scoreboard()

screen.onkeypress(player.move,"Up")




x=0
game_is_on = True
y=1
z=1
while game_is_on:
    time.sleep(0.1)
    screen.update()

    x+=1
    if x%8==0:
        carmanager.create_car()
    if x>=8:
        carmanager.move()

    for car in carmanager.all_cars:
        if car.distance(player)<30:
            game_is_on=False

    if player.at_finish():

        player.next_level()
        carmanager.level_up()
        scoreboard.point()

    if scoreboard.score==1 and y==1:
        playsound('C:/Users/bardz/Downloads/naruto.mp3')
        y+=1

    if scoreboard.score==2 and z==1:
        playsound('C:/Users/bardz/Downloads/sam.mp3')
        z+=1
    scoreboard.praise()
scoreboard.game_over()
screen.exitonclick()