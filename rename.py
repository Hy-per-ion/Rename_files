import os

# Path to the input dataset folder
input_folder_path = "path_to_input_folder"
# Path to the output folder where renamed images will be saved
output_folder_path = "path_to_output_folder"
# Base name for the renamed images
base_name = "image"

# Create the output folder if it doesn't exist
os.makedirs(output_folder_path, exist_ok=True)

# List all files in the input folder
files = os.listdir(input_folder_path)
# Filter out non-image files
image_files = [file for file in files if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

# Sort the image files
image_files.sort()

# Rename and save the images in the output folder
for i, image_file in enumerate(image_files):
    # Generate the new file name
    new_file_name = f"{base_name}{i+1:04d}.png"
    # Construct the paths
    input_file_path = os.path.join(input_folder_path, image_file)
    output_file_path = os.path.join(output_folder_path, new_file_name)
    # Rename and move the file
    os.rename(input_file_path, output_file_path)
