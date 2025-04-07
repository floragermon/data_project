## some machine learning - Fundamentally, machine learning involves building mathematical models to help understand data.
## supervised  - classisification,regression and unsupervised learning - clustering, dimensionality reduction 
import scipy
from scipy import stats
from sklearn.linear_model import LinearRegression
model = LinearRegression(fit_intercept=True)

import matplotlib.pyplot as plt

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]


slope, intercept, r , p, std_err = stats.linregress(x,y)
def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, x))
plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

def future(n):
    return(myfunc(n))

future(10)

#simple face detection pipeline
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np

