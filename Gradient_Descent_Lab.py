import math,copy
import numpy as numpy
import matplotlib.pyplot as plt
plt.style.use('./deeplearning.mplstyle')
from lab_utils_uni import plt_house_x, plt_contour_wgrad,plt_divergence,plt_gradients


#adding a problem statement
#two-houses with data (1,300) and (2,500)

x_train=np.array([1.0,2.0])
y_train=np.array([300.0,500.0])