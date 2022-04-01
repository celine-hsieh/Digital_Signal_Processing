import numpy as np
from numpy.fft import fft, ifft
import scipy.signal as signal
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

xa = np.array( [ 1, 4, 3, 2 ] )
na = np.array( [ 0, 1, 2, 3 ] )

Xa = fft( xa )
X_mag = abs ( Xa )
#X_phase = mlab.phase_spectrum ( Xa )
X_phase = np.angle( Xa )

print( "x =", xa )
print( "X =", Xa )
print( "Magnitude of X =", X_mag )

'''plt.figure( 1 )
plt.stem( na, xa )
plt.xlabel( 'n' )
plt.ylabel( 'x[n]' )'''

plt.figure( 1 )
plt.stem( na, X_mag )
plt.xlabel( 'k' )
plt.ylabel( '|X[k]|' )
plt.savefig ('13_1(a)_magnitude.png')
#plt.phase_spectrum(X_mag, color ='green')

plt.figure( 2 )
plt.stem( na, X_phase )
plt.xlabel( 'ω' )
plt.ylabel( 'Ø' )
plt.savefig ('13_1(a)_phase.png')

plt.show( )

#-----------------------------------------------------
xb = np.array( [ 1, 2, 3, 4, 1, 2, 3, 4 ] )
nb = np.array( [ 0, 1, 2, 3, 4, 5, 6, 7 ] )

Xb = fft( xb )
X_mag = abs ( Xb )
X_phase = np.angle( Xb )

print( "x =", xb )
print( "X =", Xb )
print( "Magnitude of X =", X_mag )

plt.figure( 1 )
plt.stem( nb, X_mag )
plt.xlabel( 'k' )
plt.ylabel( '|X[k]|' )
plt.savefig ('13_1(b)_magnitude.png')

plt.figure( 2 )
plt.stem( nb, X_phase )
plt.xlabel( 'ω' )
plt.ylabel( 'Ø' )
plt.savefig ('13_1(b)_phase.png')

plt.show( )

#-----------------------------------------------------
xc = np.array( [ 1, 2, 3, 4, 3, 2, 1, 2 ] )
nc = np.array( [ 0, 1, 2, 3, 4, 5, 6, 7 ] )

Xc = fft( xc )
X_mag = abs ( Xc )
X_phase = np.angle( Xc )

print( "x =", xc )
print( "X =", Xc )
print( "Magnitude of X =", X_mag )

plt.figure( 1 )
plt.stem( nc, X_mag )
plt.xlabel( 'k' )
plt.ylabel( '|X[k]|' )
plt.savefig ('13_1(c)_magnitude.png')

plt.figure( 2 )
plt.stem( nc, X_phase )
plt.xlabel( 'ω' )
plt.ylabel( 'Ø' )
plt.savefig ('13_1(c)_phase.png')

plt.show( )