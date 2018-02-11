#import modules
import os, numpy as np
from datetime import datetime

#read observed local k function
headArr = np.loadtxt("outputs/obs/localk.txt",delimiter=",",usecols = (0,1,2,3))
obsArr = np.delete(np.loadtxt("outputs/obs/localk.txt",delimiter=","),(0,1,2,3),1)

#initialize zero array and infinity array
maxArr = np.zeros(obsArr.shape)
minArr = np.full(obsArr.shape, np.inf)

#find simulation envelopes
i = 1
startTime = datetime.now()
while i<=len(os.listdir('outputs/sim')):

    simArr = np.delete(np.loadtxt("outputs/sim/localk" + str(i) + ".txt",delimiter=","),(0,1,2,3),1)

    maxArr1 = np.amax(np.stack([maxArr, simArr]),axis=0)
    maxArr = maxArr1

    minArr1 = np.amin(np.stack([minArr, simArr]),axis=0)
    minArr = minArr1

    i += 1

#compute differences between observed local k function and simulation envelopes
np.savetxt('outputs/diff/obs_max.txt', np.concatenate((headArr, np.subtract(obsArr,maxArr)), axis=1),fmt='%1.2f',delimiter=',')	#difference between observed and upper envelope
np.savetxt('outputs/diff/obs_min.txt', np.concatenate((headArr, np.subtract(obsArr,minArr)), axis=1),fmt='%1.2f',delimiter=',')   #difference between observed and lower envelope

endTime = datetime.now()
runTime = endTime - startTime
print("execution time: ", runTime)
