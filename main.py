import sys, os, pygame, random as r, itertools

os.environ['SDL_AUDIODRIVER'] = 'dsp' # fix sound playback

# Initialize PyGame's internal variables
pygame.init()

pygame.key.set_repeat(60, 10)

pygame.display.set_caption('  Slot Machine Game  ')

# Set up variables for the screen size in pixels
size = (1280, 865)

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
win_num = 0
win = ["You Lost", "You Won", "You won the Jackpot", "You won the Super Jackpot"]
plays = 1
images = ["images/slot1.png", "images/slot2.png", "images/slot3.png", "images/slot4.png", "images/slot5.png"]
chance_dict = {}
num = 0
for i in itertools.product([0,1,2,3,4], repeat=3):
    chance_dict[num] = i
    num += 1
print(chance_dict)
num_slots = 3
num_images = 5
# Load images for the slots
# slots_images = [pygame.transform.scale(pygame.image.load(f"./images/slot{i+1}.png"), (200, 200)) for i in range(num_images)]    
# Colors
txt_color = (0, 0, 0)

game_font_small = pygame.font.Font("Ubuntu-Regular.ttf", 25)
game_font_reg = pygame.font.Font("Ubuntu-Regular.ttf", 50)
game_font_big = pygame.font.Font("Ubuntu-Regular.ttf", 100)

stage = 1
scene = 1

def draw_sprites():
    if scene == 1:
        screen.blit(bg_image, (0, 0))
        draw_text("Slots Machine Game", game_font_big, txt_color, 450, 252.5)
        draw_text("BY IAN NORTHCUTT", game_font_big, txt_color, 450, 352.5)
        draw_text("PRESS SPACE TO START", game_font_big, txt_color, 400, 452.5)
    elif scene == 2:
        screen.blit(bg_image, (0, 0))
        Slots_animation()
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

def determin_slots():   
    global plays, images, slots2
    plays += 1
    slots = chance_dict[r.randint(1, 125)]
    slots2 = slots
    for i in range(num_slots):
        num = slots[i]
        slots[i] = images[num]
    return slots
    
    

def Slots_animation():
    global scene
    slots_images = [pygame.transform.scale(pygame.image.load(f"./images/slot{i+1}.png"), (200, 200)) for i in range(num_images)]
    slot_rects = [pygame.Rect(100 + i * 250, 300, 200, 200) for i in range(num_slots)]
    
    for i in range(30):  # Animation frames
        screen.blit(bg_image, (0, 0))
        for j in range(num_slots):
            image_index = (i + j) % num_images
            screen.blit(slots_images[image_index], slot_rects[j])
        
        pygame.display.flip()
        clock.tick(30)  # Control the speed of the animation
    
    final_images = determin_slots()
    for i in range(num_slots):
        image_index = final_images[i]
        screen.blit(pygame.transform.scale(pygame.image.load(image_index), (200, 200)), slot_rects[i])
    draw_text("Press space to continue", game_font_reg, txt_color, 20, 20)  # Move to the next scene after animation

def determin_win():
    global win_num
    for i in range(num_slots):
        if slots2[0] == 0 and slots2[1] == 0 and slots2[2] == 0:
            win_num = 1
        elif slots2[0] == 1 and slots2[1] == 1 and slots2[2] == 1:
            win_num = 1
        elif slots2[0] == 2 and slots2[1] == 2 and slots2[2] == 2:
            win_num = 1
        elif slots2[0] == 3 and slots2[1] == 3 and slots2[2] == 3:
            win_num = 2
        elif slots2[0] == 4 and slots2[1] == 4 and slots2[2] == 4:
            win_num = 3
        else:
            win_num = 0


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
                    Slots_animation()
                elif key[pygame.K_q] or key[pygame.K_ESCAPE] or key[pygame.K_END]:
                    print("You left the game. :|")
                    sys.exit()
            elif scene == 2:
                if key[pygame.K_SPACE]:
                    scene = 3
                if key[pygame.K_q] or key[pygame.K_ESCAPE] or key[pygame.K_END]:
                    print("You left the game. :|")
                    sys.exit()
            elif scene == 3:
                if key[pygame.K_SPACE] or key[pygame.K_s]:
                    scene = 1
                elif key[pygame.K_q] or key[pygame.K_ESCAPE] or key[pygame.K_END]:
                    print("You left the game. :|")
                    sys.exit()

    draw_sprites()

    # At the end of each game loop, call pygame.display.flip() to update the screen with all of your sprites
    pygame.display.flip()
