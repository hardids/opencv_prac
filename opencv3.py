import cv2

image = cv2.imread("D:\ToyProject\opencv\Image\lunar.jpg", cv2.IMREAD_ANYCOLOR)
cv2.imshow("Moon", image)
cv2.waitKey()
cv2.destroyAllWindows()