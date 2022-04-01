import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
from matplotlib import patches
from matplotlib.markers import MarkerStyle

def zplane(z, p):
	fig = plt.figure( )
	ax = plt.subplot( 1, 1, 1 )
	
	unit_circle = patches.Circle( ( 0,0 ), radius = 1, fill = False, color = 'black', ls = 'dashed' )
	ax.add_patch( unit_circle )
	plt.axvline( 0, color = 'black' )
	plt.axhline( 0, color = 'black' )
	plt.xlim( ( -2, 2 ) )
	plt.ylim( ( -1.5, 1.5 ) )
	plt.grid( )

	plt.plot( z.real, z.imag, 'ko', fillstyle = 'none', ms = 12 )
	plt.plot( p.real, p.imag, 'kx', fillstyle = 'none', ms = 12 )
	return fig

def main( ):
	
	# 10-1 (a)
	a1 = np.array( [ 1, -0.2 ] )
	a2 = np.array( [ 1, -2, 1.25 ] )

	z, p, k = signal.tf2zpk( a1, a2 )

	print( "Zeros =", z )
	print( "Poles =", p )
	print( "Gain =", k )

	zplane( z, p )
	plt.savefig ('10-1 (a).png')
	plt.show( )

	# 10-1 (b)
	b1 = np.array( [ 1, -0.1 ] )
	b2 = np.array( [ 1, -0.4, 0.2 ] )

	z, p, k = signal.tf2zpk( b1, b2 )

	print( "Zeros =", z )
	print( "Poles =", p )
	print( "Gain =", k )

	zplane( z, p )
	plt.savefig ('10-1 (b).png')
	plt.show( )

	# 10-1 (c)
	b1 = np.array( [ 1, -0.5 ] )
	b2 = np.array( [ 1, -0.1, 1, -0.1 ] )

	z, p, k = signal.tf2zpk( b1, b2 )

	print( "Zeros =", z )
	print( "Poles =", p )
	print( "Gain =", k )

	zplane( z, p )
	plt.savefig ('10-1 (c).png')
	plt.show( )

main( )