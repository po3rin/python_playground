import pandas as pd
import numpy as np
from random import randint
from scipy import stats 

click_control = [randint(0,20) for i in range(10000)]
view_control = [randint(1,60) for i in range(10000)]

click_treatment = [randint(0,21) for i in range(10000)]
view_treatment = [randint(1,60) for i in range(10000)]

control = pd.DataFrame({'click':click_control,'view':view_control})
treatment = pd.DataFrame({'click':click_treatment,'view':view_treatment})

def var_ratio(x,y):
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    var_x = np.var(x,ddof=1)
    var_y = np.var(y,ddof=1)
    cov_xy = np.cov(x,y,ddof=1)[0][1]
    result = (var_x/mean_x**2 + var_y/mean_y**2 - 2*cov_xy/(mean_x*mean_y))*(mean_x*mean_x)/(mean_y*mean_y*len(x))
    return result
    
def ttest(mean_control,mean_treatment,var_control,var_treatment):
    diff = mean_treatment - mean_control
    var = var_control+var_treatment
    stde = 1.96*np.sqrt(var)
    lower = diff - stde 
    upper = diff + stde
    z = diff/np.sqrt(var)
    p_val = stats.norm.sf(abs(z))*2

    result = {'mean_control':mean_control,
             'mean_experiment':mean_treatment,
             'var_control':var_control,
             'var_experiment':var_treatment,
             'difference':diff,
             'lower_bound':lower,
             'upper_bound':upper,
             'p-value':p_val}
    return pd.DataFrame(result,index=[0])

var_control = var_ratio(control['click'],control['view'])
var_treatment = var_ratio(treatment['click'],treatment['view'])
mean_control = control['click'].sum()/control['view'].sum()
mean_treatment = treatment['click'].sum()/treatment['view'].sum()

ttest(mean_control,mean_treatment,var_control,var_treatment)
