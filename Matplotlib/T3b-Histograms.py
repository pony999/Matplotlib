""" Source:
    https://www.youtube.com/watch?v=ZyTO4SwhSeE&list=PLQVvvaa0QuDfefDfXb9Yf0la1fPDKluPF&index=3

    Tutorial 3:
    Bar charts and Histograms
"""

import matplotlib.pyplot as plt

population_age = [51,81,77,29,1,89,54,7,23,56,45,23,7,65,45,24,34,23,73,8,3,25,72,83,16,62,36,97,24,45,44,73,27,79]

# ids = [x for x in range(len(population_age))]

bins = [0,10,20,30,40,50,60,70,80,90,100]

plt.hist(population_age, bins, histtype='bar', rwidth=0.8)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting graph')
plt.show()
