

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

#x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
#y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

slope, intercept, r, p, std_error = stats.linregress(x,y)
#r - coeffitcient of correlation;
#p - how much the value of r confidently (usually lower than 0,05)
#std_error - measure of 'Student'

def linregressfunction(x):
    return slope * x + intercept

mymodel1 = list(map(linregressfunction, x))

mymodel2 = np.poly1d(np.polyfit(x, y, 3))
myline = np.linspace(2, 17,100)

plt.scatter(x, y)
plt.plot(x, mymodel1)
plt.plot(myline, mymodel2(myline))
plt.show()
print(f"Correlation coeffitcient: {r:.2f}, P: {p:.4f}, Standart error: {std_error:.2f}")
print(f"Polynomial function's formulae: \n {mymodel2}")

