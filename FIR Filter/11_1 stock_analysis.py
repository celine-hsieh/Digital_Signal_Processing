import numpy as np
import csv
import scipy.signal as signal
import matplotlib.pyplot as plt

csvDataFile = open( '8299.TWO2019.csv' )
reader = csv.reader( csvDataFile )

data = []							# 讀取收盤價資料
for row in reader:				
	data.append( row[4] )	

price = []							# 讀取股價
for i in range( 1, len( data ) ):	
	price.append( eval( data[i] ) )

day = np.arange( len( price ) )
x = np.array( price )				# 轉換成陣列

b1 = np.ones( 5 ) / 5				# 週線
y1 = signal.lfilter ( b1, 1, x )

b2 = np.ones( 20 ) / 20				# 月線
y2 = signal.lfilter ( b2, 1, x )

plt.figure( 1 )						# 繪圖				
plt.plot( day, x, '-', fillstyle = 'bottom' )						
plt.xlabel( 'Day' )
plt.ylabel( 'Price' )
plt.axis( [ 0, len( price), 200, 400 ] )
plt.savefig ('11_1 figure 1.png')
		
plt.figure( 2 )					
plt.plot( day, x, '--', day, y1, '-' )	
plt.xlabel( 'Day' )
plt.ylabel( 'Price' )
plt.axis( [ 0, len( price), 200, 400 ] )
plt.savefig ('11_1 figure 2.png')

plt.figure( 3 )						
plt.plot( day, x, '--', day, y2, '-' )		
plt.xlabel( 'Day' )
plt.ylabel( 'Price' )
plt.axis( [ 0, len( price), 200, 400 ] )
plt.savefig ('11_1 figure 3.png')

plt.show()