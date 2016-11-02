import math
import random
from PIL import Image


# distance between (x1, y1) and (x2, y2)
def hyp(x1, x2, y1, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

# shade at point (x1, y1) from a rock centered at (cX, cY)
def shadeAt(cX, cY, x1, y1, rippleRadius):
    return 255.0/rippleRadius * (abs(hyp(cX, x1, y1, cY) % (2*rippleRadius) - rippleRadius))

def main(xSize = 1200, ySize = 1200,
         rockXs = [random.randint(200,300), random.randint(700,900)],
         rockYs = [random.randint(200,300), random.randint(700,900)]):
    
    img = Image.new('RGB', (xSize, ySize), "black") # create new image
    pixels = img.load() # create pixel map
    
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            color = 0
            for k in range(len(rockXs)):
                color = 40 + (color + shadeAt(rockXs[k], rockYs[k], i, j,  xSize/40.0)) % 170;
            pixels[i,j] = (130, int(color), int(color)) # set the colour at each pixel

    img.save("TiledRipples.png", "PNG")


main()