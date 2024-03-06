"""Siminterface"""

import pygame


class SimInterface:
    def __init__(self, screen, game):
        # SimInterface Information
        self.game = game
        self.width = 1000
        self.height = 800
        self.field_height = self.height * 0.6
        self.scoreboard_height = self.height * 0.2
        self.textbox_height = self.height * 0.2
        self.endzone_width = self.width * 0.1
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
        self.running = True

        # Team names and colors
        self.user_team = {"name": "User Team", "color": "Blue"}
        self.opponent_team = {"name": "Opponent Team", "color": "Red"}

        # Initialize game variables
        self.user_score = 0
        self.opponent_score = 0
        self.time_left = "15:00"
        self.quarter = 1
        self.user_possession = True

    def update(self):
        self.screen.fill("White")
        pygame.display.flip()

    def draw(self):
        # Clear the screen
        self.screen.fill("White")

        # Draw the field
        pygame.draw.rect(self.screen, "Green", (self.endzone_width, 0, self.width - 2 * self.endzone_width, self.field_height))

        # Draw the lines and numbers
        for i in range(1, 10):
            pygame.draw.line(self.screen, "White", (self.endzone_width + i * (self.width - 2 * self.endzone_width) / 10, 0), (self.endzone_width + i * (self.width - 2 * self.endzone_width) / 10, self.field_height), 1)
            if i < 6: text = self.font.render(str(i * 10), True, "White")
            else: text = self.font.render(str(50 - ((i-5) * 10)), True, "White")
            self.screen.blit(text, (self.endzone_width + i * (self.width - 2 * self.endzone_width) / 10 - text.get_width() / 2, self.field_height / 2 - text.get_height() / 2))

        # Draw the end zones
        pygame.draw.rect(self.screen, self.user_team["color"], (0, 0, self.endzone_width, self.field_height))
        pygame.draw.rect(self.screen, self.opponent_team["color"], (self.width - self.endzone_width, 0, self.endzone_width, self.field_height))

        # Draw the team names
        text = self.font.render(self.user_team["name"], True, "White")
        rotated_text = pygame.transform.rotate(text, 90)
        self.screen.blit(rotated_text, (self.endzone_width / 2 - rotated_text.get_width() / 2, self.field_height / 2 - rotated_text.get_height() / 2))
        text = self.font.render(self.opponent_team["name"], True, "White")
        rotated_text = pygame.transform.rotate(text, 270)
        self.screen.blit(rotated_text, (self.width - self.endzone_width / 2 - rotated_text.get_width() / 2, self.field_height / 2 - rotated_text.get_height() / 2))

        # Draw the scoreboard
        pygame.draw.rect(self.screen, "Light Blue", (0, self.field_height, self.width, self.scoreboard_height))

        # Draw the scores
        score_text = self.font.render(f"{self.user_team['name']}: {self.user_score}   {self.opponent_team['name']}: {self.opponent_score}", True, "White")
        self.screen.blit(score_text, (self.width / 2 - score_text.get_width() / 2, self.field_height + self.scoreboard_height / 4 - score_text.get_height() / 2))

        # Draw the time and quarter
        time_quarter_text = self.font.render(f"Time: {self.time_left}   Quarter: {self.quarter}", True, "White")
        self.screen.blit(time_quarter_text, (self.width / 2 - time_quarter_text.get_width() / 2, self.field_height + 3 * self.scoreboard_height / 4 - time_quarter_text.get_height() / 2))

        # Draw the possession light
        if self.user_possession:
            pygame.draw.circle(self.screen, "Yellow", (self.width / 4, self.field_height + self.scoreboard_height / 2), 10)
        else:
            pygame.draw.circle(self.screen, "Yellow", (3 * self.width / 4, self.field_height + self.scoreboard_height / 2), 10)

        # Draw the text box
        pygame.draw.rect(self.screen, "White", (0, self.field_height + self.scoreboard_height, self.width, self.textbox_height))

        # Update the display
        pygame.display.flip()

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False



