## tiled-ripples

Creates a tiled pattern inspired by the interference of ripples/waves (for example, two rocks dropped in a pond). 

### Usage

    python tiled-ripples.py

The output will be stored in `TiledRipples.png`. The program runs a `main()` function with default arguments for `xSize`, `ySize`, `rockXs`, and `rockYs`. `xSize` and `ySize` control the width and height of the image produced (in pixels), `rockXs` and `rockYs` are lists containing the coordinates for the locations of the "rocks" that generate the image (more detail below). As a default, the image produced is 1200 by 1200 and there are two rocks, one randomly generated to be in the top left and one randomly generated in the bottom right. 

### Sample

![Screenshot](http://i.imgur.com/JkgArvx.png)

### Algorithm

A rock dropped in a pond creates a ripple. A simplistic representation of this is given by running the program with only one rock -- e.x. `main(rockXs = [600], rockYs = [600])`. 
<p align="center">
    <img src="https://i.imgur.com/lP0tKkx.png" width="300"/>
</p>

This works with the `shadeAt` function - if a point is at distance *d* from the rock, and the provided ripple radius is *r*, the function computes `abs(d % (2*r) - r)`. As this ranges between *0* and *r*, the function scales this by 255/*r* for a pixel intensity value. 

Where it gets interesting is in the interaction between ripples. To create the tiled pattern, instead of modeling the constructive/destructive interference seen in the natural world, the program *directly adds* pixel intensity values given by each rock, allowing them to overflow and then taking them modulo 256. The crests of two waves may add to a trough. 

After adding coloring effects, we get the image seen above. 