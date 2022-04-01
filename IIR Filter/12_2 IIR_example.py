import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

n = np.array( [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ] )
x = np.array( [ 1, 2, 1, 2, 1, 0, 0, 0, 0, 0 ] )

b = np.array( [ 0.5, -0.5 ] )
a = np.array( [ 1, -0.8 ] )
y = signal.lfilter( b, a, x )

print( "x =", x )
print( "y =", y )

plt.figure( 1 )
plt.stem( n, x )
plt.xlabel( 'n' )
plt.ylabel( 'x[n]' )
plt.savefig ('12_2 figure(1).png')

plt.figure( 2 )
plt.stem( n, y )
plt.xlabel( 'n' )
plt.ylabel( 'y[n]' )
plt.savefig ('12_2 figure(2).png')

plt.show( )