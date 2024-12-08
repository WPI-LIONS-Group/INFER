import sys
from PIL import Image

def extract_message(image_path):
    # Open the image using the .open() function from Image and image_path
    #img = TODO

    # Extract the binary message from the image pixels
    binary_message = ""
    # Load the pixels in img using the PIL library
    #pixels = TODO

    for x in range(img.width):
        #for y in range(TODO pass the height of img):
            r, g, b = pixels[x, y]

            # Extract the least significant bit from the red channel
            #binary_message += TODO

    # Convert the binary message back to text
    message = ""
    #How many bits are in a byte? Replace the following 2 TODOS with that number
    #for i in range(0, len(binary_message), TODO):
        #byte = binary_message[i:i + TODO]
        #What is the base number in binary? Replace the following T0D0 with that number
        #message += chr(int(byte, TODO))

    return message

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python messageExtract.py <image_file>")
        sys.exit(1)

    image_path = sys.argv[1]
    hidden_message = extract_message(image_path)
    print(hidden_message)
