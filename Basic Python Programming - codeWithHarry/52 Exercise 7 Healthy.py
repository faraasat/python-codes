from time import time
from pygame import mixer
from datetime import datetime


def musicloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersec = 5
    exesec = 10
    eyesec = 15

    while True:
        if time() - init_water > watersec:
            print("Water drinking time. Enter 'drank' to stop")
            musicloop('water.mp3', 'drank')
            log_now("Drank water at")

        if time() - init_eyes > eyesec:
            print("Eye exercise time. Enter 'doneeye' to stop")
            musicloop('water.mp3', 'doneeye')
            log_now("Eye freshed at")

        if time() - init_exercise > exesec:
            print("Exercise time. Enter 'doneex' to stop")
            musicloop('water.mp3', 'doneex')
            log_now("Done Exercise at")
