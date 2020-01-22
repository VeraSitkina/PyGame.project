from pygame.rect import Rect
import pygame
import random
from collections import defaultdict


WIDTH = 700
HEIGHT = 550
FPS = 35


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)


    def update(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
running = True

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit() 
class GameObject:
    def __init__(self, x, y, w, h, speed=(0,0)):
        self.bounds = Rect(x, y, w, h)
        self.speed = speed

    def left(self):
        return self.bounds.left

    def right(self):
        return self.bounds.right

    def top(self):
        return self.bounds.top

    def bottom(self):
        return self.bounds.bottom

    def width(self):
        return self.bounds.width

    def height(self):
        return self.bounds.height

    def center(self):
        return self.bounds.center

    def centerx(self):
        return self.bounds.centerx

    def centery(self):
        return self.bounds.centery

    def draw(self, surface):
        pass

    def move(self, dx, dy):
        self.bounds = self.bounds.move(dx, dy)

    def update(self):
        if self.speed == [0, 0]:
            return

        self.move(*self.speed)
        
        

class Game:
    def __init__(self, caption, width, height, back_image_filename, frame_rate):
        self.background_image = \
            pygame.image.load(back_image_filename)
        self.frame_rate = frame_rate
        self.game_over = False
        self.objects = []
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        pygame.init()
        pygame.font.init()
        self.surface = pygame.display.set_mode((width, height))
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()
        self.keydown_handlers = defaultdict(list)
        self.keyup_handlers = defaultdict(list)
        self.mouse_handlers = []
        
        
    def update(self):
        for o in self.objects:
            o.update()
    
    def draw(self):
        for o in self.objects:
            o.draw(self.surface)
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                for handler in self.keydown_handlers[event.key]:
                    handler(event.key)
            elif event.type == pygame.KEYUP:
                for handler in self.keydown_handlers[event.key]:
                        handler(event.key)
            elif event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEMOTION):
                for handler in self.mouse_handlers:
                    handler(event.type, event.pos)    
    def run(self):
            while not self.game_over:
                self.surface.blit(self.background_image, (0, 0))
    
                self.handle_events()
                self.update()
                self.draw()
    
                pygame.display.update()
                self.clock.tick(self.frame_rate)    

pygame.quit() 