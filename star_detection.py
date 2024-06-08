import cv2
import numpy as np

# Define the image path
image_path = r'C:\Users\User\image.png'

def detect_stars(image_path):
    # Read the image
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found")
        return None, None

    # Convert to grayscale (for complex tasks RGB separating might be needed)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    # If needed, apply Gaussian blur by
    # blurred = cv2.GaussianBlur(gray, (5, 5), 0)
  
    # No Gaussian blur applied for this example
    blurred = gray

    # Apply a threshold to get only the bright regions, play with the value '150'
    _, thresh = cv2.threshold(blurred, 150, 255, cv2.THRESH_BINARY)

    # Use morphological operations to enhance faint stars
    kernel = np.ones((3, 3), np.uint8)
    thresh = cv2.dilate(thresh, kernel, iterations=1)

    # Find contours which will be the potential stars
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw yellow circles around the stars
    for cnt in contours:
        (x, y), radius = cv2.minEnclosingCircle(cnt)
        center = (int(x), int(y))
        radius = int(radius * 3)  # Radius adjusted as needed
        cv2.circle(img, center, radius, (0, 255, 255), 1)  # Yellow circle with thickness of 1 pixels

    # Save the image with stars detected
    cv2.imwrite('stars_detected.png', img)
    print("Stars detected and image saved as 'stars_detected.png'.")

    return img, contours

# Detect stars
img, contours = detect_stars(image_path)

