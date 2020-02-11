import pygame
import sys
import random
import time
import os


#������ ��������� ������
size = width, height = 700, 500
screen = pygame.display.set_mode(size)


#����� ��� ��������� ����
class Game():
    def __init__(self, fps):
        #������ ������� ������
        self.width = 700
        self.height = 500
        
        #������ �����
        self.play_surface = screen
        
        #����������� �����
        self.red = pygame.Color(255, 0, 0)
        self.green = pygame.Color(0, 255, 0)
        self.black = pygame.Color(0, 0, 0)
        self.white = pygame.Color(255, 255, 255)
        self.brown = pygame.Color(165, 42, 42)
        self.blue_green = pygame.Color(0,255,170)
        self.marroon = pygame.Color(115,0,0)
        self.lime = pygame.Color(180,255,100)
        self.pink = pygame.Color(255,100,180)
        self.purple = pygame.Color(240,0,255)
        
        #������ ��������
        self.speed_fps = [8, 15, 23]
        self.i_fps = fps
        
        #������ ���������� ������ � �������
        self.fps_control = pygame.time.Clock()
        
        #���������� ��� ������������ ���������� (������� ��� �����)
        self.score = 0
    
    def init_and_check_for_errors(self):
        #��������� ������� ��� ������������� � �������� ��� ���������� pygame
        check_errors = pygame.init()
        if check_errors[1] > 0:
            sys.exit()
        else:
            print('Ok')
            
    def set_title(self):
        #������ surface(����������� ������ ������� ����� ��� ����������) � ������������� ��������� ����
        pygame.display.set_caption('Snake Game')
    
    def refresh_screen(self):
        #��������� ����� � ������ ��� (�������� ����������� ������)
        pygame.display.flip()
        game.fps_control.tick(self.speed_fps[self.i_fps])
        
    def show_score(self, choice=1):
        #����������� ����������
        s_font = pygame.font.SysFont('comicsansms', 24)
        s_surf = s_font.render('����: {0}'.format(self.score), True, self.black)
        s_rect = s_surf.get_rect()
        
        #��������� ������ ���������� ��������� ����� ������
        if choice == 1:
            s_rect.midtop = (80, 10)
        #��� game_overe ���������� ��������� �� ������ ��� �������� game over
        else:
            s_rect.midtop = (360, 200)
        
        #������ ������������� ������ surface
        self.play_surface.blit(s_surf, s_rect)
                
    def game_over(self):
        #������� ��� ������ ������� Game Over � ����������� � ������ ���������� ���� � ����� �� ����
        
        go_font = pygame.font.SysFont('comicsansms', 72)
        go_surf = go_font.render('Game over', True, self.red)
        go_rect = go_surf.get_rect()
        go_rect.midtop = (360, 100)
        self.play_surface.blit(go_surf, go_rect)
        self.show_score(0)
        pygame.display.flip()
        time.sleep(3)
        pygame.quit()
        sys.exit()
          

#����� ��� ����
class Snake():
    def __init__(self, snake_color):
        #������ ���������� - ������� ������ ���� � ��� ����
        self.snake_head_pos = [100, 50]  # [x, y]
        
        #��������� ���� ���� ������� �� ���� ���������
        #������ ���� - ������ �������, ����� - ���������
        self.snake_body = [[100, 50], [90, 50], [80, 50]]
        self.snake_color = snake_color
        
        #����������� �������� ����, ���������� ��������� ������
        self.direction = "RIGHT"
        
        #���� ����� �������� ���������� �������� ���� ��� ������� ��������������� ������
        self.change_to = self.direction
        
    def validate_direction_and_change(self):
        #��������� ����������� �������� ���� ������ � ��� ������, ���� ��� �� ����� �������������� ��������
        if (self.change_to == "RIGHT" and not self.direction == "LEFT") or (self.change_to == "LEFT" and not self.direction == "RIGHT") or (self.change_to == "UP" and not self.direction == "DOWN") or (self.change_to == "DOWN" and not self.direction == "UP"):
            self.direction = self.change_to
            
    def change_head_position(self):
        #��������� ��������� ������ ����
        if self.direction == "RIGHT":
            self.snake_head_pos[0] += 10
        elif self.direction == "LEFT":
            self.snake_head_pos[0] -= 10
        elif self.direction == "UP":
            self.snake_head_pos[1] -= 10
        elif self.direction == "DOWN":
            self.snake_head_pos[1] += 10
            
    def snake_body_mechanism(self, score, food_pos, width, height):
        #���� ��������� ������ snake_head_pos, �� �� ���� ���� �������� � snake_body
        #�������� ���� � ��� �� ������ � ����������� ������������ � �� ����� ��������� ����� �� ������ ��������
        self.snake_body.insert(0, list(self.snake_head_pos))
        
        #���� ����� ���
        if (self.snake_head_pos[0] == food_pos[0] and self.snake_head_pos[1] == food_pos[1]):
            #���� ����� ��� �� ������ ����� ��������� ��� ��������� ������� � ���������� score �� ����
            food_pos = [random.randrange(1, width / 10) * 10, random.randrange(1, height / 10) * 10]
            score += 1
        else:
            #���� �� ����� ���, �� ������� ��������� �������, ���� ����� �� �������, �� ���� ����� ��������� �����
            self.snake_body.pop()
        
        return score, food_pos
    
    def draw_snake(self, play_surface, surface_color):
        #���������� ��� �������� ����
        play_surface.fill(surface_color)
        for pos in self.snake_body:
            #pygame.Rect(x,y, sizex, sizey)
            pygame.draw.rect(play_surface, self.snake_color, pygame.Rect(pos[0], pos[1], 10, 10))
            
    def check_for_boundaries(self, game_over, width, height):
        #��������, ��� ����������� � ������� ������ ��� ���� � ����� (���� ��������������)
        if (self.snake_head_pos[0] > width - 10 or self.snake_head_pos[0] < 0) or (self.snake_head_pos[1] > height - 10 or self.snake_head_pos[1] < 0):
            game_over()
            
        for block in self.snake_body[1:]:
            #�������� �� ��, ��� ������ �������(������) �������� � ����� ������ ������� ���� (��������������)
            if (block[0] == self.snake_head_pos[0] and block[1] == self.snake_head_pos[1]):
                game_over()
                

