from configparser import Interpolation
import cv2

img = cv2.imread("alarm.jpg")
new_img = cv2.resize(img, (64,64), interpolation = cv2.INTER_CUBIC)
cv2.imwrite("./icon.png", new_img)
