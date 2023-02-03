import numpy as np
import matplotlib.pyplot as pltlib

gaussian_x = np.random.normal(-1,1,100000)
gaussian_y = np.random.normal(3,2,100000)
gaussian_z = gaussian_x + gaussian_y
pltlib.hist(gaussian_z, bins = 50, alpha= 0.5, color= 'r')
pltlib.title("Histogram of 6.a")
pltlib.show()