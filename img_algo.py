import cv2
import imutils

def convert_to_grayscale(image_path):
    img=cv2.imread(image_path)
    img=imutils.resize(img,height=250)
    gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    return gray_img


    