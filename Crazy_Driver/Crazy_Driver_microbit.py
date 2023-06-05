import time
import random
import pygame
from pygame import mixer
import serial
import threading, queue

# imposta la finestra di pygame
TITLE="Crazy Driver"
WIDTH = 640
HEIGHT = 480
CORSIE=[70, 135, 220, 310] 

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)

# clock
clock = pygame.time.Clock()

#imposta il player
player_image = pygame.image.load("immagini\player.png")
player_rect = player_image.get_rect()
player_rect.x = 32
player_rect.y = CORSIE[0]

# imposta i van
enemy_image = pygame.image.load("immagini\enemy.png")
enemy_rect = enemy_image.get_rect()
enemy_rect.x = WIDTH 
enemy_rect.y = enemy_rect.y = CORSIE[random.randrange(0,3)] #sceglie una corsia casuale su cui mettere il vam

enemy_1_image = pygame.image.load("immagini\enemy01.png")
enemy_1_rect = enemy_1_image.get_rect()
enemy_1_rect.x = WIDTH 
enemy_1_rect.y = enemy_rect.y = CORSIE[random.randrange(0,3)]

enemy_2_image = pygame.image.load("immagini\enemy02.png")
enemy_2_rect = enemy_2_image.get_rect()
enemy_2_rect.x = WIDTH  -60
enemy_2_rect.y = enemy_rect.y = CORSIE[random.randrange(0,3)]

enemy_3_image = pygame.image.load("immagini\enemy03.png")
enemy_3_rect = enemy_3_image.get_rect()
enemy_3_rect.x = WIDTH 
enemy_3_rect.y = enemy_rect.y = CORSIE[random.randrange(0,3)]


#imposta lo stato iniziale del gioco

game_over = False
#imposta una serie di variabili per timer di ms
ms=0
en0=0
en1=0
en2=0
en3=0
score=0
#imposta il testo
font=pygame.font.Font('font\Gameplay.ttf', 40)
over_font=pygame.font.Font('font\Gameplay.ttf', 64)
textx=10
texty=10
def showScore(x,y): #mostra il punteggio
    scoret=font.render("Score:"+str(score), True, (183, 28, 2))
    screen.blit(scoret, (x, y))

def gameOverText(): #testo del game over
    over_text=over_font.render("GAME OVER", True, (183, 0, 0))
    screen.blit(over_text, (100,100))

def End(): #mostra lo schermo del game over
    crash=mixer.Sound('suoni\\boom9.wav')
    crash.play()
    mixer.music.load('suoni\Free Bird 8-bit.mp3')
    mixer.music.play(1)
    screen.fill((0,0,0))
    showScore(215,250)
    gameOverText()
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()

#resetta la posizione dei van una volta che sono passati
def respos(posx, posy):
    posy = CORSIE[random.randrange(0,4)]
    posx = WIDTH
    return posx, posy

#colonna sonora
mixer.music.load('suoni\Free Bird 8-bit.mp3')
mixer.music.play(-1,287)

# sfondo 
bg = pygame.image.load("immagini\\bg.png")



#loop fino al game over
while not game_over:

    # condizione di uscita dal gioco
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over = True
    
    # comandi del gioco
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        if player_rect.y +5 <335:
            player_rect.y += 5
    if keys[pygame.K_UP]:
        if player_rect.y -5 >50:
            player_rect.y -= 5
    if keys[pygame.K_RIGHT]:
        if player_rect.x +157 <WIDTH:
            player_rect.x += 5
    if keys[pygame.K_LEFT]:
        if player_rect.x -5 >0:
            player_rect.x -= 5

    #muove e resetta i van
    enemy_rect.x -=5
    enemy_1_rect.x -=5
    enemy_2_rect.x -=5
    enemy_3_rect.x -=5
    if enemy_rect.x < -150: #controlla se il van è uscito dallo schermo

        #timer di millisecondi che serve per randomizzare il momento in cui i van vengono riportati a destra dello schermo
        #in modo che non si sovrappongano(nella maggior parte dei casi)
        en0=pygame.time.get_ticks() 
        if ms - en3 > random.randrange(50,1000):  
            enemy_rect.x, enemy_rect.y = respos(enemy_rect.x, enemy_rect.y) 
            score+=1   #aumenta il punteggio
    
    if enemy_1_rect.x < -150:
        en1=pygame.time.get_ticks()

        if ms - en0 > random.randrange(900,1000):
            enemy_1_rect.x, enemy_1_rect.y=respos(enemy_1_rect.x, enemy_1_rect.y)
            score+=1  

    if enemy_2_rect.x < -150:
        en2=pygame.time.get_ticks()
        if ms - en1 > random.randrange(130,1000):
            enemy_2_rect.x, enemy_2_rect.y=respos(enemy_2_rect.x, enemy_2_rect.y)
            score+=1  

    if enemy_3_rect.x < -150:
        en3=pygame.time.get_ticks()
        if ms - en2 > random.randrange(560,1000):
         enemy_3_rect.x, enemy_3_rect.y=respos(enemy_3_rect.x, enemy_3_rect.y)
         score+=1  

    # Controlla le collisioni
    if player_rect.colliderect(enemy_rect) or player_rect.colliderect(enemy_1_rect) or player_rect.colliderect(enemy_2_rect) or player_rect.colliderect(enemy_3_rect):
        game_over = True
    
    # Disegna lo schermo
    screen.blit(bg, (0, 0))
    screen.blit(player_image, player_rect)
    screen.blit(enemy_image, enemy_rect)
    screen.blit(enemy_1_image, enemy_1_rect)
    screen.blit(enemy_2_image, enemy_2_rect)
    screen.blit(enemy_3_image, enemy_3_rect)
    showScore(textx,texty) #richimama la funzione che mostra il punteggio
    pygame.display.flip()
    ms=pygame.time.get_ticks() #ms attuali, variabile per i timer
    #frame rate
    clock.tick(60)

End()

