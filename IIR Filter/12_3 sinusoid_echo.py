import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

fs = 100										# 取樣率
t = np.linspace( 0, 1, fs, endpoint = False )	# 定義時間陣列
x = np.exp( -t ) * np.sin( 2 * np.pi * 5 * t )  # 產生淡出弦波
x = np.pad( x, ( 0, fs * 4 ), 'constant' )		# 補零

b = np.array( [ 1 ] )							# 定義b陣列

num_echos = 5									# 迴音次數
a = np.zeros( fs * num_echos )					# 定義a陣列
for i in range( num_echos ):
	a[i * fs] = 1 - i / num_echos

y = signal.lfilter( x, b, a )					# IIR濾波器

plt.figure( 1 )									# 繪圖
plt.plot( x )								
plt.xlabel( 'n' )
plt.ylabel( 'Amplitude' )

plt.figure( 2 )
plt.plot( y )								
plt.xlabel( 'n' )
plt.ylabel( 'Amplitude' )

plt.show( )