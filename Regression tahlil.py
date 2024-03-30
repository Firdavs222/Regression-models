# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 11:06:27 2024

@author: user
"""

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
#kerakli modullar import qilinadi;

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

#x = [1,2,3,5,6,7,8,9,10,12,13,14,15,16,18,19,21,22]
#y = [100,90,80,60,60,55,60,65,70,70,75,76,78,79,90,99,99,100]

slope, intercept, r, p, std_error = stats.linregress(x,y)
#slope - burchak koeffitsiyent;
#intercept - kx+b funksiyaning b parametri;
#r - korrelyatsiya koeffitsiyenti;
#p - r koeffitsiyentning ahamiyatlilgini baholaydi(odatda 0,05 dan kichik)
#std_error - burchak koeffitsiyentni xatoligi tekshriladi(Student mezoni bo'yicha)


def linregressfunction(x):
    return slope * x + intercept

mymodel1 = list(map(linregressfunction, x))

mymodel2 = np.poly1d(np.polyfit(x, y, 3))
myline = np.linspace(2, 17,100)

plt.scatter(x, y)
plt.plot(x, mymodel1)
plt.plot(myline, mymodel2(myline))
plt.show()
print(f"Korrelyatsiya koeffitsiyenti: {r:.2f}, P: {p:.4f}, Standart error: {std_error:.2f}")
print(f"Egri chiziqli regressiyaning formulasi quyidagicha: \n {mymodel2}")
