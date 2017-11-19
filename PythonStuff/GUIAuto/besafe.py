#! python3
import pyautogui

print('''
if the program runs out of your control
on windows: ctrl-alt-del
on OS X: cmd-shift-option-q 
if FAILSAFE is true, you can stop the program
by moving the mouse to the (top-left) 
as far up and as left as you can
''')

# every fun() call will wait for a second
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

# pyautogui use x, y coordinate
# follow javascript coordinate approach

# screen size
width, height = pyautogui.size()

# moving mouse
for i in range(1):
    pyautogui.moveTo(100, 100, duration=0.25)
    pyautogui.moveTo(200, 100, duration=0.25)
    pyautogui.moveTo(200, 200, duration=0.25)
    pyautogui.moveTo(100, 200, duration=0.25)
# get mouse position
print(pyautogui.position())

pyautogui.click(10, 5)
pyautogui.doubleClick(10, 5)
pyautogui.rightClick(10, 50)

# drag
pyautogui.dragTo(100, 300)
pyautogui.scroll(500)

# screenshot
im = pyautogui.screenshot()
im.save('files/shot.png')
