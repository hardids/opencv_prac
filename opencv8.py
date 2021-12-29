#Cropping

import cv2

src = cv2.imread(r"D:\ToyProject\opencv\Image\apple.jpg", cv2.IMREAD_COLOR)

#ROI (Region of Interest) -> Selecting
# dst = src[100:600, 200:700].copy()

dst = src.copy()
roi = src[100:600, 200:700]
dst[0:500, 0:500] = roi

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()