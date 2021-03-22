import sys

def main():
    check = check_args(sys.argv)
    if(check):
        print(check)
        return
    f = open(sys.argv[2], 'r', encoding = "utf-8")
    data = f.readlines()
    f.close()
    width, height = tuple(data[1].split())
    pixel_data = []
    for i in range(0, int(width)*int(height)):
        pixel = data[i+3].split()
        pixel_data.append([int(x) for x in pixel])
    if sys.argv[1] == 'fade':
        out = fade_image(pixel_data, int(width), 
                int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]))
    else:
        reach = 4
        if len(sys.argv) >= 4:
            reach = int(sys.argv[3])
        out = blur_image(pixel_data, int(width), reach)
    f = open(sys.argv[1] + '.ppm', 'wb+')
    f.write('P3\n'.encode('utf-8'))
    f.write((' '.join([width, height]) + '\n').encode('utf-8'))
    f.write(data[2].encode('utf-8'))
    for pixel in out:
        f.write((' '.join([str(pixel[0]), str(pixel[1]), 
                str(pixel[2])])+'\n').encode('utf-8'))
    f.close()


def check_args(args):
    if len(args) < 3:
        return "Usage: python3 pixelmagic.py <mode> <image>"
    if args[1] == 'fade' and len(args) < 6:
        return "Usage: python3 pixelmagic.py fade <image> <row> <col> <radius>"
    if args[1] != 'blur' and args[1] != 'fade':
        return "Error: Invalid mode"
    try:
        f = open(args[2], 'r', encoding = "utf-8")
        f.close()
    except FileNotFoundError:
        return "Could not open file %s" % args[2]

    return None

def fade_image(pixels, width, row, col, radius):
    for x in range(0, width):
        for y in range(0, int(len(pixels)/width)):
            dist = ((x - col)**2 + (y-row)**2)**(0.5)
            scale = max(0.2, (radius - dist)/radius)
            for i in range(0, 3):
                pixels[y*width+x][i] = int(pixels[y*width+x][i]*scale)
    return pixels

def blur_image(pixels, width, reach):
    height = int(len(pixels)/width)
    out = []
    for i in range(0, width*height):
        out.append([0, 0, 0])
    for x in range(0, width):
        for y in range(0, height):
            for i in range(0, 3):
                s, c = (0, 0)
                for x_off in range(-reach, reach+1):
                    for y_off in range(-reach, reach+1):
                        x_r, y_r = (x+x_off, y+y_off)
                        if(x_r>=0 and x_r<width):
                            if(y_r>=0 and y_r<height):
                                s += pixels[y_r*width+x_r][i]
                                c += 1
                out[y*width+x][i] = int(s/c)
    return out

main()
