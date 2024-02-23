"""The Strategy page is where the user can go to adjust the team's strategy for the
week. Here they will be in charge of setting the playcall thresholds, viewing the 
opposing team's scouting report and matchups with the user's team, Make decisions on 
generated weekly dilemmas (both on and off the field), and administer touches to 
each specific offensive player."""

import pygame
from button import Button
from valuebutton import ValueButton
from quadbutton import Quad
from tributton import Tri
import random


class Strategy:

    def __init__(self, screen):
        # Strategy Screen Information
        self.width = 1000
        self.height = 800
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True

        # Initialize buttons
        self.buttons = []
        self.theshold = Button(self.screen, 0, 0, 500, 400, "Thresholds", color="White")
        self.scouting = Button(self.screen, 500, 0, 500, 400, "Scouting Report", color="Green")
        self.dilemma = Button(self.screen, 0, 400, 500, 400, "Dilemmas", color="Blue")
        self.touch = Button(self.screen, 500, 400, 500, 400, "Touches", color="Black")

        # Threshold Value Buttons
        self.thHeader = Button(screen, 190, 50, 300, 50, "<5      5-10     >10", color="White")
        self.th1 = Button(self.screen, 0, 100, 150, 50, "1st Down", color="White")
        self.th2 = Button(self.screen, 0, 175, 150, 50, "2nd Down", color="White")
        self.th3 = Button(self.screen, 0, 250, 150, 50, "3rd Down", color="White")
        self.th4 = Button(self.screen, 0, 325, 150, 50, "4th Down", color="White")

        self.q1 = Tri(self.screen, 200, 90)
        self.q2 = Tri(self.screen, 290, 90)
        self.q3 = Tri(self.screen, 380, 90)
        self.q4 = Tri(self.screen, 200, 165)
        self.q5 = Tri(self.screen, 290, 165)
        self.q6 = Tri(self.screen, 380, 165)
        self.q7 = Tri(self.screen, 200, 240)
        self.q8 = Tri(self.screen, 290, 240)
        self.q9 = Tri(self.screen, 380, 240)
        self.q10 = Tri(self.screen, 200, 315)
        self.q11 = Tri(self.screen, 290, 315)
        self.q12 = Tri(self.screen, 380, 315)
    

        """
        self.thv2 = ValueButton(screen, x=275, y=75, width=75, height=75, value=5)
        self.thv3 = ValueButton(screen, x=350, y=75, width=75, height=75, value=5)
        """

        # Weekly Dilemma Buttons
        self.dilemma1 = Button(self.screen, 10, 500, 200, 50, "Dilemma 1", color="White")
        dilemNUm = random.randint(0, 9)
        self.dilemma1.addSubText("dilemmas.txt", 10, 550, dilemNUm)

        # Add buttons to the list
        self.buttons.append(self.theshold)
        self.buttons.append(self.scouting)
        self.buttons.append(self.dilemma)
        self.buttons.append(self.touch)
        self.buttons.append(self.thHeader)
        self.buttons.append(self.th1)
        self.buttons.append(self.th2)
        self.buttons.append(self.th3)
        self.buttons.append(self.th4)
        self.buttons.append(self.q1)
        self.buttons.append(self.q2)
        self.buttons.append(self.q3)
        self.buttons.append(self.q4)
        self.buttons.append(self.q5)
        self.buttons.append(self.q6)
        self.buttons.append(self.q7)
        self.buttons.append(self.q8)
        self.buttons.append(self.q9)
        self.buttons.append(self.q10)
        self.buttons.append(self.q11)
        self.buttons.append(self.q12)
        self.buttons.append(self.dilemma1)
        



    def draw(self):
        # Draw the buttons
        for button in self.buttons:
            button.draw()
    
    def update(self):
        self.screen.fill((0, 0, 0))
        text = self.font.render("Weekly Strategy", True, (255, 255, 255))
        self.screen.blit(text, (200, 50))
        pygame.display.flip()
    
    def handle_event(self, event):
        for button in self.buttons:
            if isinstance(button, ValueButton):
                button.handle_event(event)
                               
