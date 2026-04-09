import cv2
import matplotlib.pyplot as plt

# Load image
image = cv2.imread('photo.jpeg')

# Check
if image is None:
    print("Error: Image not found!")
else:
    print("✅ Image loaded successfully!")

    # Shape
    print("Shape:", image.shape)

    # Pixel values
    print("\nSample Pixels:")
    print(image[0:3, 0:3])

    # Channels
    print("\nBlue channel shape:", image[:, :, 0].shape)
    print("Green channel shape:", image[:, :, 1].shape)
    print("Red channel shape:", image[:, :, 2].shape)

    # Show image
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    plt.imshow(image_rgb)
    plt.axis('off')
    plt.show()