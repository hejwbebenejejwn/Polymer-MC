import numpy as np
from polymer import Polymer
from utils import acc_simulate
import matplotlib.pyplot as plt


def main():
    Ns = [50]
    Ts = [2.0]

    for N in Ns:
        plm = Polymer(N)
        for T in Ts:
            accumulative_Es, accumulative_Rs = acc_simulate(
                round(40 * N**2.6), plm, T, True
            )
            x = np.arange(len(accumulative_Es))

            fig, ax1 = plt.subplots()
            # Plot accumulative_Es on the first y-axis
            ax1.plot(
                x, accumulative_Es, "g-", label="E"
            )  # Green line for accumulative_Es
            ax1.set_xlabel("X-axis")
            ax1.set_ylabel("E", color="g")
            ax1.tick_params(axis="y", labelcolor="g")

            # Create a second y-axis
            ax2 = ax1.twinx()

            # Plot R2 on the second y-axis
            ax2.plot(x, accumulative_Rs, "b-", label="R2/N")  # Blue line for R2
            ax2.set_ylabel("R2/N", color="b")
            ax2.tick_params(axis="y", labelcolor="b")

            # Show the plot
            plt.title("Convergence of E and R2/N")
            plt.savefig(f"convergence_T={T}_N={N}.png")
            plt.close()


main()
