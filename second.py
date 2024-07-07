import pyautogui
import time
import os

def auto_click_on_images(image_paths, delay=0.1):
  while True:
    clicked = False
    for image_path in image_paths:
      full_image_path = os.path.join('images', image_path)
      image_loc = pyautogui.locateOnScreen(full_image_path, confidence=0.8)

      if image_loc:
        center_loc = pyautogui.center(image_loc)
        x, y = center_loc

        pyautogui.click(x, y)

        clicked = True
        break

    if not clicked:
      print("----")
      time.sleep(delay)

if __name__ == "__main__":
    
  image1 = 'img1.png'
  image2 = 'img2.png'
  image3 = 'img3.png'

  images = [image1, image2, image3]
    
  auto_click_on_images(images)
