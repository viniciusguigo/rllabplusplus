import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import argparse
sns.set(style='whitegrid', font_scale=1.25)

def main():
    # define data location
    data_addr = './data/local/test-exp/LunarLanderContinuous-v2-1000--ad-0-0--an-actrpo--asb-0--bc-linear--bhs-32x32--gl-0-97--ksb-0--phn-tanh--phs-100x50--pon-None--psl-True--qbs-64--qhn-relu--qhs-100x100--qlr-0-001--qmr-0-0--qrp-0-0--qut-True--sr-1-0--ss-0-01--ur-1-0--s-1'

    # load data from progress log
    data = np.genfromtxt('{}/progress.csv'.format(data_addr), delimiter=',', skip_header=True)
    labels = np.genfromtxt('{}/progress.csv'.format(data_addr), dtype=str, delimiter=',', max_rows=1)

    # find returns on progress.csv file
    avg_return_idx = np.where([label == 'AverageReturn' for label in labels])[0][0]

    # plot them
    plt.figure()
    plt.ylabel(labels[avg_return_idx])
    plt.xlabel('Iteration')
    plt.plot(data[:,avg_return_idx])
    plt.xlim([0,data.shape[0]])
    plt.tight_layout()
    plt.legend()
    plt.show()

if __name__ == '__main__':
    main()