import os
import numpy as np
from PIL import Image

def average_images_in_folder(folder_path):
    images = []

    # Loop through the folder, open each image, and append to the list
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(folder_path, filename)
            img = Image.open(img_path)
            images.append(np.array(img))

    # Check if there are any images loaded
    if not images:
        print("No images found in the folder.")
        return

    # Convert all images to the same size as the first image to ensure consistency
    base_shape = images[0].shape
    resized_images = [np.array(Image.fromarray(img).resize((base_shape[1], base_shape[0]))) for img in images]

    # Calculate the average across all images
    average_image = np.mean(resized_images, axis=0).astype(np.uint8)

    # Convert the average array back to an image
    average_image_pil = Image.fromarray(average_image)

    # Save the averaged image
    save_path = 'ungodly.png'
    average_image_pil.save(save_path)

    print(f"Averaged image saved as {save_path}.")

# Specify the folder path containing your images
folder_path = 'images'
average_images_in_folder(folder_path)
