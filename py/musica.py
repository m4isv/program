import pygame_sdl2
pygame_sdl2.init()
pygame_sdl2.mixer.music.load("alan.mp3")
pygame_sdl2.mixer.music.play()
pygame_sdl2.event.wait()