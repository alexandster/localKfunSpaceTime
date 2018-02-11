Computes local space-time k-function.

Required modules: 
numpy

Relevant Literature: 
Hohl, A., Zheng, M., Tang, W., Delmelle, E., & Casas, I. (2017). Spatiotemporal Point Pattern Analysis Using Ripley’s K Function. In: Karimi, H. A. & Karimi, B. (Eds.) Geospatial Data Science: Techniques and Applications. Taylor & Francis.

Scripts:
localK_obs.py - Computes observed local space-time k function. 
localK_sim.py - Computes local space-time k function from n simulated datasets. 
results_collect.py - Gathers results from observed and simulated local k functions, computes simulation envelopes, and differences between observed and simulated.
maxClustScale.py: Finds the spatial and temporal bandwidths at which clustering is strongest.
settings.py: Parameters

data files:
files/data.txt - Mock dataset (oberved) for illustration purposes. Includes 100 (x, y, t) tuples.
files/grid.txt - Grid of points for which the  local space-time k-function is evaluated.
files/MC/data_sim1.txt, data_sim2.txt, data_sim3.txt - Mock dadtasets (simulated).
output files:
outputs/obs/localk.txt - observed local k function
outputs/sim/localk1.txt, localk2.txt, localk3.txt - simulated local k functions
outputs/diff/obs_max.txt - difference between observed k function and upper simualtion envelope.
outputs/diff/obs_min.txt - difference between observed k function and lower simualtion envelope.
outputs/scale/scale_obs_max.txt - the spatial and temporal bandwidths at which clustering is strongest.
 
