import numpy as np
import matplotlib.pyplot as pltlib
import math


#I SEPARATED THE CODE INTO 3 PARTS FOR EACH CASE, AFTER CLICKING THE X, THE OTHER GRAPH OPENS

binomial_1 = np.random.binomial(5,0.2,(10000))
binomial_2 = np.random.binomial(5,0.33,(10000))
binomial_3 = np.random.binomial(5,0.5,(10000))

binomial_4 = np.random.binomial(10,0.2,(10000))
binomial_5 = np.random.binomial(10,0.33,(10000))
binomial_6 = np.random.binomial(10,0.5,(10000))

binomial_7 = np.random.binomial(20,0.2,(10000))
binomial_8 = np.random.binomial(20,0.33,(10000))
binomial_9 = np.random.binomial(20,0.5,(10000))

binomial_10 = np.random.binomial(30,0.2,(10000))
binomial_11 = np.random.binomial(30,0.33,(10000))
binomial_12 = np.random.binomial(30,0.5,(10000))

binomial_13 = np.random.binomial(40,0.2,(10000))
binomial_14 = np.random.binomial(40,0.33,(10000))
binomial_15 = np.random.binomial(40,0.5,(10000))

binomial_16 = np.random.binomial(100,0.2,(10000))
binomial_17 = np.random.binomial(100,0.33,(10000))
binomial_18 = np.random.binomial(100,0.5,(10000))

normal_1 = np.random.normal((0.2*5),math.sqrt(5*0.2*0.8),(10000))
normal_2 = np.random.normal((0.33*5),math.sqrt(5*0.33*0.67),(10000))
normal_3 = np.random.normal((0.5*5),math.sqrt(5*0.5*0.5),(10000))

normal_4 = np.random.normal((0.2*10),math.sqrt(10*0.2*0.8),(10000))
normal_5 = np.random.normal((0.33*10),math.sqrt(10*0.33*0.67),(10000))
normal_6 = np.random.normal((0.5*10),math.sqrt(10*0.5*0.5),(10000))

normal_7 = np.random.normal((0.2*20),math.sqrt(20*0.2*0.8),(10000))
normal_8 = np.random.normal((0.33*20),math.sqrt(20*0.33*0.67),(10000))
normal_9 = np.random.normal((0.5*20),math.sqrt(20*0.5*0.5),(10000))

normal_10 = np.random.normal((0.2*30),math.sqrt(30*0.2*0.8),(10000))
normal_11 = np.random.normal((0.33*30),math.sqrt(30*0.33*0.67),(10000))
normal_12 = np.random.normal((0.5*30),math.sqrt(30*0.5*0.5),(10000))

normal_13 = np.random.normal((0.2*40),math.sqrt(40*0.2*0.8),(10000))
normal_14 = np.random.normal((0.33*40),math.sqrt(40*0.33*0.67),(10000))
normal_15 = np.random.normal((0.5*40),math.sqrt(40*0.5*0.5),(10000))

normal_16 = np.random.normal((0.2*100),math.sqrt(100*0.2*0.8),(10000))
normal_17 = np.random.normal((0.33*100),math.sqrt(100*0.33*0.67),(10000))
normal_18 = np.random.normal((0.5*100),math.sqrt(100*0.5*0.5),(10000))


pltlib.hist(binomial_1, bins = 50, alpha= 0.5,label= "binomial n=5 ; p=0.2")
pltlib.hist(normal_1, bins = 50, alpha= 0.5, label= "normal, n=5 ; p=0.2")

pltlib.hist(binomial_4, bins = 50, alpha= 0.5, label= "binomial n=10 ; p=0.2")
pltlib.hist(normal_4, bins = 50, alpha= 0.5, label= "normal, n=10 ; p=0.2")

pltlib.hist(binomial_7, bins = 50, alpha= 0.5, label= "binomial n=20 ; p=0.2")
pltlib.hist(normal_7, bins = 50, alpha= 0.5, label= "normal, n=20 ; p=0.2")

