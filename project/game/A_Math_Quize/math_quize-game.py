import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Educational Math Quiz Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Fonts
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

# Game variables
score = 0
level = 1
points_to_level_up = 5
question, answer = "", 0
user_answer = ""
feedback = ""
feedback_color = BLACK

# Function to generate a new math question based on level
def generate_question(level):
    num1 = random.randint(1, level * 10)
    num2 = random.randint(1, level * 10)
    operation = random.choice(["+", "-", "*"])
    question = f"{num1} {operation} {num2}"
    answer = eval(question)
    return question, answer

# Function to draw text on the screen
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

# Generate the first question
question, answer = generate_question(level)

# Main game loop
while True:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  # Check answer on Enter key press
                if user_answer.isdigit() and int(user_answer) == answer:
                    score += 1
                    feedback = "Correct!"
                    feedback_color = GREEN
                    if score % points_to_level_up == 0:
                        level += 1
                        feedback += " Level Up!"
                else:
                    feedback = f"Incorrect! The answer was {answer}"
                    feedback_color = RED
                question, answer = generate_question(level)
                user_answer = ""
            elif event.key == pygame.K_BACKSPACE:
                user_answer = user_answer[:-1]
            else:
                user_answer += event.unicode

    # Display question and user input
    draw_text(f"Level: {level}", small_font, BLACK, screen, 50, 50)
    draw_text(f"Question: {question}", font, BLACK, screen, 50, 150)
    draw_text(user_answer, font, BLACK, screen, 50, 250)

    # Display score and feedback
    draw_text(f"Score: {score}", small_font, BLACK, screen, 50, 100)
    draw_text(feedback, small_font, feedback_color, screen, 50, 350)

    # Display rewards (points or badges)
    draw_text(f"Rewards: {score // points_to_level_up} Badge(s)", small_font, YELLOW, screen, 50, 400)

    # Update display
    pygame.display.flip()
