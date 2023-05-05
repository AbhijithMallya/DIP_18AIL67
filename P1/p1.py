#4SF20CI002 - ABHIJITH MALLYA
import cv2
import numpy as np

image = cv2.imread("image.jpg")
image = cv2.resize(image, (640, 640))
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)
topLeft=cv2.copyMakeBorder(image[0:cY, 0:cX], 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=[255, 255, 0])
topRight=cv2.copyMakeBorder(image[0:cY, cX:w], 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=[255, 255, 0])
bottomLeft=cv2.copyMakeBorder(image[cY:h, 0:cX], 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=[255, 255, 0])
bottomRight=cv2.copyMakeBorder(image[cY:h, cX:w], 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=[255, 255, 0])

Hori1 = np.concatenate((topLeft, topRight), axis=1)
Hori2 = np.concatenate((bottomLeft, bottomRight), axis=1)
Vert=np.concatenate((Hori1, Hori2), axis=0)
cv2.imshow("STICHED IMAGE",Vert)

cv2.imshow("original image",image)
cv2.waitKey(0)
cv.waitKey(0)
cv.destroyAllWindows("q")
