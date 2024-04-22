
import numpy
datos = [12, 14, 16, 17, 18, 20, 20, 24, 28, 32]

#Pos1q1 = (1 * (10+1)) / 4  #.... Q1 = 15.5
#Pos2q2 = (2 * (10+1)) / 4  # ... Q2 = 19
#Pos3q3 = (3 * (10+1)) / 4  # ... Q3 = 25
print()

################################################################################################
#forma 0
#x = numpy.quantile(datos, [0,0.25,0.5,0.75,1])
x = numpy.quantile(datos, [0.25,0.5,0.75], method="weibull")
print(x)
#for i in x:
#    print(i)
################################################################################################
#forma 1
#x = numpy.quantile(datos, [0,0.25,0.5,0.75,1])
x = numpy.quantile(datos, [0.25,0.5,0.75])
print(x)
#for i in x:
#    print(i)
################################################################################################
#forma 2
q1, q2, q3 = numpy.percentile (datos, [25, 50, 75])
#iqr = q3 - q1
print(q1)
print(q2)
print(q3)
#print(iqr)

################################################################################################
#forma 3
import math
posQ1 = (len(datos)+1)/4
posQ3 = 3*(len(datos)+1)/4

p_decimal_Q1, p_entera_Q1 = math.modf(posQ1)
p_entera_Q1 = int(p_entera_Q1)
Q1 = datos[p_entera_Q1-1]+p_decimal_Q1*(datos[p_entera_Q1]-datos[p_entera_Q1-1]) #Index starts in 0

p_decimal_Q3, p_entera_Q3 = math.modf(posQ3)
p_entera_Q3 = int(p_entera_Q3)
Q3 = datos[p_entera_Q3-1]+p_decimal_Q3*(datos[p_entera_Q3]-datos[p_entera_Q3-1]) #Index starts in 0

print("Q1-Position: ", posQ1, " Q1 Value: ", Q1)
print("Q3-Position: ", posQ3, " Q3 Value: ", Q3)

IQR = Q3-Q1
print("IQR: ", IQR)
################################################################################################
