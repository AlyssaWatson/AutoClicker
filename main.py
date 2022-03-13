from pynput import mouse
import keyboard
import time

# mouse needed for click
cursor = mouse.Controller()
# variable to toggle whether mouse should be clicking or not
clicking = False

while True:
    # start(s) clicking
    if keyboard.is_pressed('ctrl + s'):
        clicking = True

    # quit(q) clicking
    if keyboard.is_pressed('ctrl + q'):
        clicking = False

    # escape(esc) program
    if keyboard.is_pressed('esc'):
        break

    # script to click mouse
    if clicking:
        cursor.click(mouse.Button.left, 1)
        time.sleep(.01)
