import math
################################################################################################
#LOAD AND SORT DATASET
file = open("instancia_toReview.txt")
file_content = file.readlines()
print(file_content)
dataset = [int(i) for i in file_content]
print("Dataset: ", dataset)
dataset.sort()
print("Sort Dataset: ", dataset)
################################################################################################
posQ1 = (len(dataset)+1)/4
posQ3 = 3*(len(dataset)+1)/4
################################################################################################
p_decimal, p_entera = math.modf(posQ1)
p_entera = int(p_entera)
Q1 = dataset[p_entera-1]+p_decimal*(dataset[p_entera]-dataset[p_entera-1]) #Index starts in 0
################################################################################################
p_decimal, p_entera = math.modf(posQ3)
p_entera = int(p_entera)
Q3 = dataset[p_entera-1]+p_decimal*(dataset[p_entera]-dataset[p_entera-1]) #Index starts in 0
################################################################################################
print("Q1-Position: ", posQ1, " Q1 Value: ", Q1)
print("Q3-Position: ", posQ3, " Q3 Value: ", Q3)
################################################################################################
IQR = Q3-Q1
print("IQR: ", IQR)
################################################################################################
## Determines the reach of the whiskers to the beyond the first and third quartiles
whiskers = 1.5
#whiskers = 3.0 
#
################################################################################################
#
lower_limit = Q1 - whiskers * IQR
upper_limit = Q3 + whiskers * IQR
print("LOWER LIMIT: ", lower_limit, " UPPER LIMIT: ", upper_limit)
#
################################################################################################
##REVIEW DATASET TO FIND AND ELIMINATE OUTLIERS
#
for value in dataset:
    if value < lower_limit or value > upper_limit:
        print("outlier found: ",  value)

