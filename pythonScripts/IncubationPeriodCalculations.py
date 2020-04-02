import numpy as np
import math
from scipy.stats import gamma

x = [i for i in range(15) ]
a = 5.807
b = 0.948
def pdff(x):
    return (1/((b**a)*math.gamma(a)))*x**(a-1)*math.exp(-x/b)

pdf = [pdff(i) for i in x]
cdf = [gamma.cdf(i,a,b) for i in x]

f = open('../js/data/IncubationPeriod.js','w')
f.write("let x = " + str(x) + ";\n") 
f.write("let pdf = " + str(pdf) + ";\n")
f.write("let cdf = " + str(cdf) + ";\n")
f.close() 