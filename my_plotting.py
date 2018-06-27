import matplotlib.pyplot as plt
from numpy import array
from numpy import linspace, cos, sin, pi

def plot_guy(x, y, frown=False, **plot_args):
    an = array(linspace(0,2*pi,100))
    head, = plt.plot(cos(an)+x, sin(an)+y + 5, **plot_args)
    body, = plt.plot(array([0,0])+x, array([4,2])+y, **plot_args)
    legs, = plt.plot(array([-1,0,1])+x, array([0,2,0])+y, **plot_args)
    arms, = plt.plot(array([-1.5,0,1.5])+x, array([3.5,3,3.5])+y, **plot_args)
    eye1, = plt.plot(.2*cos(an)-.35 + x, .2*sin(an) + 5.2 + y, **plot_args)
    eye2, = plt.plot(.2*cos(an)+.35 + x, .2*sin(an) + 5.2 + y, **plot_args)
    if frown:
        mouth, = plt.plot(cos(an[15:35]) + x, sin(an[15:35]) + 3.8 + y, **plot_args)
    else:
        mouth, = plt.plot(cos(an[65:85]) + x, sin(an[65:85]) + 5.4 + y, **plot_args)
