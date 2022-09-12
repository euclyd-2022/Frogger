from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 0.2
IMAGES = ["Car_blue.gif", "Car_orange.gif", "Car_grey.gif", "Car_yellow.gif", "Car_purple.gif"]


class CarManager():

    def __init__(self):

        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

        #self.yrange = random.randrange(-250, 250, 30)
    def create_car(self):
            random_choice = random.randint(1, 6)
            if random_choice >4:
                new_y = random.randrange(-240, 250, 30)
                new_car = Turtle(random.choice(IMAGES))
                new_car.shapesize(stretch_wid=1,stretch_len=2)
                new_car.penup()
                new_car.color(random.choice(COLORS))
                new_car.setx(300)
                new_car.sety(new_y)
                self.all_cars.append(new_car)


    def move(self):
        for car in self.all_cars:
        #while car.xcor() > -250:
            car.backward(self.speed + random.randint(0, 4))

    def increase_speed(self):

        for car in self.all_cars:
            self.speed += MOVE_INCREMENT
            car.backward(self.speed)
            #print(self.speed)







