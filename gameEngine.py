"""This game engine class runs and sets the state of the game, and allows for the
User to go back and forth between different screens in the game"""

import pygame

class Game:
    def __init__(self, screen, dashboard=None, strategy=None, simulation=None):
        self.running = True
        self.active_screen = dashboard
        self.screen = screen
        self.dashboard = dashboard
        self.strategy = strategy
        self.siminterface = simulation

    def set_dashboard(self, dashboard):
        self.dashboard = dashboard
    
    def set_strategy(self, strategy):
        self.strategy = strategy
    
    def set_simulation(self, simulation):
        self.siminterface = simulation


    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                else:
                    if self.active_screen is not None:
                        self.active_screen.handle_event(event)

            # Draw
            self.screen.fill((255, 255, 255))
            if self.active_screen is not None:
                self.active_screen.draw()

            pygame.display.flip()

    def change_screen(self, new_screen):
        self.active_screen = new_screen
    
    def newWeek(self):
        """This function is called after each week progresses in the game and will generate all 
        simulated game information from around the league, update all necessary files with stats
        and scores around the league, progress user players and team, and choose new dilemmas, as well
        as generate a scouting report for the next week's game"""
        pass




