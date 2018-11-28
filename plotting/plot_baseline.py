#!/usr/bin/env python
"""plot_baseline.py:
Plots comparison between different algorithms solving the 
LunarLanderContinuous-v2 environment.
"""

__author__ = "Vinicius Guimaraes Goecks"
__version__ = "0.0.1"
__date__ = "November 27, 2018"

# import
import matplotlib.pyplot as plt
import numpy as np
import sys
import seaborn as sns
sns.set(style='whitegrid', font_scale=1.25)


def plot_history(fig, ax, avg_return, n_samples, run_id_label):
    """Plot history results (iterations, mean reward) using Matplotlib.
    """
    # average data
    avg = np.average(avg_return, axis=0)
    std_dev = np.std(avg_return, axis=0)
    steps = np.arange(n_samples)

    # plot avg
    ax.plot(steps, avg, alpha=.75,label=run_id_label)

    # print std dev areas
    ax.fill_between(steps, avg+std_dev, avg-std_dev, alpha=0.5)#, facecolor='green', alpha=0.35)


def process_avg(fig, ax, run_id, run_id_label, n_seeds=1):
    """Load files, calculate average, std dev, plot, and save figure.
    """
    # load first file (seed == 1)
    data = np.genfromtxt('{}{}/progress.csv'.format(run_id,1), delimiter=',', skip_header=True)
    n_samples = data.shape[0]
    labels = np.genfromtxt('{}{}/progress.csv'.format(run_id,1), dtype=str, delimiter=',', max_rows=1)

    # find returns on progress.csv file
    avg_return_idx = np.where([label == 'AverageReturn' for label in labels])[0][0]
    avg_return = data[:,avg_return_idx].reshape(1,n_samples)

    # loop for different seeds
    for i in range (2,n_seeds+1):
        # load data from progress log
        temp_data = np.genfromtxt('{}{}/progress.csv'.format(run_id,i), delimiter=',', skip_header=True)
        temp_labels = np.genfromtxt('{}{}/progress.csv'.format(run_id,i), dtype=str, delimiter=',', max_rows=1)

        # find returns on progress.csv file
        temp_avg_return_idx = np.where([label == 'AverageReturn' for label in temp_labels])[0][0]
        temp_avg_return = temp_data[:,temp_avg_return_idx].reshape(1,n_samples)

        # append to data of first file
        avg_return = np.vstack((avg_return, temp_avg_return))

    # plot
    plot_history(fig, ax, avg_return, n_samples, run_id_label)

if __name__ == '__main__':
    # setup figure
    save_pic = True
    name_pic = './plotting/baseline.png'

    # plot rewards
    fig, ax = plt.subplots(1)
    ax.set_xlabel("Episode")
    ax.set_ylabel("Average Return")

    # plot data
    ## IPG
    run_id = './data/local/lander-ipg/LunarLanderContinuous-v2-1000--ad-0-0--an-actrpo--asb-0--bc-linear--bhs-32x32--gl-0-97--ksb-0--phn-tanh--phs-100x50--pon-None--psl-True--qbs-64--qhn-relu--qhs-100x100--qlr-0-001--qmr-0-0--qrp-0-0--qut-True--sr-1-0--ss-0-01--ur-1-0--s-'
    run_id_label = 'IPG'
    process_avg(fig, ax, run_id, run_id_label, n_seeds=3)

    ## QPROP
    run_id = './data/local/lander-qprop/LunarLanderContinuous-v2-1000--an-qprop--bc-linear--bhs-32x32--gl-0-97--ksb-0--phn-tanh--phs-100x50--pon-None--psl-True--qbs-64--qeo-ones--qhn-relu--qhs-100x100--qlr-0-001--qmr-0-0--qrp-0-0--qut-True--sb-0--sr-1-0--ss-0-01--ur-1-0--s-'
    run_id_label = 'Q-Prop'
    process_avg(fig, ax, run_id, run_id_label, n_seeds=3)

    ## TRPO
    run_id = './data/local/lander-trpo/LunarLanderContinuous-v2-1000--an-trpo--bc-linear--bhs-32x32--gl-0-97--ksb-0--phn-tanh--phs-100x50--pon-None--ss-0-01--s-'
    run_id_label = 'TRPO'
    process_avg(fig, ax, run_id, run_id_label, n_seeds=3)

    # save/show pic
    plt.legend()
    plt.tight_layout()
    if save_pic:
        plt.savefig(name_pic, dpi=300)    
    plt.show()
        
