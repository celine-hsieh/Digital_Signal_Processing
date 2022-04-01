import numpy as np
import scipy.signal as signal

x = np.array( [ 1, 2, 4, 3, 2, 1, 1 ] )
b = np.ones( 3 ) / 3
y = signal.lfilter( b, 1, x )

print( "x =", x )
print( "y =", y )