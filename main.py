import cv2
import numpy as np
import pyautogui
import keyboard

image1 = 'img1.png'
image2 = 'img2.png'
image3 = 'img3.png'

images = [image1, image2, image3]

def find_image_on_screen(image_path, threshold=0.9):
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    template = cv2.imread(image_path, cv2.IMREAD_COLOR)

    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val >= threshold:
        return max_loc[0] + template.shape[1] // 2, max_loc[1] + template.shape[0] // 2
    return None

while True:
    if keyboard.is_pressed('c'):
        print("프로그램을 종료합니다.")
        break

    for image in images:
        location = find_image_on_screen(image, threshold=0.9)
        if location is not None:
            pyautogui.click(location)
            pyautogui.moveTo(0, 0)
            break

    pyautogui.sleep(1)
