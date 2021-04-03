import pyautogui
import keyboard
from PIL import ImageGrab
from time import sleep

# You may use the following code to find the position of the mouse cursor on the screen.
# Doing so you can adjust the code to match your screen specifications.
# Comment the rest of the code to run this part
# while True:
#     sleep(1)
#     print(pyautogui.position())


# 1920x1080
pyautogui.PAUSE = 0.05
Y = 29  # Y pixel position - it is the "line" on the screen you are looking for a specific pixel
GREEN_BUTTON_X = 160
RED_BUTTON_X = 250
YELLOW_BUTTON_X = 350
BLUE_BUTTON_X = 440
ORANGE_BUTTON_X = 540
THRESHOLD = 255  # Sometimes it can be useful to lower the threshold to have more accuracy finding the buttons


def play_guitarflash():
    print(1)
    sleep(1)
    print(2)
    sleep(1)
    print(3)
    sleep(1)
    print('Start!')

    key_bidings = {'a': GREEN_BUTTON_X, 's': RED_BUTTON_X, 'j': YELLOW_BUTTON_X,
                   'k': BLUE_BUTTON_X, 'l': ORANGE_BUTTON_X}

    while not keyboard.is_pressed('q'):  # Hold 'q' to stop the code
        screen = ImageGrab.grab(bbox=(600, 750, 1250, 900))  # Takes a screen shot of the region in bbox
        for key in key_bidings:
            color = screen.getpixel((key_bidings[key], Y))
            if color >= (THRESHOLD, THRESHOLD, THRESHOLD):
                pyautogui.press(key)


play_guitarflash()
