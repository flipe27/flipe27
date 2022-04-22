import pygame

# Existem diversas maneiras de reproduzir áudio, outro exemplo seria a biblioteca "playsound"
pygame.init()
pygame.mixer.music.load('phoenix.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
