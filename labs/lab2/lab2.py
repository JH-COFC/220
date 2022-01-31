# calculate means rms average, harmonic, and geometric

# inputs in numbers, numbers to be averaged and total number of numbers to be averaged
# outputs as results of 3 mean calculations
# gather user inputs, run mean calculation rms average, run mean calculation harmonic, run mean calculation geometric
# #print outputs

import math

def mean_calcs():
    rms, harmonic, geometric = 0,0,1
    n = eval(input("Enter the values to be entered."))
    for i in range(n):
        x = eval(input("Enter value"))
        rms = rms + x**2
        harmonic = harmonic + (1/x)
        geometric = geometric * x
    rms_average = round(math.sqrt((rms/n)),3)
    harmonic_mean = round(n/harmonic,3)
    geometric_mean = round(math.pow(geometric,(1/n)),3)
    print(rms_average,"\n",harmonic_mean,"\n",geometric_mean)

mean_calcs()