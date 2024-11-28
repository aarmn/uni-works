import numpy as np
from PIL import Image
import os

def convert_to_greyscale(input_path, output_path):
    """
    Convert a color TIF image to greyscale
    
    Parameters:
    input_path: str - path to input TIF image
    output_path: str - path to save greyscale image
    """

    # PIL method
    # Open the image
    img = Image.open(input_path)
    
    # Convert to greyscale
    grey_img = img.convert('L')
    
    # Save the image
    grey_img.save(output_path)

def main():
    # Example usage
    input_file = "./images/fetus-us.tif"
    output_file = "./images/fetus-us-grey.tif"
    
    try:
        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        # Convert using PIL
        convert_to_greyscale(input_file, output_file)
        print(f"Successfully converted {input_file} to greyscale")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()