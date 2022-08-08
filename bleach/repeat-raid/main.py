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
            pyautogui.click(imageLocation)
            restorePosition()


    def restorePosition():
        pyautogui.moveTo(cur_mouse)


    while True:
        if keyboard.is_pressed('q'):
            print('Stop and Exit')
            break


        # Resolution Windows 1024x576 /w Lobby Screen
        findAndClick('host-start-raid.png', 0.8, 'Start Raid')
        findAndClick('result-screen.png', 0.8, 'Result Screen')
        findAndClick('retry.png', 0.8, 'Retry')
        findAndClick('create-raid.png', 0.8, 'Create Raid')

        time.sleep(0.05)
except KeyboardInterrupt:
    print('\n')
