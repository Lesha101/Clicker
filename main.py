import pygame
import random
import pgzrun


WIDTH = 600
HEIGHT = 380
TITLE = "World"
FPS = 60
b = Actor("buttun")
def draw():
    b.draw()
pgzrun.go()
