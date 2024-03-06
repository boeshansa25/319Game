"""
The dashboard is the main view for the user where they can see an overview of how
the season is currently going. In includes the Facility grades, the current
statistical leaders, the current division standings, a window of the recent past and 
upcoming games, and then the managerial customization settings such as the roster, 
coaching adjustments, and gameplay settings.
"""
import pygame
from button import Button

class Dashboard:

    def __init__(self, screen):
        # Dashboard Information
        self.width = 1000
        self.height = 800
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.Font(None, 36)

        # Initialize buttons
        self.buttons = []
        # Facilities Button
        self.button1 = Button(self.screen, 25, 25, 300, 300, "Facilities", color="Blue")
        self.button1.addSubText("Facilities.txt", 25, 100, 0)
        self.button1.addSubText("Facilities.txt", 25, 150, 1)
        self.button1.addSubText("Facilities.txt", 25, 200, 2)
        

        self.button2 = Button(self.screen, 350, 25, 300, 300, "Statistics", color="Blue")
        self.button2.addSubText("Statistics.txt", 25, 100, 0)
        self.button2.addSubText("Statistics.txt", 25, 150, 1)
        self.button2.addSubText("Statistics.txt", 25, 200, 2)
        self.button2.addSubText("Statistics.txt", 25, 250, 3)


        self.button3 = Button(self.screen, 675, 25, 300, 300, "Standings", color="Blue")
        self.button3.addSubText("Standings.txt", 25, 50, 0)
        self.button3.addSubText("Standings.txt", 25, 100, 1)
        self.button3.addSubText("Standings.txt", 25, 150, 2)
        self.button3.addSubText("Standings.txt", 25, 200, 3)
        self.button3.addSubText("Standings.txt", 25, 250, 4)


        # Schedule Button
        self.button4 = Button(self.screen, 25, 350, 950, 350, "Schedule View")
 

        # Setting Buttons
        self.button5 = Button(self.screen, 40, 725, 200, 50, "Roster", color="Green")
        self.button6 = Button(self.screen, 280, 725, 200, 50, "Coaching", color="Green")
        self.button7 = Button(self.screen, 520, 725, 200, 50, "Settings", color="Green")
        self.button8 = Button(self.screen, 760, 725, 200, 50, "Strategy", color="Green")

        
        # Add buttons to the list
        self.buttons.append(self.button1)
        self.buttons.append(self.button2)
        self.buttons.append(self.button3)
        self.buttons.append(self.button4)
        self.buttons.append(self.button5)
        self.buttons.append(self.button6)
        self.buttons.append(self.button7)
        self.buttons.append(self.button8)

    
    def update(self):
        self.screen.fill((0, 0, 0))
        text = self.font.render("Dashboard", True, (255, 255, 255))
        self.screen.blit(text, (200, 50))
        pygame.display.flip()
        
    def draw(self):
        # Clear the screen
        self.screen.fill((0, 0, 0))

        # Draw all buttons
        for button in self.buttons:
            button.draw()

        # Update the display
        pygame.display.flip()
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                if button.rect.collidepoint(event.pos):
                    if button.text == "Strategy":
                        self.game.change_screen(self.game.strategy)

