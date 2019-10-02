#coding:utf-8

import serial
import time
import pygame
import os
import random

# シリアルポートのデバイスファイル名に差し替える
PORT = '/dev/bell_button'
# ベル音源のディレクトリ名
BELL_DIR = 'bells/'

def getBellSound():
    bells = os.listdir(BELL_DIR)
    bell_filename = BELL_DIR + random.choice(bells)
    pygame.mixer.music.load(bell_filename)

pygame.mixer.init(44100, -16, 1, 256)
announce = pygame.mixer.Sound('sounds/announce.wav')
bell = getBellSound()
s = serial.Serial(PORT, dsrdtr=True)

s.dtr = True
last_state = False

while True:
    try:
        state = s.dsr
    except OSError:
        print('disconnected')
        exit()

    if last_state == False and state == True:
        pygame.mixer.music.play(loops=-1)
        last_state = True
    elif last_state == True and state == False:
        pygame.mixer.music.stop()
        last_state = False
        announce.play()
        getBellSound()
        
    time.sleep(0.01)
