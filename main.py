import pyautogui
import time
import keyboard

image1 = 'img1.png'
image2 = 'img2.png'
image3 = 'img3.png'

images = [image1, image2, image3]

while True:
    if keyboard.is_pressed('c'):
      break
    for image in images:
        location = pyautogui.locateCenterOnScreen(image)
        if location is not None:
            pyautogui.click(location)
            pyautogui.moveTo(0, 0)
            break
    time.sleep(1)
