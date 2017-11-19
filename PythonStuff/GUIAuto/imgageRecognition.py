#! python3

import pyautogui

location = pyautogui.locateOnScreen('files/chrome.png')
if location is not None:
    x, y, w, h = pyautogui.locateOnScreen('files/chrome.png')
    print(location)
    print(x, y, w, h)

    xy = pyautogui.center(location)
    pyautogui.rightClick(xy)
else:
    print('Image not found')
