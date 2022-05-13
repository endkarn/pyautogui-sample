import pyautogui
import time
import keyboard


def collect_all():
    findAndClick('collect-all.png', 0.8, 'Collect Reward')
    time.sleep(1)
    findAndClick('ok.png', 0.9, 'OK')
    time.sleep(2)
    findAndClick('close.png', 0.8, 'Close Reward')
    time.sleep(2)


def repeat_event():
    findAndClick('ticket.png', 0.7, 'Start with Ticket')
    findAndClick('purchase-tickets.png', 0.7, '1 Orb = 5 Tickets')
    findAndClick('tap-screen.png', 0.8, 'Tap Screen')
    findAndClick('result-screen.png', 0.8, 'Result Screen')
    findAndClick('tap-screen.png', 0.8, 'Tap Screen')
    findAndClick('close.png', 0.8, 'Close Reward')
    findAndClick('retry.png', 0.7, 'Retry Quest')


try:
    cur_mouse = pyautogui.position()
    c_round = 0


    def findAndClick(image, cond, lable):
        imageLocation = pyautogui.locateCenterOnScreen(image, confidence=cond, grayscale=True)
        if imageLocation is not None:
            print('Click Image "' + lable + '" at ' + str(imageLocation))
            global cur_mouse
            cur_mouse = pyautogui.position()
            pyautogui.click(imageLocation)
            restorePosition()

            if lable == 'Result Screen':
                global c_round
                c_round = c_round + 1
                print('Cur Round ' + str(c_round))



    def restorePosition():
        pyautogui.moveTo(cur_mouse)


    while True:
        if keyboard.is_pressed('end'):
            print('Stop and Exit')
            break

        if c_round > 1000:
            print('Completed Round' + c_round)
            break

        # repeat_event()
        # findAndClick('retry-chronicle.png', 0.7, 'Start with Ticket')
        collect_all()

        time.sleep(0.3)
except KeyboardInterrupt:
    print('\n')
