import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

if __name__ == '__main__':
    screen.listen()
    screen.onkey(player.move_player, "Up")

    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        car_manager.create_car()
        car_manager.move_cars()

        # Detect turtle collision with a car
        for car in car_manager.cars:
            if player.distance(car) < 20:
                scoreboard.game_over()
                game_is_on = False

        # Detect if turtle reach the top of the screen
        if player.is_at_top():
            car_manager.speed_up()
            scoreboard.add_level()

    screen.exitonclick()
