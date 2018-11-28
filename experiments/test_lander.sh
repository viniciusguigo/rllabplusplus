#!/usr/bin/env bash
# delete previous logs
EXP_NAME='test-exp'
rm -rf ./data/local/$EXP_NAME*

# run experiment
cd sandbox/rocky/tf/launchers
python algo_gym_stub.py --exp=$EXP_NAME --env_name=LunarLanderContinuous-v2 --max_episode=1000 --batch_size=1000 --n_paralel=0 --restore_auto=False --overwrite=True --algo_name=actrpo

# plot results
cd ../../../../
python ./plotting/plot_exp.py