import numpy as np
import matplotlib.pyplot as pltlib
import math

def find_probability(x , mean , standard_dev):
    probability =  np.exp(-0.5*((x-mean)**2/(standard_dev)**2)) / (math.sqrt(2 * np.pi)*standard_dev)
    return probability


normal_distr = np.random.normal(0,1,(1000))


sum = 0
y = 0
for i in range(1,1000):
    prob_p = find_probability(normal_distr[i], 0, 1)
    prob_q = find_probability(normal_distr[i], 0, 2)
    prob_q += 1e-12
    y = prob_p/prob_q
    sum += np.log(y + 1e-12)
    
    
    
result = sum/1000
print(result)
    
    
