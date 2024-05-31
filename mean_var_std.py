import numpy as np

def calculate(list):
    calculations = {}
    if len(list) ==9:
        a = np.array(list)
        b = a.reshape(3,3) #Reshaping 

        #For Mean
        mean_axis0 = b.mean(axis=0)
        mean_axis1 = b.mean(axis=1)
        mean_flatten = a.mean()
        mean = [mean_axis0.tolist(), mean_axis1.tolist(), mean_flatten.tolist()]
        calculations['mean'] = mean

        #For Variance
        variance_axis0 = b.var(axis=0)
        variance_axis1 = b.var(axis=1)
        variance_flatten = a.var()
        variance = [variance_axis0.tolist(), variance_axis1.tolist(), variance_flatten.tolist()]
        calculations['variance'] = variance

        #Stadard Deviation
        std_axis0 = b.std(axis=0)
        std_axis1 = b.std(axis=1)
        std_flatten = a.std()
        std = [std_axis0.tolist(), std_axis1.tolist(), std_flatten.tolist()]
        calculations['standard deviation'] = std

        #For Max
        max_axis0 = b.max(axis=0)
        max_axis1 = b.max(axis=1)
        max_flatten = a.max()
        ma = [max_axis0.tolist(), max_axis1.tolist(), max_flatten.tolist()]
        calculations['max'] = ma

        #For Min
        min_axis0 = b.min(axis=0)
        min_axis1 = b.min(axis=1)
        min_flatten = a.min()
        mi = [min_axis0.tolist(), min_axis1.tolist(), min_flatten.tolist()]
        calculations['min'] = mi

        #For Sum
        sum_axis0 = b.sum(axis=0)
        sum_axis1 = b.sum(axis=1)
        sum_flatten = a.sum()
        su = [sum_axis0.tolist(), sum_axis1.tolist(), sum_flatten.tolist()]
        calculations['sum'] = su
    else:
        raise ValueError("List must contain nine numbers.")


    return calculations