import random

sensor1 = []
sensor2 = []
sensor3 = []

for i in range(10):
    sensor1.append(random.randint(0,1023))
    sensor2.append(random.randint(0,1023))
    sensor3.append(random.randint(0,1023))

print(sensor1)
print(sensor2)
print(sensor3)


from scipy import stats

#Friedman Test
res = stats.friedmanchisquare(sensor1, sensor2, sensor3)
#Si pvalue < 0.05 se rechaza Ho y se acepta Ha
print(res)

############################################################
import numpy as np
data = np.array([sensor1, sensor2, sensor3])
############################################################

from scikit_posthocs import posthoc_nemenyi_friedman #pip install scikit-posthocs
res = posthoc_nemenyi_friedman(data.T)
print(res)

############################################################
print()
############################################################
from scikit_posthocs import posthoc_conover_friedman
res = posthoc_conover_friedman(data.T)
print(res)

