import math
from random import randint

import pandas as pd
import numpy as np
from scipy import stats 


def variance(x,y):
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    var_x = np.var(x, ddof=1)
    var_y = np.var(y, ddof=1)

    # メトリクスの平均の分散は標本分散をnで割ったものに等しい
    return (var_x/mean_y**2 + var_y*mean_x**2/mean_y**3) / len(x)



def t_test(control, treatment):
    # 平均
    ctr_mean_control = control['ctr'].sum() / len(control)
    ctr_mean_treatment = treatment['ctr'].sum() / len(treatment)

    # 分散
    ctr_variance_control = variance(control['clicks'], control['views'])
    ctr_variance_treatment = variance(treatment['clicks'], treatment['views'])

    percent_change = ctr_mean_treatment - ctr_mean_control

    var = ctr_variance_control + ctr_variance_treatment
    z = percent_change / np.sqrt(var)
    p = stats.norm.sf(abs(z)) * 2

    result = {
        'ctr_mean_control': ctr_mean_control,
        'ctr_mean_treatment': ctr_mean_treatment,
        'percent_change': percent_change,
        'p-value': p
    }
    return pd.DataFrame(result, index=[0])


def main():
    # control ctr data
    view_control = [math.floor(x) for x in np.random.normal(100, 10, 10000)]
    click_control = [math.floor(views * np.random.normal(0.3, 0.1)) for views in view_control]
    control = pd.DataFrame({'clicks': click_control, 'views': view_control})
    control['ctr'] = control['clicks']/control['views']

    # treatment ctr data
    view_treatment = [math.floor(x) for x in np.random.normal(100, 10, 10000)]
    click_treatment = [math.floor(views * np.random.normal(0.31, 0.1)) for views in view_control]
    treatment = pd.DataFrame({'clicks': click_treatment, 'views': view_treatment})
    treatment['ctr'] = treatment['clicks'] / treatment['views']

    print(control)
    print(treatment)

    result = t_test(control, treatment)
    print(result)

if __name__ == '__main__':
    main()
