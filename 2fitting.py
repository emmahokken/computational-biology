import matplotlib.pyplot as plt
import scipy as sp
import numpy as np
import pandas as pd

from sympy.solvers import solve
from sympy import Symbol

from scipy.optimize import curve_fit
import seaborn as sns
sns.set()

def main():
    df = pd.read_csv('data_for_fitting.csv', names=['x', 'y'])

    # plot datapoints
    plt.scatter(df['x'], df['y'], label='Data points')

    # linear fit
    p_0 = np.array([0, 1])
    A, B = curve_fit(linear_fit, df['x'], df['y'], p0=p_0, maxfev=10000)[0]

    # make and plot the line
    x = np.arange(0, 3, 0.1)
    y = linear_fit(x, A, B)

    plt.plot(x, y, label='linear fit: $' + str(round(A, 2)) + '\cdot x ' + str(round(B, 2)) + '$', color='purple')

    # exponential fit
    p_0 = np.array([1, 0])
    A, B = curve_fit(exponential_fit, df['x'], df['y'], p0=p_0, maxfev=10000)[0]

    # make and plot the line
    x = np.arange(0, 3, 0.1)
    y = exponential_fit(x, A, B)

    plt.plot(x, y, label='exponential fit: $' + str(round(A, 2)) + '\cdot e^{' + str(round(B, 2)) + '\cdot x}$', color='green')

    # show the plot
    plt.title('Fitting linear or exponential to growth data')
    plt.xlabel('Time')
    plt.ylabel('Bacteria')

    plt.xlim(0, 3)
    plt.ylim(-10, 80)
    plt.legend()
    plt.savefig('results/fitting.png')


def exponential_fit(x, A, B):
    return A * np.exp(B * x)

def linear_fit(x, A, B):
    return A * x + B

if __name__ == '__main__':
    main()
