import numpy as np
import cv2


def detect(imag):
    img = cv2.imread(imag)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blur = cv2.blur(gray, (5, 5))
    img_log = (np.log(blur + 1) / (np.log(1 + np.max(blur)))) * 255
    img_log = np.array(img_log, dtype=np.uint8)
    bilateral = cv2.bilateralFilter(img_log, 7,55,55)  
    edges = cv2.Canny(bilateral, 25,25) 
    kernel = np.ones((3, 3), np.uint8)
    closing = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)
    orb = cv2.ORB_create(nfeatures=3000)
    keypoints, descriptors = orb.detectAndCompute(closing, None)
    featuredImg = cv2.drawKeypoints(closing, keypoints, None)
    return featuredImg
    
