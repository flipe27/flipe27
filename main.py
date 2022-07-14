# TODO: Save the best score

from assets import *
from classes.bird import Bird
from classes.ground import Ground
from classes.pipe import Pipe

# Screen size
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600


# Restart the game option
def restart_screen(screen):
    restart = START_FONT.render('Press SPACEBAR to try again', True, (255, 255, 255))

    screen.blit(restart, ((SCREEN_WIDTH / 2) - (restart.get_width() / 2), 240))
    screen.blit(RESTART_IMAGE,
                ((SCREEN_WIDTH / 2) - (RESTART_IMAGE.get_width() / 2),
                 (SCREEN_HEIGHT / 2) - (RESTART_IMAGE.get_height() / 2)))


# Drawing the title screen
def title_screen(screen):
    screen.blit(BACKGROUND_IMAGE, (0, -300))
    screen.blit(GAME_LOGO,
                ((SCREEN_WIDTH / 2) - (GAME_LOGO.get_width() / 2),
                 (SCREEN_HEIGHT / 3) - (GAME_LOGO.get_height() / 2)))

    start = START_FONT.render('Press SPACEBAR', True, (255, 255, 255))
    screen.blit(start,
                ((SCREEN_WIDTH / 2) - (start.get_width() / 2),
                 (SCREEN_HEIGHT / 2) - (start.get_height() / 2)))

    pygame.display.update()


# Drawing the objects in the game screen
def draw_screen(screen, birds, pipes, ground, points, restart):
    screen.blit(BACKGROUND_IMAGE, (0, -300))
    for bird in birds:
        bird.draw(screen)
    for pipe in pipes:
        pipe.draw(screen)
    ground.draw(screen)

    text = POINTS_FONT.render(f'Score: {points}', True, (255, 255, 255))
    screen.blit(text, (SCREEN_WIDTH - 10 - text.get_width(), 10))

    # Restart option
    if restart:
        restart_screen(screen)

    pygame.display.update()


# Playing the game
def main(title=True, playing=True):
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Flappy Bird')
    pygame.display.set_icon(GAME_ICON)

    restart_game = False

    # Title screen
    while title:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                title = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    title = False

        title_screen(screen)

    birds = [Bird(90, 200)]
    ground = Ground(530)
    pipes = [Pipe(700)]
    points = 0
    clock = pygame.time.Clock()

    # Game screen
    while playing:
        clock.tick(30)

        if len(birds) == 0:
            if len(pipes) == 0:
                restart_game = True

        # User interaction
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Restart the game
                    if restart_game:
                        main(False)
                    else:
                        for bird in birds:
                            bird.jump()

        # Moving the objects
        ground.move()
        for bird in birds:
            bird.move()

        add_pipe = False
        remove_pipes = []
        for pipe in pipes:
            for i, bird in enumerate(birds):
                if pipe.collide(bird):
                    birds.pop(i)
                if not pipe.passed and bird.x > pipe.x:
                    pipe.passed = True
                    add_pipe = True
            pipe.move()

            if pipe.x + pipe.TOP_PIPE.get_width() < 0:
                remove_pipes.append(pipe)

        if add_pipe:
            points += 1
            pipes.append(Pipe(600))
        for pipe in remove_pipes:
            pipes.remove(pipe)

        # Bird collision with the scenery
        for i, bird in enumerate(birds):
            if (bird.y + bird.image.get_height()) > ground.y or bird.y < 0:
                birds.pop(i)

        # Draw the game screen
        draw_screen(screen, birds, pipes, ground, points, restart_game)


if __name__ == '__main__':
    main()