"""
# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 800, 600
FIELD_HEIGHT = HEIGHT * 0.6
SCOREBOARD_HEIGHT = HEIGHT * 0.2
TEXTBOX_HEIGHT = HEIGHT * 0.2
ENDZONE_WIDTH = WIDTH * 0.1

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create the fonts
font = pygame.font.Font(None, 36)

# Team names and colors
user_team = {"name": "User Team", "color": "Blue"}
opponent_team = {"name": "Opponent Team", "color": "Red"}

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill("White")

    # Draw the field
    pygame.draw.rect(screen, "Green", (ENDZONE_WIDTH, 0, WIDTH - 2 * ENDZONE_WIDTH, FIELD_HEIGHT))

    # Draw the lines and numbers
    for i in range(1, 10):
        pygame.draw.line(screen, "White", (ENDZONE_WIDTH + i * (WIDTH - 2 * ENDZONE_WIDTH) / 10, 0), (ENDZONE_WIDTH + i * (WIDTH - 2 * ENDZONE_WIDTH) / 10, FIELD_HEIGHT), 1)
        if i < 6: text = font.render(str(i * 10), True, "White")
        else: text = font.render(str(50 - ((i-5) * 10)), True, "White")
        screen.blit(text, (ENDZONE_WIDTH + i * (WIDTH - 2 * ENDZONE_WIDTH) / 10 - text.get_width() / 2, FIELD_HEIGHT / 2 - text.get_height() / 2))

    # Draw the end zones
    pygame.draw.rect(screen, user_team["color"], (0, 0, ENDZONE_WIDTH, FIELD_HEIGHT))
    pygame.draw.rect(screen, opponent_team["color"], (WIDTH - ENDZONE_WIDTH, 0, ENDZONE_WIDTH, FIELD_HEIGHT))

    # Draw the team names
    text = font.render(user_team["name"], True, "White")
    rotated_text = pygame.transform.rotate(text, 90)
    screen.blit(rotated_text, (ENDZONE_WIDTH / 2 - rotated_text.get_width() / 2, FIELD_HEIGHT / 2 - rotated_text.get_height() / 2))
    text = font.render(opponent_team["name"], True, "White")
    rotated_text = pygame.transform.rotate(text, 270)
    screen.blit(rotated_text, (WIDTH - ENDZONE_WIDTH / 2 - rotated_text.get_width() / 2, FIELD_HEIGHT / 2 - rotated_text.get_height() / 2))

    # Draw the scoreboard
    # Initialize game variables
    user_score = 0
    opponent_score = 0
    time_left = "15:00"
    quarter = 1
    user_possession = True

    # In your main loop, draw the scoreboard
    # Draw the scoreboard
    pygame.draw.rect(screen, "Light Blue", (0, FIELD_HEIGHT, WIDTH, SCOREBOARD_HEIGHT))

    # Draw the scores
    score_text = font.render(f"{user_team['name']}: {user_score}   {opponent_team['name']}: {opponent_score}", True, "White")
    screen.blit(score_text, (WIDTH / 2 - score_text.get_width() / 2, FIELD_HEIGHT + SCOREBOARD_HEIGHT / 4 - score_text.get_height() / 2))

    # Draw the time and quarter
    time_quarter_text = font.render(f"Time: {time_left}   Quarter: {quarter}", True, "White")
    screen.blit(time_quarter_text, (WIDTH / 2 - time_quarter_text.get_width() / 2, FIELD_HEIGHT + 3 * SCOREBOARD_HEIGHT / 4 - time_quarter_text.get_height() / 2))

    # Draw the possession light
    if user_possession:
        pygame.draw.circle(screen, "Yellow", (WIDTH / 4, FIELD_HEIGHT + SCOREBOARD_HEIGHT / 2), 10)
    else:
        pygame.draw.circle(screen, "Yellow", (3 * WIDTH / 4, FIELD_HEIGHT + SCOREBOARD_HEIGHT / 2), 10)

    # Draw the text box
    pygame.draw.rect(screen, "White", (0, FIELD_HEIGHT + SCOREBOARD_HEIGHT, WIDTH, TEXTBOX_HEIGHT))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
"""

