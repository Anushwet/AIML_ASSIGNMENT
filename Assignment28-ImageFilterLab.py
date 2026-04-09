import cv2
import matplotlib.pyplot as plt

# Step 1: Load image
image = cv2.imread('photo.jpeg')   # make sure image is in same folder

if image is None:
    print(" Image not found!")
    exit()

# Convert BGR to RGB (for correct display)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Step 2: Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Step 4: Edge Detection
edges = cv2.Canny(blur, 100, 200)

# Step 5: Display all images
plt.figure(figsize=(10,8))

plt.subplot(2,2,1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis('off')

plt.subplot(2,2,2)
plt.imshow(gray, cmap='gray')
plt.title("Grayscale")
plt.axis('off')

plt.subplot(2,2,3)
plt.imshow(blur, cmap='gray')
plt.title("Blur Image")
plt.axis('off')

plt.subplot(2,2,4)
plt.imshow(edges, cmap='gray')
plt.title("Edge Detection")
plt.axis('off')

plt.tight_layout()
plt.show()