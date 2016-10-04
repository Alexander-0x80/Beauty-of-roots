import numpy as np
import matplotlib.pyplot as plt
from argparse import ArgumentParser


x_max = 1.8
x_min = -1.8
y_max = 1.8
y_min = -1.8


def heat_map(size, datafile):
    img = np.zeros((size, size), dtype=np.float)
    f = np.load(datafile, 'r')

    for root in tqdm(f):
        point_x = (size - 1) * (root.real - x_min) / (x_max - x_min)   
        point_y = (size - 1) * (root.imag - y_min) / (y_max - y_min)  
        if all([point_x >= 0,
                point_x <= size - 1,
                point_y >= 0,
                point_y <= size - 1]):
            img[int(point_y)][int(point_x)] += 1
    
    log_max = np.log(np.amax(img))
    ind = np.where(img > 0)
    img[ind] = np.log(img[ind]) / log_max
    return img


def main():
    parser = ArgumentParser()
    parser.add_argument('-s', type=int, default=800,
                        help='image size')      
    parser.add_argument('data', type=str,
                        help='roots data to be loaded')
    parser.add_argument('-o', type=str, default='polyroots.png',
                        help='output filename')                        
    args = parser.parse_args()   
    
    img = heat_map(args.s, args.data)
    fig = plt.figure(figsize=(args.s/100.0, args.s/100.0), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1], aspect=1)
    ax.axis('off')
    ax.imshow(img, cmap='afmhot')
    fig.savefig(args.o)
    
    
if __name__ == '__main__':
    main()
