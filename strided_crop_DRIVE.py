import pytesseract
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('img.jpg')

img = cv2.resize(img, (600, 360))
print(pytesseract.image_to_string(img))