pltlib.hist(binomial_10, bins = 50, alpha= 0.5, label= "binomial n=30 ; p=0.2")
pltlib.hist(normal_10,  bins = 50, alpha= 0.5,label= "normal, n=30 ; p=0.2")

pltlib.hist(binomial_13, bins = 50, alpha= 0.5, label= "binomial n=40 ; p=0.2")
pltlib.hist(normal_13, bins = 50, alpha= 0.5, label= "normal, n=40 ; p=0.2")

pltlib.hist(binomial_16,  bins = 50, alpha= 0.5, label= "binomial n=100 ; p=0.2")
pltlib.hist(normal_16,  bins = 50, alpha= 0.5,label= "normal, n=100 ; p=0.2")

pltlib.title("6.b; p = 0.2 case")
pltlib.legend()
pltlib.show()

pltlib.hist(binomial_2, bins = 50, alpha= 0.5, label= "binomial n=5 ; p=0.33")
pltlib.hist(normal_2,  bins = 50, alpha= 0.5,label= "normal, n=5 ; p=0.33")

pltlib.hist(binomial_5, bins = 50, alpha= 0.5, label= "binomial n=10 ; p=0.33")
pltlib.hist(normal_5, bins = 50, alpha= 0.5, label= "normal, n=10 ; p=0.33")

pltlib.hist(binomial_8, bins = 50, alpha= 0.5, label= "binomial n=20 ; p=0.33")
pltlib.hist(normal_8, bins = 50, alpha= 0.5, label= "normal, n=20 ; p=0.33")

pltlib.hist(binomial_11, bins = 50, alpha= 0.5, label= "binomial n=30 ; p=0.33")
pltlib.hist(normal_11, bins = 50, alpha= 0.5, label= "normal, n=30 ; p=0.33")

pltlib.hist(binomial_14, bins = 50, alpha= 0.5, label= "binomial n=40 ; p=0.33")
pltlib.hist(normal_14, bins = 50, alpha= 0.5, label= "normal, n=40 ; p=0.33")

pltlib.hist(binomial_17,  bins = 50, alpha= 0.5, label= "binomial n=100 ; p=0.33")
pltlib.hist(normal_17,  bins = 50, alpha= 0.5, label= "normal, n=100 ; p=0.33")

pltlib.title("6.b; p = 0.33 case")
pltlib.legend()
pltlib.show()

pltlib.hist(binomial_3, bins = 50, alpha= 0.5, label= "binomial n=5 ; p=0.5")
pltlib.hist(normal_3, bins = 50, alpha= 0.5, label= "normal, n=5 ; p=0.5")

pltlib.hist(binomial_6, bins = 50, alpha= 0.5, label= "binomial n=10 ; p=0.5")
pltlib.hist(normal_6, bins = 50, alpha= 0.5, label= "normal, n=10 ; p=0.5")


pltlib.hist(binomial_9, bins = 50, alpha= 0.5, label= "binomial n=20 ; p=0.5")
pltlib.hist(normal_9,  bins = 50, alpha= 0.5,label= "normal, n=20 ; p=0.5")


pltlib.hist(binomial_12, bins = 50, alpha= 0.5, label= "binomial n=30 ; p=0.5")
pltlib.hist(normal_12, bins = 50, alpha= 0.5, label= "normal, n=30 ; p=0.5")


pltlib.hist(binomial_15,  bins = 50, alpha= 0.5,label= "binomial n=40 ; p=0.5")
pltlib.hist(normal_15,  bins = 50, alpha= 0.5,label= "normal, n=40 ; p=0.5")


pltlib.hist(binomial_18, bins = 50, alpha= 0.5, label= "binomial n=100 ; p=0.5")
pltlib.hist(normal_18, bins = 50, alpha= 0.5, label= "normal, n=100 ; p=0.5")

pltlib.title("6b; p = 0.5 case")
pltlib.legend()
pltlib.show()