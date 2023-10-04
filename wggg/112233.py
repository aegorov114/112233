from pygame import *

window_size = [700, 500]
window = display.set_mode(window_size)
display.set_caption('Пинг-понг')
window.fill([240, 250, 235])

class GameSprite(sprite.Sprite): 
    def __init__(self, player_image ,x_size , y_size, x_cor, y_cor, speed_x, speed_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(x_size, y_size))
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.rect = self.image.get_rect()
        self.rect.x = x_cor
        self.rect.y = y_cor

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()   
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed_y 
        if keys_pressed[K_s] and self.rect.y <= 440:
            self.rect.y += self.speed_y
    def update_r(self):
        keys_pressed = key.get_pressed()   
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed_y
        if keys_pressed[K_DOWN] and self.rect.y <= 440:
            self.rect.y += self.speed_y

class Ball(GameSprite):
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y <= 0:
            self.speed_y *= -1
        if self.rect.y >= 480:
            self.speed_y *= -1
        if ball.rect.colliderect(rocket_l.rect) or ball.rect.colliderect(rocket_r.rect):
            self.speed_x *= -1
            self.speed_y *= 1


font.init()  
f = font.SysFont('Arial', 33)
rpl_score = ()      

rocket_l = Player('rocket.png', 40, 90, 5, 30, 0, 5)  
rocket_r = Player('rocket.png', 40, 90, 655, 30, 0, 5)
ball = Ball('ball.png', 20, 20, 250, 300, 3, 4)
game = True
FPS = 60
clock = time.Clock()
score_r = 0
score_l = 0

font.init()  
f = font.SysFont('Arial', 33)
 
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    rocket_l.update_l()
    rocket_r.update_r()
    ball.update()

    rpl_score = f.render(str(score_r), True, [255, 255, 255])
    lpl_score = f.render(str(score_l), True, [255, 255, 255])

    window.fill([240, 250, 235])
    window.blit(rpl_score,(20, 40))
    window.blit(lpl_score,(680, 40))



    if ball.rect.x <= -100:
        score_r += 1
        ball.rect.x = 350
    elif ball.rect.x >= 800:
        score_l += 1
        ball.rect.x = 350

    rocket_l.reset()
    rocket_r.reset()
    ball.reset()


    display.update()
    clock.tick(FPS)
    rocket_r.reset()


    display.update()
    clock.tick(FPS)