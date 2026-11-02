import math
import numpy as np
import matplotlib.pyplot as plt

# task 1
def approx_ln (x,n):
    if x > 0:
        a = (1+x) / 2
        g = math.sqrt(x)
        
        for i in range(n):
            a_new = (a + g) / 2
            g_new = math.sqrt (a_new * g) 
            a = a_new
            g = g_new
        return (x-1) / a
    else:
        return "x must be greater than 0"

print (approx_ln(2, 10)) 
        
# task 2

# graph 1

def graph_1 ():
    x_list = np.linspace (0.1, 21, 100) 
    y_list = [np.log(x) for x in x_list]
    y_approx = [approx_ln(x, 2) for x in x_list]
    plt.plot (x_list, y_list, label = "ln(x)")
    plt.plot (x_list, y_approx, label = "approx_ln(x)")
    plt.title ("Graph of ln(x) and its approximation")
    plt.xlabel ("x")
    plt.ylabel ("y")
    plt.legend ()
    plt.show ()
print (graph_1 ())

# graph 2 
def graph_2 ():
    x_list = np.linspace (0.1, 21, 100) 
    y_list = [np.log(x) for x in x_list]
    y_approx = [approx_ln(x, 20) for x in x_list]
    difference_list = []
    for i in range (len(x_list)):
        difference = y_list[i] - y_approx[i]
        difference_list.append (difference)

    plt.plot (x_list, difference_list)
    plt.title ("Difference between ln(x) and its approximation")
    plt.xlabel ("x")
    plt.ylabel ("Difference")
    plt.show()
print (graph_2())

# task 3

def task_3 ():
    x = 1.41
    c_list = list(range(1,21))
    error_list = []
    for i in c_list:
        error = abs(np.log(x) - approx_ln(x,i))
        error_list.append(error)
    plt.plot (c_list, error_list)
    plt.title ("Absolute error in the approximation of ln(x)")
    plt.xlabel ("Iterations")
    plt.ylabel ("Absolute error")
    plt.xlim (0, 20)
    plt.yscale ("log")
    plt.show()
print (task_3())

# task 4

def fast_approx_ln (x,n):
    if x > 0:
        a = (1+x) / 2
        g = math.sqrt(x)
        a_list = [a]
        for i in range(n):
            a_new = (a + g) / 2
            g_new = math.sqrt (a_new * g) 
            a = a_new
            g = g_new
            a_list.append (a)
        d_list = [a_list]
        for k in range (1, n+1):
            d_new = [0] * (n+1)
            for i in range (k, n+1):
                d_new [i] = (
                    d_list [k-1][i] - 4**(-k) * d_list[k-1][i-1]
                ) / (1-4**(-k))

            d_list.append (d_new)
        return (x-1) / d_list [n][n]
    else:
        return "x must be greater than 0"
print (fast_approx_ln (1,20))

# task 5

x_list = np.linspace (0.1, 20, 1650)
for n in range (2,7):
    error_list = []

    for x in x_list:
        error = abs(np.log(x) - fast_approx_ln (x,n))
        error_list.append(error)

    plt.scatter (x_list, error_list, label ="iteration" + str(n), s=10)
plt.yscale ("log")
plt.title ("Error behavior of the accelerated Carlsson method for the log")
plt.xlabel("x")
plt.ylabel("error")
plt.xlim(0,20)
plt.ylim(10**(-19), 10**(-5))
plt.legend(loc="upper left") 
plt.show()
