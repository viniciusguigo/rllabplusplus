#!/usr/bin/env bash
# Evaluate multiple algorithms in the LunarLanderContinuous-v2 env
# delete previous logs
EXP_NAME='lander_qprop'
rm -rf ./data/local/$EXP_NAME*

# run experiments (3 seeds each)
cd sandbox/rocky/tf/launchers
python algo_gym_stub.py --exp=$EXP_NAME --env_name=LunarLanderContinuous-v2 --max_episode=1000 --batch_size=1000 --n_paralel=0 --restore_auto=False --overwrite=True --algo_name=qprop --seed=1
python algo_gym_stub.py --exp=$EXP_NAME --env_name=LunarLanderContinuous-v2 --max_episode=1000 --batch_size=1000 --n_paralel=0 --restore_auto=False --overwrite=True --algo_name=qprop --seed=2
python algo_gym_stub.py --exp=$EXP_NAME --env_name=LunarLanderContinuous-v2 --max_episode=1000 --batch_size=1000 --n_paralel=0 --restore_auto=False --overwrite=True --algo_name=qprop --seed=3
