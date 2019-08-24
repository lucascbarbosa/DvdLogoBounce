import pygame as pg
try:
    pg.init()
except :
    print("Erro. Pygame não foi inicializado")

width = 1366
height = 768
#Define Important Variables
class Enviroment:
    def __init__(self,width, height,rect,image):
        self.width = width
        self.height = height
        self.rect = rect
        self.image = image
        self.black = (0,0,0)
        self.red = (255,0,0)
        self.green = (0,255,0)
        self.blue = (0,0,255)
        self.white = (255,255,255)
        self.clock = pg.time.Clock()
        self.screen_size = pg.FULLSCREEN
        self.screen = pg.display.set_mode((0,0),self.screen_size)
        pg.display.set_caption("Dvd Logo")

    def logo(self,pos_x,pos_y):
        imagerect = (pos_x,pos_y,1,1)
        env.screen.blit(self.image, imagerect)
        
    def bounce(self,pos_x,pos_y):
        bounce_x = bounce_y = False
        if pos_x < 0 or pos_x > self.width-self.rect[2]:
            bounce_x = True
        if pos_y < 0 or pos_y > self.height-self.rect[3]:
            bounce_y = True
        return (bounce_x,bounce_y)
    
    def hitCorner(self,pos_x,pos_y):
        hit = False
        if (pos_x,pos_y) == (0,0) or (pos_x,pos_y) == (0,self.height - self.rect[3]) or (pos_x,pos_y) == (self.width - self.rect[2]) or (pos_x,pos_y) == (self.height - self.rect[3], self.width - self.rect[2]):
            hit = True
        return hit
        myfont = pg.font.Font('Roboto-Regular.ttf', 30)
        text = myfont.render('It will take %i bounces to hit a corner!! %(bounces)', False, env.white)
        text_rect = text.get_rect(center=(self.width - self.rect[2]/2, self.rect[3]/2))
        env.screen.blit(text,text_rect)

myImage = pg.image.load('logo-dvd.jpg')
rect = myImage.get_rect()
env = Enviroment(width, height,rect,myImage)
pos_x,pos_y = (1,env.height-env.rect[3])
vel_x = 1
vel_y = -1

sair = False

myfont = pg.font.Font('Roboto-Regular.ttf', 30)
bounce_count = 0
while not sair:

    env.logo(pos_x,pos_y)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sair = True
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                sair = True
    if env.bounce(pos_x,pos_y)[0]:
        vel_x = -1*vel_x
        bounce_count += 1
    
    if env.bounce(pos_x,pos_y)[1]:
        vel_y = -1*vel_y
        bounce_count += 1

    string_count = 'Bounces = %i'%(bounce_count)
    textCount_size = myfont.size(string_count)
    text_bounceCount = myfont.render(string_count, False, env.red)
    textCount_rect = text_bounceCount.get_rect(center = (width - textCount_size[0]/2,textCount_size[1]/2))
    pos_x += vel_x
    pos_y += vel_y
    env.screen.blit(text_bounceCount,textCount_rect)
    pg.display.update()
    env.screen.fill(env.black)
    env.clock.tick(15000)
