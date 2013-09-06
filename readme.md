Beauty of Roots
===============

This script generates a fractal from polynomial roots . First time when i saw this image i wanted to print it on canvas ant put it in our office , but printing an image that i found on the internet would not be so much fun right ? so i wrote my own implementation , it looks really cool on our wall . 

__Example__: This is a plot of all roots with coefficents of [1 or -1] and degree of 24 .

![roots](http://alexander-0x80.github.io/data/roots.png)

### How to use :
* Run `roots.py` to generate NumPy array file with a hit map that should be used to draw the PNG .
* Run `plot.py` to create PNG file from the hit map .

#### Example:
Generate hit map for polynomials with degree of 24 inside 512x512 array : 
>`python roots.py 24 512`

This will create `pointmap.npy` file in your working directory . You should use it to produce a color image of the hits .
> `python plot.py pointmap.npy my_image.png`


### More info 
http://mathworld.wolfram.com/PolynomialRoots.html