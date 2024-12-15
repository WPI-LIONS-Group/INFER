import sys
from PIL import Image

def hide_message(image_path, message):
    # Open the image using the .open() function from Image and image_path
    #img = TODO

    # Convert the message to binary
    #binary_message = TODO

    # Embed the binary message into the image pixels
    # Load the pixels in img using the PIL library
    #pixels = TODO
    index = 0
    for x in range(img.width):
        #for y in range(TODO pass the height of img):
            r, g, b = pixels[x, y]

            # Modify the least significant bit of each color channel
            if index < len(binary_message):
                #TODO clear only the last bit of the red(r) value. If binary_message[index] has a value then replace pixels[x,y] with that value
                #TODO move to the next index by adding 1 to index

    # Save img by calling the .save() function from the PIL library on it. Pass in the file name "output.png" so you do not overwrite the original image.
    #img.save(TODO)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python myStegTool.py <image_file>")
        sys.exit(1)

    image_path = sys.argv[1]
    message = input("Enter the message to hide: ")
    hide_message(image_path, message)
    print("Message hidden in the image. Output image: output.png")
