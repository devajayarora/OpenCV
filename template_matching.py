import numpy as np
import cv2

img = cv2.imread('assets/soccer.webp', 0)
template = cv2.imread('assets/ball.jpg', 0)

h, w = template.shape[:2]

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
           'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for method in methods:
    img2 = img.copy()
    method_eval = eval(method)
    
    # Apply template Matching
    res = cv2.matchTemplate(img2, template, method_eval)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take the minimum
    if method in ['cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']:
        top_left = min_loc
    else:
        top_left = max_loc

    bottom_right = (top_left[0] + w, top_left[1] + h)

    # Draw rectangle on the matched region
    cv2.rectangle(img2, top_left, bottom_right, 255, 5)

    cv2.imshow(method, img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()