#import modules
import os, numpy as np, settings as sett
from datetime import datetime

# ------------------------------------------------------------------------------------------------------------
# load array
inArr = np.loadtxt('outputs/diff/obs_max.txt',delimiter=',')
outArr = inArr[:,:6]

# ------------------------------------------------------------------------------------------------------------
#initialize global variables
sett.init()

# ------------------------------------------------------------------------------------------------------------
# produce map of bandwidths
ht = 0
iMap = []
startTime = datetime.now()
while ht <=sett.ht_max:
    hs = sett.hs_binsize
    while hs <= sett.hs_max:
        iMap.append([hs,ht])
        hs += sett.hs_binsize
    ht += 1
# print(iMap)

# ------------------------------------------------------------------------------------------------------------
# find scale of greatest difference between obs and simulation envelope
for i,j in enumerate(np.argmin(inArr[:,4:],axis=1)):
    outArr[i][4] = iMap[j][0]
    outArr[i][5] = iMap[j][1]


# print(outArr)
np.savetxt('outputs/scale/scale_obs_max.txt', outArr, fmt='%1.2f',delimiter=',')	#difference between observed and upper envelope

endTime = datetime.now()
runTime = endTime - startTime
print("execution time: ", runTime)