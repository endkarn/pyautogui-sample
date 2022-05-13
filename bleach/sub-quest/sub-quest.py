import pyautogui
import time
import keyboard

try:
    cur_mouse = pyautogui.position()


    def findAndClick(image, cond, label):
        imageLocation = pyautogui.locateOnScreen(image, confidence=cond)
        if imageLocation is not None:
            print('Click Image "' + label + '" at ' + str(imageLocation))
            global cur_mouse
            cur_mouse = pyautogui.position()
            pyautogui.click(imageLocation)
            restorePosition()


    def restorePosition():
        pyautogui.moveTo(cur_mouse)


    def clickNextInFooter():
        imageLocation = pyautogui.locateOnScreen('finished-footer.png', confidence=0.7)
        if imageLocation is not None:
            clickPoint = pyautogui.center(imageLocation)
            pyautogui.click((clickPoint.x + 300), clickPoint.y)
            restorePosition()




    while True:
        if keyboard.is_pressed('end'):
            print('Stop and Exit')
            break

        # Resolution Windows 1024x576
        findAndClick('unclear-3stars.png', 0.6, 'Unclear Quest')
        findAndClick('prepare-for-quest.png', 0.8, 'Prepare for Quest')
        findAndClick('ticket.png', 0.7, 'Start with Ticket')
        findAndClick('skip.png', 0.65, 'Skip')
        findAndClick('clear.png', 0.5, 'Quest Cleared')
        # findAndClick('next.png', 0.75, 'Next Quest')
        clickNextInFooter()
        findAndClick('close.png', 0.8, 'Close Reward')

        time.sleep(0.5)

except KeyboardInterrupt:
    print('\n')
