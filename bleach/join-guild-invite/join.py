import pyautogui
import time
import keyboard


try:
    cur_mouse = pyautogui.position()
    inLobby = False

    def findAndClick(image, cond, lable):
        imageLocation = pyautogui.locateOnScreen(image, confidence=cond, grayscale=True)
        if imageLocation is not None:
            print('Click Image "'+lable+'" at '+str(imageLocation))
            global cur_mouse
            cur_mouse = pyautogui.position()
            pyautogui.click(imageLocation)
            restorePosition()
            return True
        return False


    def restorePosition():
        pyautogui.moveTo(cur_mouse)


    while True:
        if keyboard.is_pressed('q'):
            print('Stop and Exit')
            break


    

        # Resolution Windows 1024x576 /w Lobby Screen
        if inLobby is False:
            findAndClick('noti.png', 0.8, 'Click Guild Noti')
        else:
            findAndClick('5ticket.png', 0.9, 'Active x5')
            findAndClick('ready5x.png', 0.5, 'Ready')
        
        if findAndClick('join.png', 0.8, 'Join Room') is True:
            inLobby = True

        findAndClick('tap-screen.png', 0.8, 'TAP SCREEN')
        findAndClick('items-obtained.png', 0.8, 'Items Obtained')
        findAndClick('result-screen.png', 0.8, 'Result Screen')

        if findAndClick('coop.png', 0.9, 'Co-Op Quest Menu') is True:
            inLobby = False

        time.sleep(0.05)
except KeyboardInterrupt:
    print('\n')
