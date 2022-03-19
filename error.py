from operator import truediv
import pygame,random,winsound
from pygame.locals import *
from random import randint
OK=randint(1,2)
if OK == 3:
    exit()
pygame.init()
def BOSS_A():
    font = pygame.font.SysFont('arial',60)
    text_surface = font.render(u"Error",False,(225,0,0))
    screen.blit(text_surface,(randint(0,320),randint(0,30)))   
    screen.blit(text_surface,(randint(0,320),randint(0,30)))
    screen.blit(text_surface,(randint(0,320),randint(0,30)))
    screen.blit(text_surface,(randint(0,320),randint(0,30)))
    screen.blit(text_surface,(randint(0,320),randint(0,30)))
    screen.blit(text_surface,(randint(0,320),randint(0,30)))
    screen.blit(text_surface,(randint(0,320),randint(0,30)))
    screen.blit(text_surface,(randint(0,320),randint(0,30)))
    pygame.draw.rect(screen,(225,0,0),(50,90,BOSS*12,20),0)
    pygame.draw.rect(screen,(225,225,225),(ball_x,ball_y,20,20),0)
    pygame.draw.rect(screen,(225,225,225),(g_x,g_y,80,20),0)
    pygame.display.flip()
def qu_it():
    if event.type == pygame.QUIT:
        font = pygame.font.SysFont('Simhei',40)
        text_surface = font.render(u"sb,退出不了",False,(225,0,0))
        screen.blit(text_surface,(randint(0,320),randint(0,400)))
