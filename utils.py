import os
import json
from PIL import Image, ImageDraw


def process_images_and_coordinates(data_directory):
    # Initialize an empty dictionary to store results
    coordinates_dict = {}

    # Loop through all the images in the directory
    for filename in os.listdir(data_directory):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            # Get the corresponding txt file
            txt_filename = filename.rsplit('.', 1)[0] + '.txt'  # Replace the extension with '.txt'
            txt_path = os.path.join(data_directory, txt_filename)

            if os.path.exists(txt_path):
                # Read the content of the txt file
                with open(txt_path, 'r') as file:
                    content = file.readline().strip()  # Read the first line
                    values = content.split()  # Split the values by space

                    if len(values) >= 5:
                        # Extract the 2nd to 5th values (ignoring the first one)
                        coordinates = list(map(float, values[1:5]))

                        # Store the coordinates using the image filename as the key
                        coordinates_dict[filename] = coordinates

    # Save the result to a JSON file
    output_path = os.path.join(data_directory, 'coordinates.json')
    with open(output_path, 'w') as json_file:
        json.dump(coordinates_dict, json_file, indent=4)

    print(f"Coordinates saved to {output_path}")


def draw_bounding_box(image_path, bounding_box, output_path, use_normalized=True):
    """
    Draws a bounding box on an image.

    Parameters:
    - image_path: str, path to the image.
    - bounding_box: list, bounding box coordinates. If use_normalized=True, the format is [x_min, y_min, x_max, y_max]
                    with normalized values between 0 and 1. If use_normalized=False, it should be pixel coordinates.
    - output_path: str, path to save the inference_results image with the bounding box.
    - use_normalized: bool, if True, the bounding box is in normalized units; if False, it is in pixel values.
    """
    # Load the image
    image = Image.open(image_path)
    image_width, image_height = image.size

    if use_normalized:
        x_min_norm, y_min_norm, x_max_norm, y_max_norm = bounding_box
        x_min = int(x_min_norm * image_width)
        y_min = int(y_min_norm * image_height)
        x_max = int(x_max_norm * image_width)
        y_max = int(y_max_norm * image_height)
    else:
        x_min, y_min, x_max, y_max = bounding_box

    draw = ImageDraw.Draw(image)
    draw.rectangle([x_min, y_min, x_max, y_max], outline="red", width=10)

    image.save(output_path)
    print(f"Image saved with bounding box at {output_path}")


IMAGE = 'img1004588.jpg'

image_path = (f"/Users/geronimobasso/Desktop/extra/drones/database/Originales/{IMAGE}")

bounding_box_normalized = [0.35390625, 0.24861111111111112, 0.025, 0.05277777777777778]
bounding_box_pixels = [109, 187, 163, 251]

OUTPUT_IMAGE = "bb_" + IMAGE
OUTPUT_PATH = f"inference_results/{OUTPUT_IMAGE}"

draw_bounding_box(image_path, bounding_box_normalized, OUTPUT_PATH, use_normalized=True)

#process_images_and_coordinates('images/')
