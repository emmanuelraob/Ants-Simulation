import pygame

class Node:
    def __init__(self, x, y, width, height, objects, level):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.objects = objects
        self.nodes = []
        self.rect = pygame.Rect(x - width / 2, y - height / 2, width, height)
        self.level = level

    def has_children(self):
        return len(self.nodes) > 0