import os
from PIL import Image

# Path to the folder containing JPG images
folder_path = 'new'

# List all files in the folder
files = os.listdir(folder_path)

# Filter JPG files
jpg_files = [f for f in files if f.lower().endswith('.jpg')]

# Sort the files to maintain order
jpg_files.sort()

# Counter for naming PNG files
counter = 1

# Convert and rename JPG files to PNG
for jpg_file in jpg_files:
    # Open the JPG image
    with Image.open(os.path.join(folder_path, jpg_file)) as img:
        # Save the image as PNG with the desired naming convention
        img.save(os.path.join(folder_path, f"image{counter:03d}.png"), 'PNG')
        counter += 1

print("Conversion completed.")
