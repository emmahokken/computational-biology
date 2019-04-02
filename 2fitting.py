import matplotlib.pyplot as plt
import scipy as sp
import numpy as np

import seaborn as sns
sns.set()

def main():
    # bacterial density doubles in 20 hours

    x0 = [10]
    x = [10, 20]

    # create a vector with points t
    t = np.linspace(0,40, 40)

    x = sp.integrate.odeint(growth, x0, t)
    bacterias = x[:,0]
    plt.plot(t, bacterias, label='growth')
    plt.show()

    print(bacterias[0], bacterias[20])

def growth(x, t):
    # try a random constant
    C = 0.05

    x = x[0]
    dxdt = C * x

    return [dxdt]

if __name__ == '__main__':
    main()
