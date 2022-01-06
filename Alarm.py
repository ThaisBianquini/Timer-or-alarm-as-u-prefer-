import datetime
import pygame
import time
hour = int(input("tell me a Hour to set: "))
minute = int(input("Tell me a min to set: "))
h = datetime.datetime.now().hour
min = datetime.datetime.now().minute
seconds = datetime.datetime.now().second
ask = ""
print(f"Your alarm was set to {hour}:{minute}")
s1 = (h*120) + (min*60)
s2 = ((hour * 120) + (minute * 60))
sec = s2 - s1 - seconds
time.sleep(sec)
while ask != "S":
    pygame.mixer.init()
    pygame.init()
    pygame.mixer.music.load("wake.mp3")
    pygame.mixer.music.play()
    pygame.event.wait.__eq__(ask)
    ask = input("Did u wake [S/N]? ").upper()
    if ask == "S":
        break