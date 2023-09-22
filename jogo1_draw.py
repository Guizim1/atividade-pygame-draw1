import pygame as pg 
from pygame.locals import * 
from random import randint 
  
tela = pg.display.set_mode((500,450)) 
  
pg.display.set_caption('>GRAFITANDO NO MURO!<') 
  
r_f,q_f,c_f = 0,0,0 
  
tela.fill((255,255,255)) 
  
while True: 
     for evento in pg.event.get(): 
         if evento.type == QUIT: 
             pg.quit() 
         if evento.type == MOUSEBUTTONDOWN: 
             x,y = evento.pos 
             if r_f: 
                 pg.draw.rect(tela,(randint(0,255),randint(0,255),randint(0,255)),(x,y,50,100)) 
             elif c_f: 
                 pg.draw.circle(tela,(randint(0,255),randint(0,255),randint(0,255)),(x,y),35) 
             elif q_f: 
                 pg.draw.rect(tela,(randint(0,255),randint(0,255),randint(0,255)),(x,y,50,50)) 
             else: 
                 pg.draw.rect(tela,(randint(0,255),randint(0,255),randint(0,255)),(x,y,50,70)) 
                 
                 
     teclas = pg.key.get_pressed() 
     if teclas[K_q]: 
         q_f = 1 
         c_f,r_f  = 0,0 
     if teclas[K_r]: 
         r_f = 1 
         c_f,r_q  = 0,0 
     if teclas[K_c]: 
         c_f = 1 
         q_f,r_f  = 0,0 
    
     pg.display.update()