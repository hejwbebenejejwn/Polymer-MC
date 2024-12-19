import numpy as np
import pandas as pd
from polymer import Polymer
from utils import simulate


def main():
    Ns = [50, 100, 150, 200, 250]
    Ts = [1.65]
    multi_index = pd.MultiIndex.from_product([Ns, Ts], names=["N", "T"])
    df = pd.DataFrame(index=multi_index, data={"E": 0}, dtype=np.float64)
    for N in Ns:
        plm = Polymer(N)
        for T in Ts:
            df.loc[N, T] = simulate(round(16 * N**2.6), plm, T)
            df.to_csv("data.csv")


main()
