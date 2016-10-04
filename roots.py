import numpy as np
from itertools import product
from tqdm import tqdm
from argparse import ArgumentParser


def save_roots(degree, datafile):
    total_polys = 2**degree
    roots = np.zeros((total_polys, degree)).astype(np.complex)
    
    with open(datafile, 'w') as f:  
        for k, poly in enumerate(tqdm(product(*([[-1, 1]] * degree)),
                                      total=total_polys,
                                      unit=' polys')):
            roots[k] =  np.roots((1,) + poly)
        np.save(f, roots.ravel())
    
def main():    
    parser = ArgumentParser()
    parser.add_argument('-d', type=int, default=18,
                        help='polynomial degree')
    parser.add_argument('-f', type=str, default='data.npy',
                        help='output filename')                        
    args = parser.parse_args()
    
    save_roots(args.d, args.f)
    

if __name__ == '__main__':
    main()

    
                        
            
