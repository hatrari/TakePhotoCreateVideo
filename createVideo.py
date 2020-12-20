import cv2
import numpy as np
import os

path = './times/'

photos = []
files = os.listdir(path)
for file in files:
    photos.append(cv2.imread(path + file))

size = (640, 480)

out = cv2.VideoWriter('out.mp4', 0x7634706d, 15, size)
 
for i in range(len(photos)):
    out.write(photos[i])

out.release()