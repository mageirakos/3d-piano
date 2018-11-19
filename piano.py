# -*- coding: cp1253 -*-
from visual import *
import pygame

pygame.init()

def rotatew(x):
    x=int(x)
    '''rotate white keys '''
    for i in range(6):
        wkey[x].rotate(angle=-pi/100, axis=(-1,0,0))
        rate(25)
    for i in range(6):
        wkey[x].rotate(angle=pi/100, axis=(-1,0,0))
        rate(25)
    return

def rotateb(x):
    x=int(x)
    '''rotate black keys '''
    for i in range(6):
        bkey[x+1].rotate(angle=-pi/100, axis=(-1,0,0))
        rate(25)
    for i in range(6):
        bkey[x+1].rotate(angle=pi/100, axis=(-1,0,0))
        rate(25)
    return

def Songs(choice):
    '''��������� ��� ������ ��������� ��� �����  '''
    if choice==1: #������� ��� ����������(� ����� ��� �������� �� �������� ������������� ���� ���� ������ ��� ��������� ���� �� ����������� ����� ��������� ��������������� �������� ����)
        Song1=[["SOUNDS\G3.wav",31],["SOUNDS\C4.wav",28],["SOUNDS\C4.wav",28],["SOUNDS\D4.wav",27],["SOUNDS\C4.wav",28],["SOUNDS\B3.wav",29],["SOUNDS\A3.wav",30],
               ["SOUNDS\A3.wav",30],["SOUNDS\A3.wav",30],["SOUNDS\D4.wav",27],["SOUNDS\D4.wav",27],["SOUNDS\E4.wav",26],["SOUNDS\D4.wav",27],["SOUNDS\C4.wav",28],
               ["SOUNDS\B3.wav",29],["SOUNDS\G3.wav",31],["SOUNDS\G3.wav",31],["SOUNDS\E4.wav",26],["SOUNDS\E4.wav",26],["SOUNDS\F4.wav",25],["SOUNDS\E4.wav",26],
               ["SOUNDS\D4.wav",27],["SOUNDS\C4.wav",28],["SOUNDS\A3.wav",30],["SOUNDS\G3.wav",31],["SOUNDS\G3.wav",31],["SOUNDS\A3.wav",30],["SOUNDS\D4.wav",27],
               ["SOUNDS\B3.wav",29],["SOUNDS\C4.wav",28]]    
        for i in range(len(Song1)):
            sound = pygame.mixer.Sound(Song1[i][0])
            sound.play()            
            rotatew(Song1[i][1])
            if scene.kb.keys:                          
                key = scene.kb.getkey()
                if key == "b":
                    pygame.mixer.fadeout(1000)#������ ��� ���
                    break #���� �� ������� �� b �� ���������� �� ��������

#------------------------------------��� ������������� � 3D ���������� ��� ������������----------------------------------# 
mainvector = vector(0,0,0)#vector(27,3,2) #����� �������� ��� ��������� ��� �� ���������� �� ����� ���� ���� 
##floor = box(pos=top-vector(0,3,0),size=(.2,24,24), axis=(0,1,0), color=color.orange, material=materials.wood)
#��� ��������� �� �����
pianobox = box(pos=mainvector-vector(0,0,0), width=1.5, height = 6, length=8, color=color.gray(0.2), meterial=materials.wood) #length/heght=1.3 
keybox = box(pos=pianobox.pos-vector(0,-1,-1.2), width=1.2, height=0.4, length=8, color=color.gray(0.2))
topbox = box(pos=pianobox.pos+vector(0,3,0), width=1.6, height=0.1, length=8.2, color=color.gray(0.2))
aboxy = box(pos=pianobox.pos-vector(0,2.7,-0.8), width=0.4, height=0.3, length=6, color=color.gray(0.2))
bboxy = box(pos=pianobox.pos-vector(0,-1.3,-0.8), width=0.1, height=0.6, length=8, color=color.gray(0.2))
boxy1 = box(pos=pianobox.pos-vector(3.95,-1.3,-1.2), width=1.2, height=0.3, length=0.1, color=color.gray(0.2))
boxy2 = box(pos=pianobox.pos-vector(-3.95,-1.3,-1.2), width=1.2, height=0.3, length=0.1, color=color.gray(0.2))
legy1 = cylinder(pos=pianobox.pos-vector(3.2,-1,-1.2), axis=(0,-4,0), radius=0.2, color=color.gray(0.2))
legy2 = cylinder(pos=pianobox.pos-vector(-3.2,-1,-1.2), axis=(0,-4,0), radius=0.2, color=color.gray(0.2))
legy1box = box(pos=pianobox.pos-vector(3.2,2.8,-1), width=1.2, height=0.2, length=0.5, color=color.gray(0.2))
legy2box = box(pos=pianobox.pos-vector(-3.2,2.8,-1), width=1.2, height=0.2, length=0.5, color=color.gray(0.2))
pedal1 = box(pos=pianobox.pos-vector(-0.5,2.7,-1), width=1, height=0.1, length=0.2, color=(1,0.7,0.2))
pedal2 = box(pos=pianobox.pos-vector(0.5,2.7,-1), width=1, height=0.1, length=0.2, color=(1,0.7,0.2))
pedal3 = box(pos=pianobox.pos-vector(0,2.7,-1), width=1, height=0.1, length=0.2, color=(1,0.7,0.2))

