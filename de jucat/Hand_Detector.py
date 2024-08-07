import cv2
from cvzone import HandTrackingModule


cap = cv2.VideoCapture(0)
detector = HandTrackingModule.HandDetector()

while True:
    succes, img = cap.read()
    detector.findHands(img)
    cv2.imshow('image', img)
    cv2.waitKey(1)
