import matplotlib.pyplot as plt
import scipy as sp
import numpy as np

from scipy.optimize import curve_fit
# import seaborn as sns
# sns.set()

def main():
    # bacterial density doubles in 20 hours
    x = [10, 20]
    t = [0, 20]

    # where D is the integration constant and C the original constant
    # ydata = curve_fit(lambda t, D, C: D * np.exp(C * t), x, t, p0=(10, 0.03), maxfev=100000)
    #
    time = np.arange(0, 25, 1)
    ydata = 10 * np.exp(0.03 * time)
    #
    print(ydata)
    #
    plt.plot(time, ydata)
    plt.scatter(t,x)
    plt.ylim(0, 100)
    plt.show()

if __name__ == '__main__':
    main()
