"""This class creates a tributton for the weekly scheme chart, which allows the user to select the
percentage of a specific play type ran depending on the given down and distance."""
import pygame

class Tri:
    def __init__(self, screen, x=0, y=0, width=75, height=50, color="White", font_color="Black"):
        # Screen
        self.screen = screen
        # Location
        self.x = x
        self.y = y
        # Dimensions
        self.width = width
        self.height = height
        # Graphics
        self.color = color
        self.font_color = font_color
        self.font = pygame.font.Font(None, 36)
        # Values
        self.values = [0, 0, 0]
        # Create a rect object for the button
        self.rects = [pygame.Rect(x + i * width // 3, y, width // 3, height) for i in range(3)]
        # Border
        self.border_color = "Black"
        self.border_width = 3
        # Max Value
        self.max_value = 10
        self.text=None

    def draw(self):
        # Change the color based on the total value
        self.color = "Green" if sum(self.values) == self.max_value else "Yellow"

        # Draw the border
        pygame.draw.rect(self.screen, self.border_color, (self.x - self.border_width, self.y - self.border_width, self.width + 2 * self.border_width, self.height + 2 * self.border_width))

        # Draw each box individually
        for i in range(3):
            pygame.draw.rect(self.screen, self.color, self.rects[i])
            text = self.font.render(str(self.values[i]), True, self.font_color)
            text_rect = text.get_rect(center=self.rects[i].center)
            self.screen.blit(text, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(3):
                if self.rects[i].collidepoint(event.pos):
                    if event.pos[1] < self.y + self.height / 2 and sum(self.values) < 10:  # Top half of the button
                        self.values[i] += 1
                    elif event.pos[1] >= self.y + self.height / 2 and self.values[i] > 0:  # Bottom half of the button
                        self.values[i] -= 1