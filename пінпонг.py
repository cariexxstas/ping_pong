from pygame import*
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

back = (200, 255, 255)
win_height = 500
win_weight = 600
window = display.set_mode((win_weight, win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60

recket1 = Player('img.png', 30, 200, 4, 50, 150)
recket2 = Player('img.png', 520, 200, 4, 50, 150)
ball = GameSprite('ball.png', 200, 200, 4, 50, 50)

font.init()
font = font.SysFont("Arial", 35)
lose1 = font.render("PLAYER 1 LOSE!", True, (180, 0, 0))
lose2 = font.render("PLAYER 2 LOSE!", True, (180, 0, 0))

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        keys = key.get_pressed()
        window.fill(back)
        recket1.update_l()
        recket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(recket1, ball) or sprite.collide_rect(recket2, ball):
            speed_x *=-1
            speed_y *=1

        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *=-1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            finish = False
            if keys[K_r]:

                ball.rect.x = 300
                ball.rect.y = 250

        if ball.rect.x > win_weight:
            finish = True
            window.blit(lose2, (200, 200))
            finish = False
            if keys[K_r]:

                ball.rect.x = 300
                ball.rect.y = 250

        recket1.reset()
        recket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)
