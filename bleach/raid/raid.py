import pyautogui
import time
import keyboard
import random

isFightScene = False

def randomSpecialMove():
    number = random.randint(3, 9)
    if isFightScene:
        if number > 6:
            pyautogui.press('r')
            print('Used Special Move')
            time.sleep(3)
            pyautogui.press('r')



try:
    cur_mouse = pyautogui.position()


    def findAndClick(image, cond, lable):
        # print('Searching for ' + lable)
        imageLocation = pyautogui.locateOnScreen(image, confidence=cond)
        if imageLocation is not None:
            print('Click Image "' + lable + '" at ' + str(imageLocation))
            global cur_mouse
            cur_mouse = pyautogui.position()
            pyautogui.click(imageLocation)
            restorePosition()

            if lable == 'Fight Auto':
                global isFightScene
                isFightScene = True

            if lable == 'SKip Friends':
                isFightScene = False

            # if lable == 'Room Closed':
            #     searchAgain()

        if lable == 'Select Room' and imageLocation is None:
            search = pyautogui.locateOnScreen('search-again.png', 0.8)
            if search is not None:
                pyautogui.click(search)
                time.sleep(1)
                pyautogui.click(pyautogui.locateOnScreen('okable.png', 0.7))
                print('no room')


    def searchAgain():
        findAndClick('search-again.png', 0.8, 'Search Again')
        time.sleep(1)
        findAndClick('okable.png', 0.7, 'Select Room')


    def restorePosition():
        pyautogui.moveTo(cur_mouse)


    while True:
        if keyboard.is_pressed('q'):
            print('Stop and Exit')
            break

        # Resolution Windows 1024x576
        # findAndClick('main-btn.png', 0.85, 'Jidanbo Raid')
        # findAndClick('hard-mode.png', 0.85, 'Select Hard')
        # findAndClick('join.png', 0.8, 'Join Rooms')
        # findAndClick('okable.png', 0.7, 'Select Room')
        # findAndClick('ready.png', 0.7, 'Ready')
        # findAndClick('fight-auto.png', 0.9, 'Fight Auto')
        # findAndClick('friends.png', 0.6, 'SKip Friends')
        # findAndClick('retry.png', 0.8, 'Retry')
        # findAndClick('room-closed.png', 0.8, 'Room Closed')
        # findAndClick('revive.png', 0.8, 'Revive')
        # findAndClick('red-retry.png', 0.85, 'Red Retry')

        findAndClick('coop-title.png', 0.85, 'Coop Title')
        time.sleep(1)
        findAndClick('select-quest.png', 0.85, 'Select Quest')

        # findAndClick('hard-mode.png', 0.85, 'Select Hard')
        findAndClick('join-coop.png', 0.8, 'Join Rooms')
        findAndClick('okable.png', 0.7, 'Select Room')
        time.sleep(5)
        findAndClick('active5x.png', 0.9, 'Active 5X')
        findAndClick('ready5x.png', 0.85, 'Active 5X')
        # findAndClick('ready.png', 0.7, 'Ready')
        findAndClick('fight-autov2.png', 0.85, 'Fight Auto')
        findAndClick('friends.png', 0.6, 'SKip Friends')
        findAndClick('tap-screen.png', 0.6, 'Tap Screen')
        findAndClick('result-screen.png', 0.8, 'Result Screen')
        findAndClick('retry-sm.png', 0.8, 'Retry')
        findAndClick('room-closed.png', 0.8, 'Room Closed')
        findAndClick('revive.png', 0.8, 'Revive')
        findAndClick('red-retry.png', 0.85, 'Red Retry')

        # randomSpecialMove()

        time.sleep(0.12)
except KeyboardInterrupt:
    print('\n')
