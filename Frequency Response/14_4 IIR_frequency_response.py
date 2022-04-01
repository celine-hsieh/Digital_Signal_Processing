import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

α1 = 0.1
α2 = 0.4
α3 = 0.7

def alpha(x):
    b = np.array( [ 1 - x, 1 - x ] )
    a = np.array( [ 2, -2 * x ] )
    w, H = signal.freqz( b, a )
    H0 = abs( H )

    plt.figure( 1 )
    plt.plot( w, H0 )
    plt.xlabel( r'$\omega$' )
    plt.ylabel( 'Magnitude' )
    if x == 0.1:
        plt.savefig ('14_4_α 0.1.png')
    elif x == 0.4:
        plt.savefig ('14_4_α 0.4.png')
    else :
        plt.savefig ('14_4_α 0.7.png')
        
    plt.show( )
    
alpha(α1)
alpha(α2)
alpha(α3)