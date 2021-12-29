#Blur

import cv2

src = cv2.imread(r"D:\ToyProject\opencv\Image\cr.jpg")
dst = cv2.blur(src, (9, 9), anchor=(-1, -1), borderType=cv2.BORDER_DEFAULT)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()