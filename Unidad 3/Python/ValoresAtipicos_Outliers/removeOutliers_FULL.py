import math
################################################################################################
#LOAD DATASET
file2read = open("iris_completa.csv")
file_content = file2read.readlines()
file2read.close()
#############################################################################################
dataset = []
headers = file_content[0].replace("\n","").split(",")
del file_content[0]  #remove headers from dataset 
for i in file_content:
    aux = (i.replace("\n","")).split(",")
    aux = [float(aux[i]) for i in range(len(aux)-1)] + [aux[-1]]
    dataset.append(aux)
################################################################################################        
################################################################################################
##per attribute
for i in range(len(dataset[0])-1):
    ################################################################################################
    dataset.sort(key=lambda x:x[i])        
    ################################################################################################            
    posQ1 = (len(dataset)+1)/4
    posQ3 = 3*(len(dataset)+1)/4
    ################################################################################################            
    p_decimal_Q1, p_entera_Q1 = math.modf(posQ1)
    p_entera_Q1 = int(p_entera_Q1)
    Q1 = dataset[p_entera_Q1-1][i]+p_decimal_Q1*(dataset[p_entera_Q1][i]-dataset[p_entera_Q1-1][i]) #Index starts in 0
    ################################################################################################    
    p_decimal_Q3, p_entera_Q3 = math.modf(posQ3)
    p_entera_Q3 = int(p_entera_Q3)
    Q3 = dataset[p_entera_Q3-1][i]+p_decimal_Q3*(dataset[p_entera_Q3][i]-dataset[p_entera_Q3-1][i]) #Index starts in 0
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
    auxiliar = []
    for value in dataset:
        if value[i] < lower_limit or value[i] > upper_limit:
            print("outlier found: ",  value)
        else:
            auxiliar.append(value)            
    dataset = auxiliar.copy()
    print()
################################################################################################
#Unsort the dataset
import random as rnd
rnd.shuffle(dataset)
################################################################################################
#Create new instance
file2write = open("iris_without_outliers.csv", "w")
for register in dataset:
    for i  in range(len(register)-1):
        file2write.write(str(register[i]) +  ",")
    file2write.write(str(register[-1]) + "\n")    
file2write.close()
################################################################################################

