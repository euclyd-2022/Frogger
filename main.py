import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("F R O G G E R Y")
screen.bgpic("road.gif")
screen.addshape("Car_blue.gif")
screen.addshape("Car_orange.gif")
screen.addshape("Car_grey.gif")
screen.addshape("Car_yellow.gif")
screen.addshape("Car_purple.gif")

screen.tracer(0)
turtle_player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
level = 0
game_is_on = True
screen.listen()
screen.onkeypress(turtle_player.move, "Up")


while game_is_on:
    time.sleep(0.1)
    screen.update()
    #move cars to left of screen
    car_manager.create_car()
    car_manager.move()
    if turtle_player.ycor() > 280:
        turtle_player.restart()
        car_manager.increase_speed()
        scoreboard.increase_score()

    for car in car_manager.all_cars:

        if car.distance(turtle_player) < 20:

            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()