screen=pygame.display.set_mode((320,400))
pygame.display.set_caption('Pinball game')
ball_x,ball_y,g_x,g_y,rgb=150,180,140,380,0
sd_x,sd_y,g,fs,gameover=10,10,10,-1,0
BOSS,BOSSgj=20,1
while True:
    if fs ==-3:
        font = pygame.font.SysFont('arial',60)
        text_surface = font.render("GAME OVER",True,(225,225,225))
        one = font.render(f"{fs}",True,(225,225,225))
        screen.blit(text_surface,(20,70))
        screen.blit(one,(320,70))
        pygame.display.flip()
        pygame.time.delay(10)
    #开始界面
    if fs==-1:
        font = pygame.font.SysFont('Simhei',50)
        one = font.render("Pinball game",True,(rgb,rgb,rgb))
        font = pygame.font.SysFont('Simhei',30)
        two = font.render("请按空格\n键开始",True,(rgb,rgb,rgb))
        screen.blit(one,(12,60))
        screen.blit(two,(50,300))
        if rgb <= 224:
            rgb+=25
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    fs = -0.9
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_f:
                    fs = 41
                    BOSS =1
            if event.type == pygame.QUIT:
                exit()
        pygame.display.flip()
        pygame.time.delay(100)
    if fs == -0.9:
        screen.fill((0,0,0))
        font = pygame.font.SysFont('Simhei',20)
        two = font.render("作为一款游戏，肯定得有一个角色",True,(rgb,rgb,rgb))
        screen.blit(two,(15,100))
        pygame.display.flip()
        pygame.time.delay(1000)
        fs =-0.8
    if fs == -0.8:
        screen.fill((0,0,0))
        font = pygame.font.SysFont('Simhei',20)
        two = font.render("这个是你，你可以按下左←键看看",True,(rgb,rgb,rgb))
        screen.blit(two,(15,100))
        pygame.draw.rect(screen,(225,225,225),(g_x,g_y,80,20),0)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_LEFT:
                    g_x-=g
                    fs=-0.7   
        pygame.time.delay(10)
    if fs==-0.7:
        screen.fill((0,0,0))
        font = pygame.font.SysFont('Simhei',20)
        two = font.render("干得不错，你可以按下右→键看看",True,(rgb,rgb,rgb))
        screen.blit(two,(15,100))
        pygame.draw.rect(screen,(225,225,225),(g_x,g_y,80,20),0)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_RIGHT:
                    g_x+=g
                    fs=-0.6   
        pygame.time.delay(10)
    if fs ==-0.6:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_LEFT:
                    g_x-=g
                if event.key == pygame.K_RIGHT:
                    g_x+=g
            if event.type == pygame.QUIT:
                exit()
        screen.fill((0,0,0))
        ball_x+=sd_x
        ball_y-=sd_y
        if ball_x+17>=320:
            sd_x-=20
        if ball_x<=0:
            sd_x+=20
        if ball_y<=0:
            sd_y-=20
        if ball_y>=360:
            if ball_x>g_x and ball_x<=g_x+80:
                sd_y+=20
                fs=1
        if ball_y>=380:
            fs=-3
        font = pygame.font.SysFont('Simhei',30)
        one = font.render("不错，尝试接住球吧",True,(225,225,225))
        screen.blit(one,(20,70))
        pygame.draw.rect(screen,(225,225,225),(ball_x,ball_y,20,20),0)
        pygame.draw.rect(screen,(225,225,225),(g_x,g_y,80,20),0)
        pygame.display.flip()
        pygame.time.delay(100)  
    #第一阶段
    if fs<=5 and fs>=0:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_LEFT:
                    g_x-=g
                if event.key == pygame.K_RIGHT:
                    g_x+=g
            if event.type == pygame.QUIT:
                exit()
        screen.fill((0,0,0))
        ball_x+=sd_x
        ball_y-=sd_y
        if ball_x+17>=320:
            sd_x-=20
        if ball_x<=0:
            sd_x+=20
        if ball_y<=0:
            sd_y-=20
        if ball_y>=360:
            if ball_x>g_x and ball_x<=g_x+80:
                sd_y+=20
                fs+=1
        if ball_y>=380:
            fs=-3
        font = pygame.font.SysFont('Simhei',30)
        text_surface = font.render(f"得分:{fs}",True,(225,225,225))
        screen.blit(text_surface,(20,70))
        pygame.draw.rect(screen,(225,225,225),(ball_x,ball_y,20,20),0)
        pygame.draw.rect(screen,(225,225,225),(g_x,g_y,80,20),0)
        pygame.display.flip()
        pygame.time.delay(100)
    #死亡机制
    if fs==-2:
        font = pygame.font.SysFont('arial',40)
        text_surface = font.render(u"Error",False,(225,0,0))
        screen.blit(text_surface,(randint(0,320),randint(0,400)))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
        pygame.display.flip()
        pygame.time.delay(10)
    #第二阶段
    if fs>=5 and fs<=10:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_LEFT:
                    g_x-=g
                if event.key == pygame.K_RIGHT:
                    g_x+=g
            if event.type == pygame.QUIT:
                exit()
        ball_x+=sd_x
        ball_y-=sd_y
        if ball_x+17>=320:
            sd_x-=20
        if ball_x<=0:
            sd_x+=20
        if ball_y<=0:
            sd_y-=20
        if ball_y>=360:
            if ball_x>g_x and ball_x<=g_x+80:
                sd_y+=20
                fs+=1
        if ball_y>=380:
            fs=-2
        font = pygame.font.SysFont('Simhei',30)
        text_surface = font.render(f"得分:{fs}",False,(225,0,0))
        screen.blit(text_surface,(20,70))
        pygame.draw.rect(screen,(225,225,225),(ball_x,ball_y,20,20),0)
        pygame.draw.rect(screen,(225,225,225),(g_x,g_y,80,20),0)
        pygame.display.flip()
        pygame.time.delay(100)
    #第三阶段
    if fs>=11:
        winsound.Beep(randint(37,32767),100)
    if fs>=11 and fs<=15:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_LEFT:
                    g=-10
                if event.key == pygame.K_RIGHT:
                    g=10
            qu_it()
        screen.fill((0,0,0))
        ball_x+=sd_x
        ball_y-=sd_y
        g_x+=g
        if ball_x+17>=320:
            sd_x-=20
        if ball_x<=0:
            sd_x+=20
        if ball_y<=0:
            sd_y-=20
        if ball_y>=360:
            if ball_x>g_x and ball_x<=g_x+80:
                sd_y+=20
                fs+=1
        if ball_y>=380:
            fs=-2
        if g_x<=0:
            fs=-2
        if g_x+80>=320:
            fs=-2
        pygame.display.set_caption('ERROR')
        font = pygame.font.SysFont('Simhei',30)
        text_surface = font.render(f"error:{fs}",False,(225,0,0))
        screen.blit(text_surface,(randint(20,30),70))
        text_surface = font.render("嘿，你看起来要死了",False,(225,0,0))
        screen.blit(text_surface,(20,200))
        pygame.draw.rect(screen,(225,225,225),(ball_x,ball_y,20,20),0)
        pygame.draw.rect(screen,(221,99,20),(g_x,g_y,80,20),0)
        pygame.display.flip()
        pygame.time.delay(10)

    #第四阶段
    if fs>=16 and fs<=20:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_LEFT:
                    g=-10
                if event.key == pygame.K_RIGHT:
                    g=10
            qu_it()
        ball_x+=sd_x
        ball_y-=sd_y
        g_x+=g
        if ball_x+17>=320:
            sd_x-=20
        if ball_x<=0:
            sd_x+=20
        if ball_y<=0:
            sd_y-=20
        if ball_y>=360:
            if ball_x>g_x and ball_x<=g_x+80:
                sd_y+=20
                fs+=1
        if ball_y>=380:
            fs=-2
        if g_x<=0:
            fs=-2
        if g_x+80>=320:
            fs=-2
        font = pygame.font.SysFont('arial',30)
        text_surface = font.render(f"error:{fs}",False,(225,0,0))
        screen.blit(text_surface,(randint(20,30),70))
        pygame.draw.rect(screen,(225,225,225),(ball_x,ball_y,20,20),0)
        pygame.draw.rect(screen,(221,99,20),(g_x,g_y,80,20),0)
        text_surface = font.render(u"SB",False,(225,0,0))
        screen.blit(text_surface,(randint(0,320),randint(0,400)))
        pygame.display.flip()
        pygame.time.delay(10)
    #第五阶段
    if fs>=21 and fs<=28:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_LEFT:
                    g_x-=g
                if event.key == pygame.K_RIGHT:
                    g_x+=g
            qu_it()
        screen.fill((0,0,0))
        ball_x+=sd_x
        ball_y-=sd_y
        if ball_x+17>=320:
            sd_x-=20
        if ball_x<=0:
            sd_x+=20
        if ball_y<=0:
            sd_y-=20
        if ball_y>=360:
            if ball_x>g_x and ball_x<=g_x+80:
                sd_y+=20
                fs+=1
        if ball_y>=380:
            fs=-2
        pygame.draw.rect(screen,(225,225,225),(ball_x,ball_y,20,20),0)
        pygame.draw.rect(screen,(225,225,225),(g_x,g_y,80,20),0)
        font = pygame.font.SysFont('arial',30)
        text_surface = font.render(u"Error",False,(225,0,0))
        screen.blit(text_surface,(randint(0,320),randint(0,400)))
        text_surface = font.render(f"error:{fs}",False,(225,0,0))
        screen.blit(text_surface,(randint(20,30),70))
        pygame.display.flip()
        pygame.time.delay(100)
    #第六上半阶段
    if fs>=26 and fs<=28:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_LEFT:
                    g_x-=g
                if event.key == pygame.K_RIGHT:
                    g_x+=g
            qu_it()
        screen.fill((225,225,225))
        ball_x+=sd_x
        ball_y-=sd_y
        if ball_x+17>=320:
            sd_x-=20
        if ball_x<=0:
            sd_x+=20
        if ball_y<=0:
            sd_y-=20
        if ball_y>=360:
            if ball_x>g_x and ball_x<=g_x+80:
                sd_y+=20
                fs+=1
        if ball_y>=380:
            fs=-2
        font = pygame.font.SysFont('arial',30)
        text_surface = font.render(f"error:{fs}",False,(225,0,0))
        screen.blit(text_surface,(randint(20,30),70))
        pygame.draw.rect(screen,(225,225,225),(ball_x,ball_y,20,20),0)
        pygame.draw.rect(screen,(225,225,225),(g_x,g_y,80,20),0)
        pygame.display.flip()
        pygame.time.delay(10)
    #第六下半阶段
    if fs<=29 and fs>=30:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_LEFT:
                    g_x-=g
                if event.key == pygame.K_RIGHT:
                    g_x+=g
            qu_it()
        screen.fill((225,225,225))
        ball_x+=sd_x
        ball_y-=sd_y
        if ball_x+17>=320:
            sd_x-=20
        if ball_x<=0:
            sd_x+=20
        if ball_y<=0:
            sd_y-=20
        if ball_y>=360:
            if ball_x>g_x and ball_x<=g_x+80:
                sd_y+=20
                fs+=1
        if ball_y>=380:
            fs=-2
        font = pygame.font.SysFont('arial',30)
        text_surface = font.render(f"error:{fs}",False,(225,0,0))
        screen.blit(text_surface,(randint(20,30),70))
        pygame.draw.rect(screen,(225,225,225),(ball_x,ball_y,20,20),0)
        pygame.draw.rect(screen,(225,225,225),(g_x,g_y,80,20),0)
        pygame.display.flip()
        pygame.time.delay(100)
    #第七上半阶段
    if fs>=31 and fs<=35:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_LEFT:
                    g_x-=g
                if event.key == pygame.K_RIGHT:
                    g_x+=g
            qu_it()
        screen.fill((0,0,0))
        ball_x+=sd_x
        ball_y-=sd_y
        if ball_x+17>=320:
            sd_x-=20
        if ball_x<=0:
            sd_x+=20
        if ball_y<=0:
            sd_y-=20
        if ball_y>=360:
            if ball_x>g_x and ball_x<=g_x+80:
                sd_y+=20
                fs+=1
        if ball_y>=380:
            fs=-2
        font = pygame.font.SysFont('arial',30)
        text_surface = font.render(f"error:{fs}",False,(225,0,0))
        screen.blit(text_surface,(20,70))
        font = pygame.font.SysFont('arial',40)
        text_surface = font.render(u"SB",False,(225,0,0))
        screen.blit(text_surface,(randint(0,320),randint(0,400)))
        pygame.draw.rect(screen,(225,225,225),(ball_x,ball_y,20,20),0)
        pygame.draw.rect(screen,(225,225,225),(g_x,g_y,80,20),0)
        pygame.display.flip()
        pygame.time.delay(5)
    #第七下半阶段
    if fs>=36 and fs<=40:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_LEFT:
                    g_x-=30
                if event.key == pygame.K_RIGHT:
                    g_x+=30
            qu_it()
        screen.fill((0,0,0))
        ball_x+=sd_x
        ball_y-=sd_y
        if ball_x+17>=320:
            sd_x-=20
        if ball_x<=0:
            sd_x+=20
        if ball_y<=0:
            sd_y-=20
        if ball_y>=360:
            if ball_x>g_x and ball_x<=g_x+80:
                sd_y+=20
                fs+=1
        if ball_y>=380:
            fs=-2
        font = pygame.font.SysFont('arial',30)
        text_surface = font.render(f"error:{fs}",False,(225,0,0))
        screen.blit(text_surface,(20,70))
        pygame.draw.rect(screen,(225,225,225),(ball_x,ball_y,20,20),0)
        pygame.draw.rect(screen,(225,225,225),(g_x,g_y,80,20),0)
        font = pygame.font.SysFont('arial',60)
        text_surface = font.render(u"You will die",False,(225,0,0))
        screen.blit(text_surface,(50,110))
        pygame.display.flip()
        pygame.time.delay(2.5)
    if  fs>=41:
        if BOSSgj == 1:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()
                    if event.key == pygame.K_LEFT:
                        g_x-=g
                    if event.key == pygame.K_RIGHT:
                        g_x+=g
                qu_it()
            screen.fill((0,0,0))
            ball_x+=sd_x
            ball_y-=sd_y
            if ball_x+17>=320:
                sd_x-=20
            if ball_x<=0:
                sd_x+=20
            if ball_y<=60:
                sd_y-=20
                BOSS-=1
                BOSSgj=randint(1,7)
            if ball_y>=360:
                if ball_x>g_x and ball_x<=g_x+80:
                    sd_y+=20
                    fs+=1
            if ball_y>=380:
                fs=-2
            BOSS_A()
            pygame.time.delay(10)
        if BOSSgj == 2:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()
                    if event.key == pygame.K_LEFT:
                        g_x-=g
                    if event.key == pygame.K_RIGHT:
                        g_x+=g
                qu_it()
            ball_x+=sd_x
            ball_y-=sd_y
            if ball_x+17>=320:
                sd_x-=20
            if ball_x<=0:
                sd_x+=20
            if ball_y<=60:
                sd_y-=20
                BOSS-=1
                BOSSgj=randint(1,7)
            if ball_y>=360:
                if ball_x>g_x and ball_x<=g_x+80:
                    sd_y+=20
                    fs+=1
            if ball_y>=380:
                fs=-2
            BOSS_A()
            pygame.time.delay(10)
        if BOSSgj == 3:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()
                    if event.key == pygame.K_LEFT:
                        g=-10
                    if event.key == pygame.K_RIGHT:
                        g=10
                qu_it()
            screen.fill((0,0,0))
            ball_x+=sd_x
            ball_y-=sd_y
            g_x+=g
            if ball_x+17>=320:
                sd_x-=20
            if ball_x<=0:
                sd_x+=20
            if ball_y<=60:
                sd_y-=20
                BOSS-=1
                BOSSgj=randint(1,7)
            if ball_y>=360:
                if ball_x>g_x and ball_x<=g_x+80:
                    sd_y+=20
                    fs+=1
            if ball_y>=380:
                fs=-2
            if g_x<=0:
                fs=-2
            if g_x+80>=320:
                fs=-2
            BOSS_A()
            pygame.draw.rect(screen,(221,99,20),(g_x,g_y,80,20),0)
            pygame.time.delay(10)
        if BOSSgj == 4:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()
                    if event.key == pygame.K_LEFT:
                        g_x-=g
                    if event.key == pygame.K_RIGHT:
                        g_x+=g
                qu_it()
            screen.fill((0,0,0))
            ball_x+=sd_x
            ball_y-=sd_y
            if ball_x+17>=320:
                sd_x-=20
            if ball_x<=0:
                sd_x+=20
            if ball_y<=60:
                sd_y-=20
                BOSS-=1
                BOSSgj=randint(1,7)
            if ball_y>=360:
                if ball_x>g_x and ball_x<=g_x+80:
                    sd_y+=20
                    fs+=1
            if ball_y>=380:
                fs=-2
            BOSS_A()
            pygame.time.delay(10)
        if BOSSgj == 5:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()
                    if event.key == pygame.K_LEFT:
                        g_x-=g
                    if event.key == pygame.K_RIGHT:
                        g_x+=g
                qu_it()
            ball_x+=sd_x
            ball_y-=sd_y
            if ball_x+17>=320:
                sd_x-=20
            if ball_x<=0:
                sd_x+=20
            if ball_y<=60:
                sd_y-=20
                BOSS-=1
                BOSSgj=randint(1,7)
            if ball_y>=360:
                if ball_x>g_x and ball_x<=g_x+80:
                    sd_y+=20
                    fs+=1
            if ball_y>=380:
                fs=-2
            BOSS_A()
            pygame.display.flip()
            pygame.time.delay(10)
        if BOSSgj == 6:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()
                    if event.key == pygame.K_LEFT:
                        g_x-=30
                    if event.key == pygame.K_RIGHT:
                        g_x+=30
                qu_it()
            screen.fill((0,0,0))
            ball_x+=30
            ball_y-=30
            if ball_x+17>=320:
                sd_x-=60
            if ball_x<=0:
                sd_x+=60
            if ball_y<=60:
                sd_y-=60
                BOSS-=1
                BOSSgj=randint(1,7)
            if ball_y>=360:
                if ball_x>g_x and ball_x<=g_x+80:
                    sd_y+=20
                    fs+=1
            if ball_y>=380:
                fs=-2
            BOSS_A()
            pygame.time.delay(10)
        if BOSSgj == 7:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()
                    if event.key == pygame.K_LEFT:
                        g_x-=g
                    if event.key == pygame.K_RIGHT:
                        g_x+=g
                qu_it()
            screen.fill((225,225,225))
            ball_x+=sd_x
            ball_y-=sd_y
            if ball_x+17>=320:
                sd_x-=20
            if ball_x<=0:
                sd_x+=20
            if ball_y<=60:
                sd_y-=20
                BOSS-=1
                BOSSgj=randint(1,7)
            if ball_y>=360:
                if ball_x>g_x and ball_x<=g_x+80:
                    sd_y+=20
                    fs+=1
            if ball_y>=380:
                fs=-2
            BOSS_A()
            pygame.time.delay(10)
    if BOSS ==0:
        screen.fill((225,0,0))
        font = pygame.font.SysFont('Simhei',40)
        text_surface = font.render("你赢了，但你真的赢了吗？",False,(0,0,0))
        screen.blit(text_surface,(20,20))
        pygame.time.delay(1000)
        exit()
