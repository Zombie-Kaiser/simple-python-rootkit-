
import random

class Lumberjack:
    def __init__(self):
        self.wood = 0
        self.time_left = 10
        self.position = 0

    def move(self, direction):
        if direction == "forward":
            self.position += 1
        elif direction == "backward":
            self.position -= 1
        else:
            print("Invalid direction")

    def chop_tree(self):
        global wood
        if random.random() < 0.5:
            print("You chopped down a tree! You now have", +wood)
            wood += 1
        else:
            print("You missed the tree.")

    def check_obstacle(self):
        global obstacles
        if random.random() < 0.2:
            print("You hit a rock! You lost one time unit.")
            self.time_left -= 1
        elif random.random() < 0.3:
            print("A squirrel ran across the path! You lost one time unit.")
            self.time_left -= 1
        else:
            pass

    def play(self):
        global obstacles
        while self.position < len(obstacles) and self.time_left > 0:
            print("You are at position", +self.position, "in the forest.")
            if self.time_left == 1:
                print("Time is running out! You need to get back to your starting point before it's too late.")
                break
            direction = input("What do you want to do? (forward/backward/chop tree): ")
            self.move(direction)
            if obstacles[self.position] == "tree":
                self.chop_tree()
            else:
                self.check_obstacle()
        print("Game over.")
