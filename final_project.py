import cv2
from cvzone.HandTrackingModule import HandDetector

#Setting up webcam for video capture
video_capture = cv2.VideoCapture(0)
video_capture.set(3,700)
video_capture.set (4, 500)
#Setting up hand detector
hand_detector = HandDetector(detectionCon=0.8)
while True:
    success,img = video_capture.read()
    img = hand_detector.findHands(img)
    lmList, _ = hand_detector.findPosition(img)
    cv2.imshow ("Image", img)
    cv2.waitKey(1)
