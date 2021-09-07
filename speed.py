import os
import glob
import timeit

def walk():
    pys = []
    for p, d, f in os.walk('.'):
        for file in f:
            if file.endswith('.doc'):
                pys.append(file)
    return pys

def iglob():
    pys = []
    for file in glob.iglob('**/*', recursive=True):
        if file.endswith('.doc'):
            pys.append(file)
    return pys

def iglob2():
    pys = []
    for file in glob.iglob('**/*.doc', recursive=True):
        pys.append(file)
    return pys

# I also tried pathlib.Path.glob but it was slow and error prone, sadly

#timeit(iglob2)
#3.95 s ± 13 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

#%timeit iglob()
#5.01 s ± 19.2 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

#%timeit iglob2()
#4.36 s ± 34 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
