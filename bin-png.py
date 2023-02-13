import sys
import png

height=sys.argv[2]
width=sys.argv[1]

if len(sys.argv) != 4:
    print("please use as follows:\npython bin-png.py <width> <height> <file>")
    exit()
def string_to_binary_png(string):

    # Encode the string to utf-8 and pass it to a list

    pixels = [list(string.encode('utf-8'))]

    for e in range(height):
        for i in range(width - len(pixels[e])):
            pixels[e] += [0]
        if e != height-1: pixels += [[]]

    # Write the image to a file in PNG format

    w = png.Writer(width=width, height=height, greyscale=True)
    w.write(open('output.png', 'wb'), pixels)

# Example usage
string_to_binary_png(open(sys.argv[3], 'r').read())
