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

        # locationEN = pyautogui.locateOnScreen('skip.png', confidence=0.7, grayscale=True)
        # locationTH = pyautogui.locateOnScreen('th.png', confidence=0.9, grayscale=True)
        # cleared = pyautogui.locateOnScreen('clear.png', confidence=0.5, grayscale=True)
        # nextTH = pyautogui.locateOnScreen('next_quest_en.png', confidence=0.8, grayscale=True)
        # nextEN = pyautogui.locateOnScreen('next_quest_th.png', confidence=0.8, grayscale=True)
        # ticket = pyautogui.locateOnScreen('ticket.png', confidence=0.7, grayscale=True)
        # prepare = pyautogui.locateOnScreen('prepare.png', confidence=0.7, grayscale=True)

        # findAndClick(locationEN, 'skipEN')
        # findAndClick(locationTH, 'skipTH')
        # findAndClick(cleared, 'clear')
        # findAndClick(nextTH, 'nextTH')
        # findAndClick(nextEN, 'nextEN')
        # findAndClick(ticket, 'ticket')
        # findAndClick(prepare, 'prepare')

        # Resolution Windows 1024x576
        findAndClick('prepare-for-quest.png', 0.8, 'Prepare for Quest')
        findAndClick('ticket.png', 0.7, 'Start with Ticket')
        findAndClick('skip.png', 0.6, 'Skip')
        findAndClick('clear.png', 0.5, 'Quest Cleared')
        findAndClick('next.png', 0.85, 'Next Quest')
        findAndClick('close.png', 0.8, 'Close Reward')
        findAndClick('ok.png', 0.8, 'Added Friend')

        time.sleep(0.05)
except KeyboardInterrupt:
    print('\n')
