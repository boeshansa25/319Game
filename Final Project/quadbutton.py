"""This class creates a quad button for the weekly scheme chart, which allows the user to select the 
percentage of a specific play type ran depending on the given down and distance."""

import pygame

class Quad:
    def __init__(self, screen, x=0, y=0, width=100, height=100):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font = pygame.font.Font(None, 24)
        self.values = {'top_left': 0, 'top_right': 0, 'bottom_left': 0, 'bottom_right': 0}
        self.rects = {
            'top_left': pygame.Rect(x, y, width//2, height//2),
            'top_right': pygame.Rect(x + width//2, y, width//2, height//2),
            'bottom_left': pygame.Rect(x, y + height//2, width//2, height//2),
            'bottom_right': pygame.Rect(x + width//2, y + height//2, width//2, height//2)
        }

    def draw(self):
        # Draw button
        pygame.draw.rect(self.screen, (255, 255, 255), (self.x, self.y, self.width, self.height))
        # Draw lines
        pygame.draw.rect(self.screen, (0, 0, 0), (self.x, self.y, self.width, self.height), 3)
        # Draw values
        for quadrant, value in self.values.items():
            value_surface = self.font.render(f'{value}%', True, (0, 0, 0))
            value_rect = value_surface.get_rect(center=self.rects[quadrant].center)
            self.screen.blit(value_surface, value_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for quadrant, rect in self.rects.items():
                if rect.collidepoint(event.pos):
                    if event.pos[1] < rect.centery and self.values[quadrant] < 100:  # top half of quadrant
                        self.values[quadrant] += 10
                    elif event.pos[1] >= rect.centery and self.values[quadrant] > 0:  # bottom half of quadrant
                        self.values[quadrant] -= 10