import sys, pygame

# Initialize PyGame's internal variables
pygame.init()

pygame.key.set_repeat(60, 10)

pygame.display.set_caption('  Game Name  ')

# Set up variables for the screen size in pixels
size = (1540, 865)

# Initialize a window with the screen size you set
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
fps = 60

bg_image = pygame.image.load("./images/bg_image.jpg")
icon = pygame.image.load("./images/icon.png")

pygame.display.set_icon(icon)

# pygame.mixer_music.load("music/Infinite Perspective.mp3")

music_playing = False

# vars
Win_chance = 0.1
Jackpot_chance = 0.01
Super_Jackpot_chance = 0.001
win_num = 0
win = ["You Lost", "You Won", "You won the Jackpot", "You won the Super Jackpot"]
plays = 1

# Colors
txt_color = (0, 0, 0)

game_font_small = pygame.font.SysFont("./fonts/Montserrat/Montserrat-Regular.ttf", 25)
game_font_reg = pygame.font.SysFont("./fonts/Montserrat/Montserrat-Regular.ttf", 50)
game_font_big = pygame.font.SysFont("./fonts/Montserrat/Montserrat-Regular.ttf", 100)

stage = 1
scene = 1

def draw_sprites():
    if scene == 1:
        screen.blit(bg_image, (0, 0))
        draw_text("Game Name", game_font_big, txt_color, 450, 252.5)
        draw_text("BY IAN NORTHCUTT", game_font_big, txt_color, 450, 352.5)
        draw_text("PRESS SPACE TO START", game_font_big, txt_color, 400, 452.5)
    elif scene == 2:
        screen.blit(bg_image, (0, 0))
        draw_text(f"", game_font_reg, txt_color, 20, 20)
    elif scene == 3:        
        screen.blit(bg_image, (0, 0))
        draw_text(win[win_num], game_font_big, txt_color, 200, 252.5)
        draw_text("press space to play again", game_font_big, txt_color, 320, 352.5)
        draw_text("or press esc, q, or end to exit.", game_font_big, txt_color, 250, 452.5)


def draw_text(text, font, color, x, y):
    image = font.render(text, True, color)
    screen.blit(image, (x, y))

def start_music(name):
    global music_playing
    if not music_playing:
        pygame.mixer_music.load(name)
        pygame.mixer_music.play()
        music_playing = True
    else:
        stop_music()
        start_music(name)

def stop_music():
    global music_playing
    pygame.mixer_music.stop()
    music_playing = False


print()

# start_music("music/Infinite Perspective.mp3")

# ==========================
# ===== MAIN GAME LOOP =====
# ==========================
while True:
    clock.tick(fps)
    # This for loop gets any keyboard, mouse, or other events that happen from user input
    for event in pygame.event.get():
        # The pygame.QUIT event happens when you close the game window
        if event.type == pygame.QUIT:
            print("You left the game. :|")
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            if scene == 1:
                if key[pygame.K_SPACE] or key[pygame.K_s]:
                    scene = 2
                elif key[pygame.K_q] or key[pygame.K_ESCAPE] or key[pygame.K_END]:
                    print("You left the game. :|")
                    sys.exit()
            elif scene == 2:
                if key[pygame.K_q] or key[pygame.K_ESCAPE] or key[pygame.K_END]:
                    print("You left the game. :|")
                    sys.exit()
            elif scene == 3:
                if key[pygame.K_SPACE] or key[pygame.K_s]:
                    win_num += 1
                    scene = 2
                elif key[pygame.K_q] or key[pygame.K_ESCAPE] or key[pygame.K_END]:
                    print("You left the game. :|")
                    sys.exit()


    draw_sprites()

    # At the end of each game loop, call pygame.display.flip() to update the screen with all of your sprites
    pygame.display.flip()
