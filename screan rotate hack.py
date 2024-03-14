import rotatescreen
import time
import pyautogui

pyautogui.hotkey("win","m")
screen=rotatescreen.get_primary_display()
while(10):
    time.sleep(0.05)
    screen.rotate_to(4*90%360)
    time.sleep(0.05)
    screen.rotate_to(3*90%360)
    time.sleep(0.05)
    screen.rotate_to(2*90%360)
    time.sleep(0.05)
    screen.rotate_to(1*90%360)
    