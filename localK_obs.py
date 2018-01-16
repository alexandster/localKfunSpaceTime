#import modules
import sys
import numpy as np
from datetime import datetime

#------------------------------------------------------------------------------------------------------------
#distance function
def dist(p1,p2):
    return [pow(pow(p1[0]-p2[0],2)+pow(p1[1]-p2[1],2),0.5), abs(p1[2] - p2[2])] 

#------------------------------------------------------------------------------------------------------------
#read sample points
inArr1 = np.loadtxt('files/grid.txt',delimiter=',')
leninArr1 = inArr1.shape[0]

#read data points
inArr2 = np.loadtxt('files/data.txt',delimiter=',')
leninArr2 = inArr2.shape[0]

headArr = np.zeros((leninArr1, 4))

#------------------------------------------------------------------------------------------------------------
#parameters
hs_max = 10		#maximum spatial bandwidth
hs_binsize = 2	#spatial bin size
ht_max = 4		#maximum temporal bandwidth (temporal bin size is 1)

#------------------------------------------------------------------------------------------------------------
#dimensions
dim1 = leninArr1			#number of sample points
dim2 = hs_max/hs_binsize	#number of spatial bins
dim3 = ht_max+1				#number of temporal bins

#------------------------------------------------------------------------------------------------------------
#initialize 3D zero-array: each sample point has counts for spatial and temporal bins
intArr = np.zeros((dim1, dim2, dim3))

#------------------------------------------------------------------------------------------------------------
#compute ST K-function
startTime = datetime.now()
a = 0	
while a < leninArr1:     #for each sample point
    #create header
    headArr[a][0] = a				#ID
    headArr[a][1] = inArr1[a][0]	#x
    headArr[a][2] = inArr1[a][1]	#y
    headArr[a][3] = inArr1[a][2]	#t

    b = 0						
    while b < leninArr2:      	#for each data point

        d = dist(inArr1[a],inArr2[b])
        
        if d[0] < hs_max and d[1] <= ht_max:

			#compute bin
            bwCount_s = int(d[0]/hs_binsize)	
            bwCount_t = int(d[1])				
            
            intArr[a][bwCount_s][bwCount_t] += 1	#increase count for sample point in corresponding bin
            #intArr[b][bwCount_s][bwCount_t] += 1  

        b += 1
    a += 1
    
#------------------------------------------------------------------------------------------------------------
#array manipulations

#compute cummulative sum along spatial bins
sumArr1 = np.cumsum(intArr, axis=1)

#compute cummulative sum along temporal bins
sumArr2 = np.cumsum(sumArr1, axis=2)

#reshape array
reArr = np.reshape(sumArr2,(dim1, dim2*dim3))

#local K-function: concatenate counts with header (contains ID and coordinates)
outArr = np.concatenate((headArr, reArr), axis=1)
np.savetxt('outputs/obs/localk.txt', outArr)

#global ST K-function: take sum over all local k functions
#sumArr3 = np.sum(sumArr2, axis=0)
#np.savetxt('outputs/obs/globalk.txt', sumArr3)


endTime = datetime.now()
runTime = endTime - startTime
print("execution time: ", runTime)















