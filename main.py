import cv2

# Read the image in grayscale
img_gray = cv2.imread('assets/images.jpg', 0)
img_gray = cv2.resize(img_gray, (300, 300))
img_gray = cv2.resize(img_gray, (0, 0), fx=0.5, fy=0.5)
img_gray = cv2.rotate(img_gray, cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite('assets/images_gray.jpg', img_gray)

# Read the image in color (default behavior)
img_default = cv2.imread('assets/images.jpg', -1)

# Read the image in color (same as -1)
img_color = cv2.imread('assets/images.jpg', 1)

# Display the images in separate windows
cv2.imshow('Grayscale Image', img_gray)
cv2.imshow('Default Image', img_default)
cv2.imshow('Color Image', img_color)

# Wait for a key press to close the windows
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()

