import matplotlib.pyplot as plt
import scipy as sp
import numpy as np

from sympy.solvers import solve
from sympy import Symbol

from scipy.optimize import curve_fit
import seaborn as sns
sns.set()

def main():
    # bacterial density doubles in 20 hours
    # use y instead of x because otherwise it confuses me
    y0 = 10
    y = [y0, 2*y0]

    t = [0, 20]

    # initial guess: at t = 0, A * e^(C * x) = 10
    p_0 = np.array([10, 0])

    # curve fit uses least squares method
    A, C = curve_fit(integral, t, y, p0=p_0, maxfev=10000)[0]

    # create the actual line
    time = np.arange(0, 30, 1)
    y_data = integral(time, A, C)

    # plot it
    plt.title('Bacterial growth')
    plt.ylabel('Amount of Bacteria/ml')
    plt.xlabel('Time (hrs)')
    plt.plot(time, y_data, color='blue', label='$y = ' + str(round(A, 2)) + '\cdot e^{' + str(round(C, 2)) + '\cdot x}$')
    plt.scatter(t,y, color='red', label='Data points')
    plt.legend()
    plt.savefig('results/bacterial_growth.png')

    t = Symbol('t')

    # # solve for density eight times original value
    # TODO HELP: 'Symbol' object has no attribute 'exp' really sympy?
    y = y0 * 8
    print(solve( A * t**2 - y, t))

    # # solve assumes equation is equaled to zero
    # answer = solve(A * np.exp(C * t) - y, t)
    # print(answer)

    # solve for density ten times original value
    y = y0 * 10

def integral(t, A, C):
    """ This is a function that contains the Integral of the ODE that is given
        in the assignment. """

    # where A is the integration constant and C the original constant
    return A * np.exp(C * t)

if __name__ == '__main__':
    main()
