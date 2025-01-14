import random

import pygame

# 初始化pygame
pygame.init()

# 游戏窗口大小
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# 设置标题和时钟
pygame.display.set_caption('坦克大战')
clock = pygame.time.Clock()

# 颜色定义
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)


# 坦克类
class Tank(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height - 50)
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed


# 敌人类
class EnemyTank(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - 50)
        self.rect.y = random.randint(-100, -50)
        self.speed = 3

    def move(self):
        self.rect.y += self.speed
        if self.rect.y > screen_height:
            self.rect.x = random.randint(0, screen_width - 50)
            self.rect.y = random.randint(-100, -50)


# 创建坦克实例
player_tank = Tank()

# 创建敌人组
enemy_tanks = pygame.sprite.Group()
for i in range(5):
    enemy = EnemyTank()
    enemy_tanks.add(enemy)

# 主游戏循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 获取按键状态
    keys = pygame.key.get_pressed()
    player_tank.move(keys)

    # 更新敌人位置
    enemy_tanks.update()

    # 绘制背景
    screen.fill(black)

    # 绘制坦克
    screen.blit(player_tank.image, player_tank.rect)

    # 绘制敌人
    for enemy in enemy_tanks:
        screen.blit(enemy.image, enemy.rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
