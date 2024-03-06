"""This file runs the simulation for each game"""

import random
import pygame
import time


class Simulation:

    def __init__(self):
        self.minutes = 15
        self.seconds = 0
        self.quater = 1
        self.user = None
        self.opponent = None
        self.ball = True
        self.down = 1
        self.yards = 10
        self.yardline = 20
        self.direction = "right"


    def clock():
        while quater < 5:
            while minutes > 0 or seconds > 0:
                if seconds == 0:
                    minutes -= 1
                    seconds = 59
                else:
                    seconds -= 1
                print(str(minutes) + ":" + str(seconds))
                pygame.time.wait(1000)
            quater += 1
            minutes = 15
            seconds = 0

    def play():
        pass