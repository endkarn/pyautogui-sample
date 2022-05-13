import datetime

import pyautogui
import time
import keyboard

try:
    cur_mouse = pyautogui.position()


    def findAndClick(image, cond, lable):
        imageLocation = pyautogui.locateOnScreen(image, confidence=cond, grayscale=True)
        if imageLocation is not None:
            print('Click Image "'+lable+'" at '+str(imageLocation))
            global cur_mouse
            cur_mouse = pyautogui.position()
            clickPos = pyautogui.center(imageLocation)
            # pydirectinput.click(clickPos.x, clickPos.y)
            pyautogui.moveTo(clickPos)
            pyautogui.mouseDown()
            pyautogui.mouseUp()

            # pyautogui.leftClick(imageLocation)
            restorePosition()
            return True
        return False


    def restorePosition():
        pyautogui.moveTo(cur_mouse)


    counterFish = 0
    while True:
        if keyboard.is_pressed('q'):
            print('Stop and Exit')
            break

        # Resolution Windows 1024x576
        findAndClick('ready.png', 0.8, 'Ready')


        time.sleep(0.05)
except KeyboardInterrupt:
    print('\n')
