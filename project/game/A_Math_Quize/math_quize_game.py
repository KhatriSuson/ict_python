import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Math Quiz Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Fonts
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

# Game variables
score = 0
question, answer = "", 0
user_answer = ""
game_over = False

# Function to generate a new math question
def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(["+", "-", "*"])
    question = f"{num1} {operation} {num2}"
    answer = eval(question)
    return question, answer

# Generate the first question
question, answer = generate_question()

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
                else:
                    feedback = f"Incorrect! The answer was {answer}"
                    feedback_color = RED
                question, answer = generate_question()
                user_answer = ""
                game_over = True
            elif event.key == pygame.K_BACKSPACE:
                user_answer = user_answer[:-1]
            else:
                user_answer += event.unicode

    # Display question and user input
    question_text = font.render(f"Question: {question}", True, BLACK)
    screen.blit(question_text, (50, 100))

    input_text = font.render(user_answer, True, BLACK)
    screen.blit(input_text, (50, 200))

    # Display score
    score_text = small_font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (50, 50))

    # Display feedback after answering
    if game_over:
        feedback_text = small_font.render(feedback, True, feedback_color)
        screen.blit(feedback_text, (50, 300))
        game_over = False

    # Update display
    pygame.display.flip()
