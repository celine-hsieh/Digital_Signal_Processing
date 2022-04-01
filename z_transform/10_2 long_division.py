import numpy as np
	
# 10-2 (a)
b = np.array( [ 1, 1, -3, -1, 2 ] )
a = np.array( [ 1, -2, 1, 0, 0 ] )

M = b.size
N = a.size
x = np.zeros( M )
x[0] = b[0] / a[0]
for n in range( 1, M ):
	sum = 0
	k = n
	if n > N:
		k = N
	for i in range( 1, k + 1 ):
		sum = sum + x[n-i] * a[i]
	x[n] = ( b[n] - sum ) / a[0]

print( x )

# 10-2 (b)
b = np.array( [ 1, 3, 2, -1, -1 ] )
a = np.array( [ 1, 2, 1, 0, 0 ] )

M = b.size
N = a.size
x = np.zeros( M )
x[0] = b[0] / a[0]
for n in range( 1, M ):
	sum = 0
	k = n
	if n > N:
		k = N
	for i in range( 1, k + 1 ):
		sum = sum + x[n-i] * a[i]
	x[n] = ( b[n] - sum ) / a[0]

print( x )