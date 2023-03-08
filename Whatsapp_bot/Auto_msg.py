import pyautogui

import time

time.sleep(20)
count=0

while count<=1000:
    pyautogui.typewrite("Type your msg here !!!! ")
    pyautogui.press("enter")
    count=count+1
