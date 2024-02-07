import cv2

#Setting up webcam for video capture
capture = cv2.VideoCapture(0)
capture.set(3,700)
capture.set (4, 500)
while True:
    success, img = capture.read()
    cv2.imshow ("Image", img)
    cv2.waitKey(1)
