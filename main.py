import sys, os, pygame, random as r, itertools

os.environ['SDL_AUDIODRIVER'] = 'dsp' # fix sound playback

# Initialize PyGame's internal variables
pygame.init()

pygame.display.set_caption('  Fruti Slots  ')

# Set up variables for the screen size in pixels
size = (1280, 865)

# Initialize a window with the screen size you set
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
fps = 60

bg_image = pygame.image.load("./images/bg_image.jpg")
icon = pygame.image.load("./images/icon.png")

pygame.display.set_icon(icon)

music_playing = False

# vars
win_num = None
# win messages
win = ["You Lost", "You Won", "You won the Jackpot"]
images = ["images/slot1.png", "images/slot2.png", "images/slot3.png", "images/slot4.png", "images/slot5.png", "images/slot6.png", "images/slot7.png", "images/slot8.png", "images/slot9.png", "images/slot10.png"]
num_images = 10
chance_dict = {}
num = 0
num_slots = 5
for i in itertools.product([0,1,2,3,4,5,6,7,8,9], repeat=num_slots):
    chance_dict[num] = i
    num += 1
# Load images for the slots
slots_images = [pygame.transform.scale(pygame.image.load(f"./images/slot{i+1}.png"), (200, 200)) for i in range(num_images)]    
# Colors
txt_color = (255, 255, 255)  
# fonts
game_font_small = pygame.font.Font(None, 25)
game_font_reg = pygame.font.Font(None, 50)
game_font_big = pygame.font.Font(None, 100)

scene = 1

def draw_sprites():
    if scene == 1:
        screen.blit(bg_image, (0, 0))
        draw_text("Fruti Slots", game_font_big, txt_color, 440, 552.5)
        draw_text("BY IAN NORTHCUTT", game_font_big, txt_color, 310, 652.5)
        draw_text("PRESS SPACE TO START", game_font_big, txt_color, 260, 752.5)
    elif scene == 2:
        screen.blit(bg_image, (0, 0))
        Slots_animation()

def draw_text(text, font, color, x, y):
    image = font.render(text, True, color)
    screen.blit(image, (x, y))

def determin_slots():   
    global images, win_num
    slots = chance_dict[r.randint(1, len(chance_dict) - 1)]
    slots1 = []
    for i in range(num_slots):
        num = slots[i]
        slots1.append(images[num])
    for i in range(num_slots):
        if slots[0] == 0 and slots[1] == 0 and slots1[2] == 0 and slots1[3] == 0 and slots1[4] == 0 and slots1[5] == 0 and slots1[6] == 0 and slots1[7] == 0 and slots1[8] == 0 and slots1[9] == 0:
            win_num = 1
        elif slots[0] == 1 and slots[1] == 1 and slots1[2] == 1 and slots1[3] == 1 and slots1[4] == 1 and slots1[5] == 1 and slots1[6] == 1 and slots1[7] == 1 and slots1[8] == 1 and slots1[9] == 1:
            win_num = 1
        elif slots[0] == 2 and slots[1] == 2 and slots1[2] == 2 and slots1[3] == 2 and slots1[4] == 2 and slots1[5] == 2 and slots1[6] == 2 and slots1[7] == 2 and slots1[8] == 2 and slots1[9] == 2:
            win_num = 1
        elif slots[0] == 3 and slots[1] == 3 and slots1[2] == 3 and slots1[3] == 3 and slots1[4] == 3 and slots1[5] == 3 and slots1[6] == 3 and slots1[7] == 3 and slots1[8] == 3 and slots1[9] == 3:
            win_num = 1
        elif slots[0] == 4 and slots[1] == 4 and slots1[2] == 4 and slots1[3] == 4 and slots1[4] == 4 and slots1[5] == 4 and slots1[6] == 4 and slots1[7] == 4 and slots1[8] == 4 and slots1[9] == 4:
            win_num = 1
        elif slots[0] == 5 and slots[1] == 5 and slots1[2] == 5 and slots1[3] == 5 and slots1[4] == 5 and slots1[5] == 5 and slots1[6] == 5 and slots1[7] == 5 and slots1[8] == 5 and slots1[9] == 5:
            win_num = 1
        elif slots[0] == 6 and slots[1] == 6 and slots1[2] == 6 and slots1[3] == 6 and slots1[4] == 6 and slots1[5] == 6 and slots1[6] == 6 and slots1[7] == 6 and slots1[8] == 6 and slots1[9] == 6:
            win_num = 1
        elif slots[0] == 7 and slots[1] == 7 and slots1[2] == 7 and slots1[3] == 7 and slots1[4] == 7 and slots1[5] == 7 and slots1[6] == 7 and slots1[7] == 7 and slots1[8] == 7 and slots1[9] == 7:
            win_num = 1
        elif slots[0] == 8 and slots[1] == 8 and slots1[2] == 8 and slots1[3] == 8 and slots1[4] == 8 and slots1[5] == 8 and slots1[6] == 8 and slots1[7] == 8 and slots1[8] == 8 and slots1[9] == 8:
            win_num = 1
        elif slots[0] == 9 and slots[1] == 9 and slots1[2] == 9 and slots1[3] == 9 and slots1[4] == 9 and slots1[5] == 9 and slots1[6] == 9 and slots1[7] == 9 and slots1[8] == 9 and slots1[9] == 9:
            win_num = 1
        elif slots[0] == 0 and slots[1] == 1 and slots1[2] == 2 and slots1[3] == 3 and slots1[4] == 4 and slots1[5] == 5 and slots1[6] == 6 and slots1[7] == 7 and slots1[8] == 8 and slots1[9] == 9:
            win_num = 2
        else:
            win_num = 0
    return slots1
    
def Slots_animation():
    global scene, win_num, num_of_wins
    slot_rects = [pygame.Rect(40 + i * 250, 300, 200, 200) for i in range(num_slots)]
    for i in range(30):  # Animation frames
        screen.blit(bg_image, (0, 0))
        for j in range(num_slots):
            image_index = (i + j) % num_images
            screen.blit(slots_images[image_index], slot_rects[j])
        
        pygame.display.flip()
        clock.tick(30)  # Control the speed of the animation
    
    final_images = determin_slots()
    screen.blit(bg_image, (0, 0))
    for i in range(num_slots):
        image_index = final_images[i]
        screen.blit(pygame.transform.scale(pygame.image.load(image_index), (200, 200)), slot_rects[i])
    draw_text(f"{win[win_num]} Press space to play again", game_font_reg, txt_color, 20, 20)  
    scene = 3 # Move to the next scene after animation

print()

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
                if key[pygame.K_SPACE]:
                    scene = 3
                if key[pygame.K_q] or key[pygame.K_ESCAPE] or key[pygame.K_END]:
                    print("You left the game. :|")
                    sys.exit()
            elif scene == 3:
                if key[pygame.K_SPACE]:
                    scene = 1
                elif key[pygame.K_q] or key[pygame.K_ESCAPE] or key[pygame.K_END]:
                    print("You left the game. :|")
                    sys.exit()

    draw_sprites()

    # At the end of each game loop, call pygame.display.flip() to update the screen with all of your sprites
    pygame.display.flip()
