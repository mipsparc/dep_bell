#coding:utf-8

import serial
import time
import pygame

# シリアルポートのデバイスファイル名に差し替える
port = '/dev/bell_button'

pygame.mixer.init(44100, -16, 1, 256)
bell = pygame.mixer.Sound('sounds/bell.wav')
announce = pygame.mixer.Sound('sounds/announce.wav')
s = serial.Serial(port, dsrdtr=True)

s.dtr = True
last_state = False

while True:
    try:
        state = s.dsr
    except OSError:
        print('disconnected')
        exit()

    if last_state == False and state == True:
        bell.play(loops=-1)
        last_state = True
    elif last_state == True and state == False:
        bell.stop()
        last_state = False
        announce.play()
    time.sleep(0.01)
