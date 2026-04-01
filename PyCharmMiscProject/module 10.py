# 1. Elevator class

class Elevator:
    def __init__(self, bottom, top):
        self.current = bottom

    def floor_up(self):
        self.current = self.current + 1
        print("Floor:", self.current)

    def floor_down(self):
        self.current = self.current - 1
        print("Floor:", self.current)

    def go_to_floor(self, target):
        while self.current < target:
            self.floor_up()

        while self.current > target:
            self.floor_down()


# 2. Building and elevator system

# Elevator class (same as before)
class Elevator:
    def __init__(self, bottom, top):
        self.current = bottom   # start at bottom

    def floor_up(self):
        self.current = self.current + 1
        print("Floor:", self.current)

    def floor_down(self):
        self.current = self.current - 1
        print("Floor:", self.current)

    def go_to_floor(self, target):
        while self.current < target:
            self.floor_up()
        while self.current > target:
            self.floor_down()


# Building class (NEW)

class Building:
    def __init__(self, bottom, top, number):
        self.elevators = []

        for i in range(number):
            e = Elevator(bottom, top)
            self.elevators.append(e)

    def run_elevator(self, num, target):
        print("Elevator", num, "going to", target)
        self.elevators[num - 1].go_to_floor(target)

b = Building(1, 10, 2)   # 2 elevators

b.run_elevator(1, 5)   # elevator 1 → floor 5
b.run_elevator(2, 3)   # elevator 2 → floor 3
b.run_elevator(1, 1)   # elevator 1 → back to bottom


# 3. Building and fire alarm

# Elevator class
class Elevator:
    def __init__(self, bottom):
        self.current = bottom

    def floor_up(self):
        self.current = self.current + 1
        print("Floor:", self.current)

    def floor_down(self):
        self.current = self.current - 1
        print("Floor:", self.current)

    def go_to_floor(self, target):
        while self.current < target:
            self.floor_up()
        while self.current > target:
            self.floor_down()


# Building class
class Building:
    def __init__(self, bottom, number):
        self.bottom = bottom
        self.elevators = []

        for i in range(number):
            self.elevators.append(Elevator(bottom))

    def run_elevator(self, num, target):
        self.elevators[num - 1].go_to_floor(target)

    def fire_alarm(self):
        print("Fire alarm! Going to bottom")

        for e in self.elevators:
            e.go_to_floor(self.bottom)

b = Building(1, 2)

b.run_elevator(1, 5)
b.run_elevator(2, 3)
b.fire_alarm()


# 4. Car race program

import random

# Car class
class Car:
    def __init__(self, reg, max_speed):
        self.reg = reg
        self.max_speed = max_speed
        self.speed = 0
        self.distance = 0

    def accelerate(self, change):
        self.speed += change

        if self.speed > self.max_speed:
            self.speed = self.max_speed
        if self.speed < 0:
            self.speed = 0

    def drive(self):
        self.distance += self.speed   # 1 hour

# Race class
class Race:
    def __init__(self, name, km, cars):
        self.name = name
        self.km = km
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive()

    def print_status(self):
        print("\n== Race Status ==")
        for car in self.cars:
            print(car.reg, "Speed:", car.speed, "Distance:", int(car.distance))

    def race_finished(self):
        for car in self.cars:
            if car.distance >= self.km:
                return True
        return False

# main program
cars = []
for i in range(1, 11):
    cars.append(Car("ABC-" + str(i), random.randint(100, 200)))
race = Race("Grand Demolition Derby", 8000, cars)
hours = 0
while not race.race_finished():
    race.hour_passes()
    hours += 1

    if hours % 10 == 0:
        race.print_status()

race.print_status()