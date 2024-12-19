import numpy as np
from polymer import Polymer
from sampler import Sampler
from tqdm import tqdm


def simulate(warmup, plm:Polymer, T, logr=False):
    Es=[]
    if logr:
        Rs=[]
    sampler=Sampler(plm, T)

    for i in tqdm(range(warmup),desc=f"warmup T={T}, N={plm.N}"):
        sampler.MC_step()

    checkstep=round(0.01*warmup)     
    for i in tqdm(range(10*warmup),desc=f"sample T={T}, N={plm.N}"):
        sampler.MC_step()
        if i%checkstep==0:
            Es.append(plm.E)
            if logr:
                Rs.append(plm.r2Gyration())

    if logr:
        return np.mean(Es), np.mean(Rs)

    return np.mean(Es)


def acc_simulate(warmup, plm: Polymer, T, logr=False):
    accumulative_Es = []
    if logr:
        Rs = []
    sampler = Sampler(plm, T)

    for i in tqdm(range(warmup), desc=f"warmup T={T}, N={plm.N}"):
        sampler.MC_step()

    checkstep = round(0.01 * warmup)
    accumulative_Es = []
    accumulative_Rs = []

    for i in tqdm(range(10 * warmup), desc=f"sample T={T}, N={plm.N}"):
        sampler.MC_step()
        if i % checkstep == 0:
            accumulative_Es.append(plm.E)
            if logr:
                Rs.append(plm.r2Gyration())

            # Compute accumulative means
            accumulative_Es.append(np.mean(accumulative_Es))
            if logr:
                accumulative_Rs.append(np.mean(Rs))

    if logr:
        return accumulative_Es, accumulative_Rs
    return accumulative_Es