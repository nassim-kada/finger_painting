import cv2
import numpy as np
import os
import HandTrackingModule as htm

brushThickness = 25
eraserThickness = 100
eraserColor = (0, 0, 0)
drawColor = (255, 0, 0)

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = htm.handDetector(detectionCon=0.65, maxHands=1)
xp, yp = 0, 0
drawing = False

imgCanvas = np.zeros((720, 1280, 3), np.uint8)

button_width = 150
button_height = 50
button1_pos = (10, 10)
button2_pos = (170, 10)
button3_pos = (330, 10)

button_color = (90, 0, 0)
button_text_color = (255, 255, 255)

mode = None

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        fingers = detector.fingersUp()

        if mode == "draw" and fingers[1] == 1 and fingers[2:] == [0, 0, 0]:
            if not drawing:
                drawing = True
                xp, yp = x1, y1
            else:
                cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)
                xp, yp = x1, y1
        elif mode == "draw" and fingers[1] == 0:
            drawing = False

        elif mode == "erase" and fingers == [0, 0, 0, 0, 0]:
            cv2.circle(imgCanvas, (x1, y1), eraserThickness, eraserColor, cv2.FILLED)
            xp, yp = x1, y1

        x, y = lmList[8][1:]
        if button1_pos[0] < x < button1_pos[0] + button_width and button1_pos[1] < y < button1_pos[1] + button_height:
            imgCanvas = np.zeros((720, 1280, 3), np.uint8)
        elif button2_pos[0] < x < button2_pos[0] + button_width and button2_pos[1] < y < button2_pos[1] + button_height:
            mode = "draw"
        elif button3_pos[0] < x < button3_pos[0] + button_width and button3_pos[1] < y < button3_pos[1] + button_height:
            mode = "erase"

    cv2.rectangle(img, button1_pos, (button1_pos[0] + button_width, button1_pos[1] + button_height), button_color, -1)
    cv2.putText(img, "Clear All", (button1_pos[0] + 20, button1_pos[1] + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, button_text_color, 2)

    cv2.rectangle(img, button2_pos, (button2_pos[0] + button_width, button2_pos[1] + button_height), button_color, -1)
    cv2.putText(img, "Draw Mode", (button2_pos[0] + 20, button2_pos[1] + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, button_text_color, 2)

    cv2.rectangle(img, button3_pos, (button3_pos[0] + button_width, button3_pos[1] + button_height), button_color, -1)
    cv2.putText(img, "Erase Mode", (button3_pos[0] + 10, button3_pos[1] + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, button_text_color, 2)

    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, imgInv)
    img = cv2.bitwise_or(img, imgCanvas)

    cv2.imshow("Virtual Drawing", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()