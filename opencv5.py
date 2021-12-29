import cv2
import numpy as np

#회전

src = cv2.imread(r"D:\ToyProject\opencv\Image\ara.jpg", cv2.IMREAD_COLOR)

print(src.shape)

height, width, channel = src.shape
matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)
dst = cv2.warpAffine(src, matrix, (width, height))

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()