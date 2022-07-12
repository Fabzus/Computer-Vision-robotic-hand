import cv2
from cvzone.HandTrackingModule import HandDetector
#from cvzone.SerialModule import SerialObject

cap=cv2.VideoCapture(0)
detector=HandDetector(detectionCon=.8, maxHands=1)
#mySerial=SerialObject("COM3", 9600, 1)


while True:
    succes, img=cap.read()
    hands, img = detector.findHands(img)
    cv2.imshow("hopa", img)
    cv2.waitKey(1)

    if hands:
        hand=hands[0]
        fingers=detector.fingersUp(hand)
        print(fingers)
        #mySerial.sendData(fingers)












#
# import cv2
# from cvzone.HandTrackingModule import HandDetector
#
# cap = cv2.VideoCapture(0)
# detector = HandDetector(detectionCon=0.8, maxHands=1)
# while True:
#     success, img = cap.read()
#     hand, img = detector.findHands(img)
#     if hand:
#         fingers=detector.fingersUp(s)
#         print(fingers)
#
#
#     # if hand:
#     #     fingers = detector.fingersUp(hand)
#     #     print(fingers)
#
#     # if hand:
#     #     # Hand -dict (lmList - bbox - center - type) DICTIONAR (nefolosit)
#     #     hand1 = hand[0]
#     #     lmList = hand1["lmList"]#o lista cu cele 21 de puncte
#     #     bbox = hand1["bbox"]#Bounding box info x y w h
#     #     centerPoint = hand1["center"]#centrul mainii pe axa cx cy
#     #     handType = hand1["type"]#ce mana este vizibila pe ecran
#     #     print(len(lmList))
#     #
#     #     # print(len(hand)) Folosit pentru a printa mainile
#
#     cv2.imshow("img", img)
#     cv2.waitKey(1)
