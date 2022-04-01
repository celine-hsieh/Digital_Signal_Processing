import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

σ2 = 2
σ7 = 7

def sigma(x):
    filter_size = int( 6 * x + 1 )				# 濾波器大小
    gauss = signal.gaussian( filter_size, x )	# 濾波器係數
    sum = np.sum( gauss )                   		# 正規化
    gauss = gauss / sum

    w, H = signal.freqz( gauss )
    mag = abs( H )

    plt.plot( w, mag )
    plt.xlabel( r'$\omega$' )
    plt.ylabel( 'Magnitude' )
    if x == 2:
        plt.savefig ('14_3_σ2.png')
    else :
        plt.savefig ('14_3_σ7.png')
    plt.show( )
    
sigma(2)
sigma(7)