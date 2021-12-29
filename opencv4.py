import cv2

src = cv2.imread("D:\ToyProject\opencv\Image\glass.jpg", cv2.IMREAD_COLOR)
dst = cv2.flip(src, 0)

#flip < 0 -> 상하좌우
#flip = 0 -> 상하
#flip > 0 -> 좌우

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
dv2.destroyAllWindows()