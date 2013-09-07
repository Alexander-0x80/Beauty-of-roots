Beauty of Roots
===============

This script generates a fractal from polynomial roots . First time when i saw this image i wanted to print it on canvas ant put it in our office , but printing an image that i found on the internet would not be so much fun right ? so i wrote my own implementation , it looks really cool on our wall . 

__Example__: This is a plot of all roots with coefficents of [1 or -1] and degree of 24 .

![roots](http://alexander-0x80.github.io/data/roots.png)

### How to use :
* _roots.py_ - Generates NumPy that contains all generated roots .
* _plot.py_ - Creates PNG image by creating a hit map from roots file .

Generate all roots of polynomials with degree of 14 : 
>`python roots.py 14`

>This will create _pointmap.npy_ file in your working directory . You should use it to produce an image .

> `python plot.py pointmap.npy my_image.png 1024`

### More info 
http://mathworld.wolfram.com/PolynomialRoots.html

### P.S 
I encourage you to generate a big resolution image of the fractal, you should find a lot of interesting patters inside . 