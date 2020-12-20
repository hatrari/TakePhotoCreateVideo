import os
from datetime import datetime
import cv2

font = cv2.FONT_HERSHEY_SIMPLEX
org = (150, 50) 
fontScale = 1
color = (255, 0, 0) 
thickness = 2

path = './photos/'
files = os.listdir(path)
for file in files:
  timestamp = int(file.split('.')[0])
  date = datetime.fromtimestamp(timestamp)
  photo = cv2.imread(path + file)
  photo = cv2.putText(photo, str(date), org, font, fontScale, color, thickness, cv2.LINE_AA)
  cv2.imwrite('./times/' + file, photo)