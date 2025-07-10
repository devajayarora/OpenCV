import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))  # Get the width of the frame
    height = int(cap.get(4))  # Get the height of the frame

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Define color ranges for detection
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])
    # lower_green = np.array([40, 100, 100])
    # upper_green = np.array([80, 255, 255])
    # lower_red = np.array([0, 100, 100])
    # upper_red = np.array([10, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # mask_green = cv2.inRange(hsv, lower_green, upper_green)
    # mask_red = cv2.inRange(hsv, lower_red, upper_red)

    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('Original Frame', result)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()