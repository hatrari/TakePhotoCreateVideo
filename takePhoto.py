import cv2 as cv
import time

camera = cv.VideoCapture(0)

while(True):
 ret, image = camera.read()
 ts = time.time()
 name = int(ts)
 cv.imwrite('photos/'+str(name)+'.jpg', image)
 time.sleep(1)
 print(name)

camera.release()
cv.destroyAllWindows()