#��� ��������� �� ������
stool = box(pos=pianobox.pos-vector(0,0.5,-4), width=1.3,height=0.5, length=4, color=color.gray(0.2))
sleg1 = box(pos=stool.pos-vector(1.8,1.3,0.3), width=0.2,height=2.5, length=0.2, color=color.gray(0.2))
sleg2 = box(pos=stool.pos-vector(-1.8,1.3,0.3), width=0.2,height=2.5, length=0.2, color=color.gray(0.2))
sleg3 = box(pos=stool.pos-vector(1.8,1.3,-0.3), width=0.2,height=2.5, length=0.2, color=color.gray(0.2))
sleg4 = box(pos=stool.pos-vector(-1.8,1.3,-0.3), width=0.2,height=2.5, length=0.2, color=color.gray(0.2))
pillowbox= box(pos=pianobox.pos-vector(0,0.2,-4), width=1.2,height=0.01, length=3, color=color.gray(0.1))

#��� ��������� �� WHITE KEYS
wkey = dict() #��� �� ����� �� ����� ���� �������� ��� key ��� ��� value �� �������������� ��� (�� ����������� ���� ��� �� bkey[] ���� ����������� rotatew ��� rotateb ����������)
for i in range(0,52):
    wkey[i]= box(pos=pianobox.pos-vector(-3.85+0.15*i,-1.3,-1.5), width=0.7, height=0.1, length=0.14) 
        
#��� ��������� �� BLACK KEYS
#� �������� ������ ��� �������� ����� 0.15 ��� ��� �������� 0.3
bkey = dict()
a=[-3.65, -3.50, -3.35, -3.05, -2.90, -2.6, -2.45, -2.30, -2.00, -1.85, -1.55, -1.40, -1.25, -0.95,
   -0.80, -0.50, -0.35, -0.20,  0.10,  0.25, 0.55,  0.70,  0.85,  1.15,  1.30,  1.60,  1.75,  1.90,
    2.20,  2.35,  2.65,  2.8,   2.95,  3.25, 3.4,   3.65] # ���� � ����� ����� ��� ������ ��� �������� 
for i in range(0, len(a)):
    bkey[i] = box(pos=pianobox.pos-vector(a[i],-1.38,-1.33), width=0.4, height=0.1, length=0.13, color=color.gray(0.1))

######################################################################################################################
#Dictionary ��� white keys ��� ����� ��� �� ������� ��� ��� ��� ��� ������ ��� ��� �����������
dic = { "q":["SOUNDS\C4.wav",28], "w":["SOUNDS\D4.wav",27], "e":["SOUNDS\E4.wav",26], "r":["SOUNDS\F4.wav",25], "t":["SOUNDS\G4.wav",24], "y":["SOUNDS\A4.wav",23],
        "u":["SOUNDS\B4.wav",22], "j":["SOUNDS\B3.wav",29], "h":["SOUNDS\A3.wav",30], "g":["SOUNDS\G3.wav",31], "f":["SOUNDS\F3.wav",32], "d":["SOUNDS\E3.wav",33],
        "s":["SOUNDS\D3.wav",34], "a":["SOUNDS\C3.wav",35], "i":["SOUNDS\C5.wav",21] }
#Dictionary ��� black keys ��� ����� ��� �� ������� ��� ��� ��� ��� ������ ��� ��� �����������
dicb = { "1":["SOUNDS\Db4.wav",18], "2":["SOUNDS\Eb4.wav",17], "3":["SOUNDS\Gb4.wav",16],"4":["SOUNDS\Ab4.wav",15],"5":["SOUNDS\Bb4.wav",14] }


while True: #(0.0 <= newforward.x <=0.5)  :

    if scene.kb.keys:                          #�� ����� ��� ����� ����� �� ������ �� ������� ���� ��� �������������
        key = scene.kb.getkey()
        if key in dic:
            sound = pygame.mixer.Sound (dic[key][0])
            sound.play()
            pygame.mixer.fadeout(1000)
            rotatew(dic[key][1])
        elif key in dicb:
            sound = pygame.mixer.Sound (dicb[key][0])
            sound.play()
            pygame.mixer.fadeout(1000)
            rotateb(dicb[key][1])
            
   #��� ����� �� ���� ��������� �� ������� ��� �� ���� ��� ��������� Songs         
        if key == "z":            
            Songs(1) #���� �� ��������
    rate(25)
        

