import numpy as np
from numpy.fft import fft, fftshift, fftfreq
import matplotlib.pyplot as plt

t = np.linspace( 0, 1, 1000, endpoint = False )
x = np.cos( 2 * np.pi * 200 * t ) 

f = fftshift( fftfreq( 1000, 0.001 ) )
X = fftshift( fft( x ) ) 
Xm = abs( X )  
X_phase = np.angle( X )

plt.plot( f, Xm )
plt.xlabel( 'f' )
plt.ylabel( 'Magnitude' )
plt.savefig ('13_2(a)_Magnitude.png')

plt.figure( 2 )
plt.stem( f, X_phase )
plt.xlabel( 'f' )
plt.ylabel( 'Phase' )
plt.savefig ('13_2(a)_phase.png')

plt.show( )