class Food():
    def __init__(self, food_color, width, height):
        #���� ���
        self.food_color = food_color
        self.food_size_x = 10
        self.food_size_y = 10
        self.food_pos = [random.randrange(1, width / 10) * 10, random.randrange(1, height / 10) * 10]
    
    def draw_food(self, play_surface):
        #����������� ���
        pygame.draw.rect(play_surface, self.food_color, 
                         pygame.Rect(self.food_pos[0], self.food_pos[1], self.food_size_x, self.food_size_y))


#�������� �����������
def load_image(name, colorkey=None):
    try:
        image = pygame.image.load(name).convert()
    except pygame.error as message:
        print('Cannot load image: ', name)
        raise SystemExit(message)
    
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    
    image = pygame.transform.scale(image, (250, 250))
    return image


#����� ��� ����������� �������� �� ������� ������
class Image_snake(pygame.sprite.Sprite):
    #��������� ��������
    image = load_image("snake.png")
    
    def __init__(self):
        #������������� ������� ��� ��������
        super().__init__(all_sprites)
        self.image = Image_snake.image
        self.rect = self.image.get_rect()
        self.rect.x = 230
        self.rect.y = 50      
        

#������� ������� ��� ������� ����
def main(fps):
    #������ ��������� ���� (��������)
    game = Game(fps)
    
    #�������� ������
    pygame.mixer.music.load('Boss Battle.mp3')
    pygame.mixer.music.play()
    
    running = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    running = False         
            #����������� ������� ������ ��� �������� ����
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    snake.change_to = "RIGHT"
                elif event.key == pygame.K_LEFT or event.key == ord('a'):
                    snake.change_to = "LEFT"
                elif event.key == pygame.K_UP or event.key == ord('w'):
                    snake.change_to = "UP"
                elif event.key == pygame.K_DOWN or event.key == ord('s'):
                    snake.change_to = "DOWN"
                elif event.key == pygame.K_ESCAPE or event.key == pygame.K_SPACE:
                    running = False
        
        snake.validate_direction_and_change()
        snake.change_head_position()
        game.score, food.food_pos = snake.snake_body_mechanism(game.score, food.food_pos, game.width, game.height)
        snake.draw_snake(game.play_surface, game.white)
        
        food.draw_food(game.play_surface)
        snake.check_for_boundaries(game.game_over, game.width, game.height)
        
        game.show_score()
        game.refresh_screen()
    
    pygame.display.quit()
    sys.exit()


#������� ��� ����������� ������ �� ������� ������
def draw_text(surface, text, size, color, x, y):
    font = pygame.font.SysFont("comicsansms", size, bold=True)
    label = font.render(text, 1, color)

    surface.blit(label, (x, y))


#������� ����� ��� ������� ����
def start(screen):
    running = True
    
    while running:     
        fon_color = pygame.Color(0, 0, 0)
        screen.fill(fon_color)
        color = pygame.Color(255, 255, 255)
        draw_text(screen, '������� 1 (������ �������)', 25, color, 180, 350)
        draw_text(screen, '������� 2 (������� �������)', 25, color, 175, 390)
        draw_text(screen, '������� 3 (������� �������)', 25, color, 170, 430)
        
        all_sprites.draw(screen)
        all_sprites.update()
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == ord('1'):
                    main(0)
                if event.key == ord('2'):
                    main(1)
                if event.key == ord('3'):
                    main(2)
                    
    pygame.display.quit()
    

#�������� �����������
all_sprites = pygame.sprite.Group()
image_snake = Image_snake() 

#������������� �������
game = Game(1)
snake = Snake(game.green)
food = Food(game.brown, game.width, game.height)

game.init_and_check_for_errors()
game.set_title()

#������ ����
start(screen)