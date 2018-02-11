# settings.py
def init():
    global hs_binsize, hs_numbins, hs_max, ht_binsize, ht_numbins, ht_max
    hs_binsize = 10                     # spatial bin size
    hs_numbins = 4                      # number of spatial bins
    hs_max = hs_binsize * hs_numbins    # maximum spatial bandwidth
    ht_binsize = 1                      # temporal bin size
    ht_numbins = 4                      # number of temporal bins
    ht_max = ht_binsize * ht_numbins    # maximum spatial bandwidth


