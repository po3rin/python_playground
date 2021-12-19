import pandas as pd
import numpy as np
from random import randint
from scipy import stats


def var_delta(x, y):
  mean_x = np.mean(x)
  mean_y = np.mean(y)
  var_x = np.var(x, ddof=1)
  var_y = np.var(y, ddof=1)
  cov_xy = np.cov(x, y, ddof=1)[0][1]
  result = (var_x / mean_x**2 + var_y / mean_y**2 - 2 * cov_xy /
            (mean_x * mean_y)) * (mean_x * mean_x) / (mean_y * mean_y * len(x))
  return result


def ttest(mean_x, mean_y, var_x, var_y):
  diff = mean_y - mean_x
  var = var_x + var_y
  stde = 1.96 * np.sqrt(var)
  z = diff / np.sqrt(var)
  p_val = stats.norm.sf(abs(z)) * 2

  result = {'difference': diff, 'p-value': p_val}
  return pd.DataFrame(result, index=[0])


def main():
  click_control = [randint(0, 30) for i in range(10000)]
  view_control = [randint(1, 100) for i in range(10000)]

  click_treatment = [randint(0, 31) for i in range(10000)]
  view_treatment = [randint(1, 100) for i in range(10000)]

  control = pd.DataFrame({'click': click_control, 'view': view_control})
  treatment = pd.DataFrame({'click': click_treatment, 'view': view_treatment})

  # 分散
  var_c = var_delta(control['click'], control['view'])
  var_t = var_delta(treatment['click'], treatment['view'])

  # 平均
  mean_c = control['click'].sum() / control['view'].sum()
  mean_t = treatment['click'].sum() / treatment['view'].sum()

  result = ttest(mean_c, mean_t, var_c, var_t)
  print(result)


if __name__ == '__main__':
  main()
