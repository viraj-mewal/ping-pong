import pygame
from sys import exit
import random

xVel, yVel = random.randint(4, 6), random.randint(4, 6)
leftScore, rightScore = 0, 0

def draw(left_padle, right_padle,ball, score_left, score_right):
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, 'white', left_padle)
    pygame.draw.rect(screen, 'white', right_padle)
    pygame.draw.line(screen, 'white', (width//2, 0), (width//2, height), 2)
    pygame.draw.ellipse(screen, 'white', ball)

    score_left_rect = score_left.get_rect(center = ((width//2)//2, 40))
    score_right_rect = score_right.get_rect(center = ((width//2)+(width//2)//2, 40))

    screen.blit(score_left, score_left_rect)
    screen.blit(score_right, score_right_rect)
def reset(ball):
    ball.center = (width//2, random.randint(20, height-20))
    xVel = random.choice([4, -4])
    yVel = 4

def moveBall(ball, left_padle, right_padle):
    global xVel, yVel, rightScore, leftScore

    ball.x += xVel
    ball.y += yVel

    # top side
    if ball.top <= 0:
        yVel = -(yVel)

    # bottom side
    if ball.bottom >= height:
        yVel = -(yVel)

    # left side
    if ball.left <= 0:
        rightScore += 1
        reset(ball)

    # right side
    if ball.right >= width:
        leftScore += 1
        reset(ball)

    if ball.colliderect(left_padle):
        xVel = -(xVel)
        yVel = random.choice([-3, -4, -5, -6, 3, 4, 5, 6])
    if ball.colliderect(right_padle):
        xVel = -(xVel)
        yVel = random.choice([-2, -3, -4, -5, -6, 2, 3, 4, 5, 6])

pygame.init()

width, height = 800, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Ultimate Game")
clock = pygame.time.Clock()


def main():
    global leftScore, rightScore
    left_padle = pygame.Rect(0, 0, 15, 80)
    left_padle.center = (20, height//2)

    right_padle = pygame.Rect(0, 0, 15, 80)
    right_padle.center = (width-20, height//2)

    ball = pygame.Rect(0, 0, 13, 13)
    ball.center = (width//2, height//2)

    paddleVel = 8

    font = pygame.font.SysFont('Comic Sans MS', 50)
    info_font = pygame.font.SysFont('Comic Sans MS', 20)

    game_active = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_active = True
                    leftScore, rightScore, = 0, 0
                    xVel, yVel = random.randint(4, 6), random.randint(4, 6)


        if game_active:
            # movement
            keys = pygame.key.get_pressed()

            # left paddle
            if keys[pygame.K_w] and not (left_padle.top <= 0):
                left_padle.y -= paddleVel
            elif keys[pygame.K_s] and not (left_padle.bottom >= height):
                left_padle.y += paddleVel

            # right paddle
            if keys[pygame.K_UP] and not (right_padle.top <= 0):
                right_padle.y -= paddleVel
            elif keys[pygame.K_DOWN] and not (right_padle.bottom >= height):
                right_padle.y += paddleVel

            score_left = font.render(str(leftScore), True, 'white')
            score_right = font.render(str(rightScore), True, 'white')

            if leftScore == 10 or rightScore == 10:
                game_active = False

            moveBall(ball, left_padle, right_padle)
            draw(left_padle, right_padle, ball, score_left, score_right)
        else:
            if leftScore == 0 and rightScore == 0:
                screen.fill('black')
                msg = font.render(f"Ping Pong", True, 'white')
                msg_rect = msg.get_rect(center = (width//2, height//2))
                msg_rect.center = (width//2, height//2-msg_rect.height)

                info = info_font.render("Press [Space] to START", True, 'white')
                info_rect = info.get_rect(center = (width//2, height//2))

                screen.blit(msg, msg_rect)
                screen.blit(info, info_rect)
            else:
                won = 'left' if leftScore > rightScore else 'Right'
                screen.fill('black')
                msg = font.render(f"Player {won} Won !", True, 'white')
                msg_rect = msg.get_rect(center = (width//2, height//2))
                msg_rect.center = (width//2, height//2-msg_rect.height)

                info = info_font.render("Press [Space] to RESTART", True, 'white')
                info_rect = info.get_rect(center = (width//2, height//2))

                screen.blit(msg, msg_rect)
                screen.blit(info, info_rect)

        pygame.display.update()
        clock.tick(60)

main()
