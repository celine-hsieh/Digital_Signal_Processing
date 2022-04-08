import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt

t = np.linspace( 0, 1, 200, endpoint = False )		
x = 10 * np.cos( 2 * np.pi * 5 * t ) + random.uniform ( -2, 10, 200 )
h = np.ones( 7 ) / 7
y = np.convolve( x, h, 'same' )

plt.figure( 1 )
plt.plot( t, x )
plt.xlabel( 't (second)' )
plt.ylabel( 'Amplitude' )

plt.savefig ('average_1.png')#儲存圖片

plt.figure( 2 )
plt.plot( t, y )
plt.xlabel( 't (second)' )
plt.ylabel( 'Amplitude' )

plt.savefig ('average_2.png')#儲存圖片
plt.show( )