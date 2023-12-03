import cv2
import numpy as np

# Read the image
image = cv2.imread('path/image.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)

# Apply blur and then extract edges with Canny
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, 50, 50)
#edges = cv2.Canny(gray, 150, 150)

cv2.imshow('a', edges)

# Find contours in the image
contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filter contours to keep only squares
squares = []
for contour in contours:
    perimeter = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.1 * perimeter, True)

    # If it has 4 vertices, then it's a square
    if len(approx) == 4:
        squares.append(approx)

# Find the largest square
largest_square = max(squares, key=cv2.contourArea)

# Create a mask for the largest square
mask = np.zeros_like(gray)
cv2.drawContours(mask, [largest_square], -1, (255), thickness=cv2.FILLED)

# Crop the image using the mask
cropped_image = cv2.bitwise_and(image, image, mask=mask)

# Get bounding box coordinates for the largest square
x, y, w, h = cv2.boundingRect(largest_square)

# Crop the image based on the bounding box
cropped_image_bounding_box = image[y:y+h, x:x+w]

# Show and save the cropped images
cv2.imshow('Cropped Image (Mask)', cropped_image)
cv2.imshow('Cropped Image (Bounding Box)', cropped_image_bounding_box)

# cv2.imwrite('path/cropped_image_mask.jpg', cropped_image)
# cv2.imwrite('path/cropped_image_bounding_box.jpg', cropped_image_bounding_box)
# cv2.imwrite('path/edges.jpg', edges)


cv2.waitKey(0)
cv2.destroyAllWindows()
