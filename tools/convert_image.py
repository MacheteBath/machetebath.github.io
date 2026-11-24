import os
import sys
from PIL import Image


def convert_to_webp(source_path):
    # Quick safety check to make sure the file actually exists
    if not os.path.exists(source_path):
        print(f"Error: The file '{source_path}' could not be found.")
        return

    # Determine the output path by swapping the extension to .webp
    destination = os.path.splitext(source_path)[0] + ".webp"

    # Open the image and save it as a high-quality WebP
    with Image.open(source_path) as img:
        img.save(destination, "WEBP", quality=90)

    print(f"Success! Converted to: {destination}")


if __name__ == "__main__":
    # Check if the user passed a file argument
    if len(sys.argv) < 2:
        print("Usage: python convert.py <path_to_image>")
    else:
        # sys.argv[1] grabs the first argument passed after the script name
        target_image = sys.argv[1]
        convert_to_webp(target_image)
