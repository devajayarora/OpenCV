import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    width = int(cap.get(3))  # Get the width of the frame
    height = int(cap.get(4))  # Get the height of the frame

    # image = np.zeros(frame.shape, np.uint8)
    # smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    
    # image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)  # Top-left quarter
    # image[height//2:, :width//2] = smaller_frame  # Bottom-left quarter
    # image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)  # Top-right quarter
    # image[height//2:, width//2:] = smaller_frame  # Bottom-right quarter

    # Draw a diagonal lines, rectangle and circle across the frame
    # img: MatLike, pt1: Point, pt2: Point, color: Scalar, thickness: int
    image = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 5)
    image = cv2.line(image, (0, height), (width, 0), (0, 255, 0), 5)
    image = cv2.rectangle(image, (100, 100), (400, 200), (0, 0, 255), 5)
    image = cv2.circle(image, (int(width/2), int(height/2)), 50, (255, 255, 0), -1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    image = cv2.putText(image, 'OpenCV Video Feed', (50, 50), font, 1, (255, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow('Video Feed', image)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()