import argparse
import os
from PIL import Image

def createImage(message: str, characters: str, output: str):
    if not os.path.exists(output):
        print(f"Output '{output}' does not exist, creating")
        os.makedirs(output)

    images = []
    for character in message:
        path = os.path.join(characters, f"{character}.png")
        if not os.path.exists(path):
            print(f"ERROR: Image file '{path}' not found, aborting")
            return
        img = Image.open(path)
        img.load()
        images.append(img)

    # Assumes all images are the same width
    widths, heights = zip(*(i.size for i in images))
    
    total_height = sum(heights)
    new_img = Image.new('RGB', (widths[0], total_height), color='white') # White background

    y_offset = 0
    for img in images:
        # Paste the image onto the new canvas
        # We align to the left if widths differ
        new_img.paste(img, (0, y_offset))
        y_offset += img.height

    output_path = os.path.join(output, f"{message}.png")
    new_img.save(output_path)

    print(f"Image file {output_path} created!")

def main():
    """
    Generate images with characters for knitting friendship bracelets with initials with AYAB
    Flags: --characters, --output, and --message.
    """

    parser = argparse.ArgumentParser(
        description="Generate images with characters for knitting friendship bracelets with initials with AYAB"
    )

    # 2. Define the string flags (arguments)
    # Each add_argument() call defines a new command-line argument.
    # The 'type=str' explicitly sets the expected type for the argument's value.
    # 'help' provides a description for the argument in the help message.

    parser.add_argument(
        '--characters',
        type=str,
        default="./characters", # A default value if the flag is not provided
        help="Where to find the character image inputs defaults to ./characters"
    )

    parser.add_argument(
        '--output',
        type=str,
        default="./output", # Default output destination
        help="Specifies the output destination defaults to ./output."
    )

    parser.add_argument(
        '--message',
        type=str,
        default="abc",
        help="A string of characters to create an image for"
    )

    # 3. Parse the arguments from the command line
    # This method reads the command-line arguments and stores them as attributes
    # of the 'args' object.
    args = parser.parse_args()

    # 4. Access and print the values of the flags
    print(f"Characters location: '{args.characters}'")
    print(f"Output location:    '{args.output}'")
    print(f"Message: '{args.message.upper()}'")

    createImage(args.message.upper(), args.characters, args.output)


if __name__ == "__main__":
    main()
