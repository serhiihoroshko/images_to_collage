from PIL import Image
import os

# Define input and output folder paths
folder_path = "G:\\"  # Change this to the desired drive letter or path
input_folder = os.path.join(folder_path, "images_to_collage", "images")
output_folder = os.path.join(folder_path, "images_to_collage", "collages")

# Define a list of filenames to exclude
exclude_filenames = ["example01.jpg", "example02.jpg", "example03.jpg"]

os.makedirs(output_folder, exist_ok=True)

# Iterate through subfolders in the input folder
for folder_name in os.listdir(input_folder):
    subfolder_path = os.path.join(input_folder, folder_name)

    if os.path.isdir(subfolder_path):
        image_files = []
        for root, dirs, files in os.walk(subfolder_path):
            for filename in files:
                # Check if the file is an image and not in the list of excluded filenames
                if filename.endswith((".jpg", ".png")) and filename not in exclude_filenames:
                    image_files.append(os.path.join(root, filename))

        if image_files:
            # Create two collages, one with a 5-image layout and another with a 10-image layout
            collage_1 = Image.new("RGB", (2000, 2000), "white")
            collage_2 = Image.new("RGB", (2000, 2000), "white")
            x, y = 0, 0

            # Loop through the list of image files
            for image_file in image_files:
                input_image = Image.open(image_file)

                # First collage layout
                collage_1.paste(input_image.resize((1500, 1500)), (0, 300))
                collage_1.paste(input_image.resize((500, 500)), (1500, 0))
                collage_1.paste(input_image.resize((500, 500)), (1500, 500))
                collage_1.paste(input_image.resize((500, 500)), (1500, 1000))
                collage_1.paste(input_image.resize((500, 500)), (1500, 1500))

                # Second collage layout
                collage_2.paste(input_image.resize((1600, 1600)), (0, 0))
                collage_2.paste(input_image.resize((400, 400)), (0, 1600))
                collage_2.paste(input_image.resize((400, 400)), (400, 1600))
                collage_2.paste(input_image.resize((400, 400)), (800, 1600))
                collage_2.paste(input_image.resize((400, 400)), (1200, 1600))
                collage_2.paste(input_image.resize((400, 400)), (1600, 1600))
                collage_2.paste(input_image.resize((400, 400)), (1600, 0))
                collage_2.paste(input_image.resize((400, 400)), (1600, 400))
                collage_2.paste(input_image.resize((400, 400)), (1600, 800))
                collage_2.paste(input_image.resize((400, 400)), (1600, 1200))

                # The code snippet is a part of the loop that controls the placement of images on the collage
                if x >= 1600:
                    x = 0
                    y += 400

            # Save the collages with folder-specific names
            collage_1.save(os.path.join(output_folder, f"{folder_name}_collage_1.jpg"))
            collage_2.save(os.path.join(output_folder, f"{folder_name}_collage_2.jpg"))
