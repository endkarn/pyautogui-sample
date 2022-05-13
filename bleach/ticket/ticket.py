import pyautogui
import time
import keyboard


def summon():
    findAndClick('ok.png', 0.9, 'OK')
    findAndClick('skip.png', 0.7, 'SKIP')
    time.sleep(0.5)
    findAndClick('summonx10.png', 0.7, 'Summon x 10')


def bulk_sell():
    findAndClick('sellchar.png', 0.7, 'sellchar')
    findAndClick('multi-select.png', 0.7, 'multiselect')
    findAndClick('select50.png', 0.8, 'select50')
    findAndClick('sell.png', 0.7, 'sell')
    findAndClick('ok.png', 0.88, 'ok')
    time.sleep(1)
    findAndClick('close.png', 0.8, 'close')


try:
    cur_mouse = pyautogui.position()
    c_round = 0
    sell_mode = True


    def findAndClick(image, cond, lable):
        imageLocation = pyautogui.locateOnScreen(image, confidence=cond, grayscale=True)
        if imageLocation is not None:
            print('Click Image "' + lable + '" at ' + str(imageLocation))
            global cur_mouse
            cur_mouse = pyautogui.position()
            pyautogui.click(imageLocation)
            restorePosition()


    def restorePosition():
        pyautogui.moveTo(cur_mouse)


    while True:
        # if keyboard.is_pressed('end'):
        #     print('Stop and Exit')
        #     break
        #
        # if c_round > 300:
        #     print('Completed Round' + c_round)
        #     break

        summon()
        # bulk_sell()

        # if pyautogui.locateCenterOnScreen("chars-full.png") is not None:
        #     findAndClick('chars-list.png', 0.85, 'chars-list')
        #     sell_mode = True
        #
        # if sell_mode is True:
        #     bulk_sell()

        time.sleep(0.25)
except KeyboardInterrupt:
    print('\n')
