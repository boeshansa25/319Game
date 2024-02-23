"""This class creates the valuebutton class which is a type of button that allows 
for the user to click an up or down arrow on a button to change a given value.
After selecting their desired value, the button will return this vlaue to a class
to be created later that will use this value to complete a specific action in
the game simulation"""

import pygame

class ValueButton:
    def __init__(self, screen, x=0, y=0, width=100, height=100, value=0, max=10, min=0):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.value = value
        self.font = pygame.font.Font(None, 24)
        self.max = max
        self.min = min

        self.rect = pygame.Rect(x, y, width, height)
        self.up_rect = pygame.Rect(x, y, width, height//2)
        self.down_rect = pygame.Rect(x, y + (height//2), width, height//2)

    def draw(self):
        # Draw button
        pygame.draw.rect(self.screen, (255, 255, 255), self.rect)
        # Draw up arrow
        pygame.draw.polygon(self.screen, (0, 0, 0), [(self.up_rect.centerx, self.up_rect.top + 10), (self.up_rect.left + 20, self.up_rect.bottom - 10), (self.up_rect.right - 20, self.up_rect.bottom - 10)])
        # Draw down arrow
        pygame.draw.polygon(self.screen, (0, 0, 0), [(self.down_rect.centerx, self.down_rect.bottom - 10), (self.down_rect.left + 20, self.down_rect.top + 10), (self.down_rect.right - 20, self.down_rect.top + 10)])

        # Draw value
        value_surface = self.font.render(str(self.value), True, (0, 0, 0))
        value_rect = value_surface.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        self.screen.blit(value_surface, value_rect) 

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.up_rect.collidepoint(event.pos) and self.value < self.max:
                self.value += 1 
            elif self.down_rect.collidepoint(event.pos) and self.value > self.min:
                self.value -= 1  