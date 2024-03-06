"""
This class is used to create a button object that can be used in the game. The user
can customize the button's text, color, and position. The button can also be clicked
and complete a specific action or send the user to an alternate screen.
"""

import pygame

class Subtext:
    def __init__(self, filename, x=0, y=0, line_number=None):
        with open(filename, 'r') as file:
            lines = file.readlines()
            if line_number is not None:
                text = lines[line_number].rstrip('\n')
            else:
                text = ''.join(lines)
        font = pygame.font.Font(None, 28)  
        self.surface = font.render(text, True, (255, 255, 255))  
        self.position = (x, y)

class Button:
    def __init__(self, screen, x=0, y=0, width=100, height=100, title="Button",
                 hover_color="Green", color="White", font_color="Black", action=None, preview=False):
        # Screen
        self.screen = screen
        # Location
        self.x = x
        self.y = y
        # Dimensions
        self.width = width
        self.height = height
        # Graphics
        self.text = title
        self.color = color
        self.font_color = font_color
        self.font = pygame.font.Font(None, 36)
        self.hover_color = hover_color
        self.preview = preview
        self.hover = False
        # Subtext
        self.subtexts = []
        # Action
        self.action = action
        # Create a rect object for the button
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self):
        # Draw the button
        color = self.hover_color if self.hover else self.color
        pygame.draw.rect(self.screen, self.color, self.rect)
        font = pygame.font.Font(None, 42)
        text = font.render(self.text, True, self.font_color)
        self.screen.blit(text, (self.x + (self.width - font.size(self.text)[0]) / 2, self.y + 10))
        # Draw the preview text
        if self.preview:
            preview_text = self.preview()
            preview_surface = font.render(preview_text, True, (0, 0, 0))
            preview_rect = preview_surface.get_rect(center=(self.rect.centerx, self.rect.centery + self.rect.height // 2 + 20))
            self.screen.blit(preview_surface, preview_rect)
        # Draw the subtexts
        for subtext in self.subtexts:
            self.screen.blit(subtext.surface, subtext.position)

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False

    def hover(self, event):
        if self.rect.collidepoint(event.pos):
            self.hovering = True
        else:
            self.hovering = False

    def update(self, event):
        self.hover(event)
        if self.is_clicked(event) and self.action:
            self.perform_action()

    def perform_action(self):
        self.action()

    def addSubText(self, filename, x=0, y=0, line_number=None):
        """Adds 1 line of subtext from a file to the button. 
        If line_number is None, the entire file is added."""
        subtext = Subtext(filename, self.x + x, self.y + y, line_number)
        self.subtexts.append(subtext)