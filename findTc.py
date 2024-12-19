import numpy as np
import pandas as pd
from polymer import Polymer
from utils import simulate


def main():
    # find critical temperature
    Ns = [50, 100]
    Ts = [
        0.1,
        0.3,
        0.5,
        0.7,
        0.9,
        1.1,
        1.3,
        1.5,
        1.55,
        1.6,
        1.65,
        1.7,
        1.75,
        1.8,
        2.0,
        2.2,
    ]
    multi_index = pd.MultiIndex.from_product([Ns, Ts], names=["N", "T"])
    df = pd.DataFrame(index=multi_index, data={"R2": 0}, dtype=np.float64)
    for N in Ns:
        plm = Polymer(N)
        for T in Ts:
            df.loc[N, T] = simulate(round(16 * N**2.6), plm, T, True)[1]
            df.to_csv("Tc.csv")


main()
