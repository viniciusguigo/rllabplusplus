#!/usr/bin/env bash
# Evaluate multiple algorithms in the LunarLanderContinuous-v2 env
# delete previous logs
EXP_NAME='lander-qprop2'
rm -rf ./data/local/$EXP_NAME*

# run experiments (3 seeds each)
cd sandbox/rocky/tf/launchers
python algo_gym_stub.py --exp=$EXP_NAME --env_name=LunarLanderContinuous-v2 --max_episode=5000 --batch_size=200 --n_paralel=0 --restore_auto=False --overwrite=True --algo_name=qprop --seed=1
python algo_gym_stub.py --exp=$EXP_NAME --env_name=LunarLanderContinuous-v2 --max_episode=5000 --batch_size=200 --n_paralel=0 --restore_auto=False --overwrite=True --algo_name=qprop --seed=2
python algo_gym_stub.py --exp=$EXP_NAME --env_name=LunarLanderContinuous-v2 --max_episode=5000 --batch_size=200 --n_paralel=0 --restore_auto=False --overwrite=True --algo_name=qprop --seed=3

# # delete previous logs
# cd ../../../../
# EXP_NAME='lander-ipg2'
# rm -rf ./data/local/$EXP_NAME*

# # run experiments (3 seeds each)
# cd sandbox/rocky/tf/launchers
# python algo_gym_stub.py --exp=$EXP_NAME --env_name=LunarLanderContinuous-v2 --max_episode=5000 --batch_size=200 --n_paralel=0 --restore_auto=False --overwrite=True --algo_name=actrpo --seed=1
# python algo_gym_stub.py --exp=$EXP_NAME --env_name=LunarLanderContinuous-v2 --max_episode=5000 --batch_size=200 --n_paralel=0 --restore_auto=False --overwrite=True --algo_name=actrpo --seed=2
# python algo_gym_stub.py --exp=$EXP_NAME --env_name=LunarLanderContinuous-v2 --max_episode=5000 --batch_size=200 --n_paralel=0 --restore_auto=False --overwrite=True --algo_name=actrpo --seed=3

# # delete previous logs
# cd ../../../../
# EXP_NAME='lander-trpo2'
# rm -rf ./data/local/$EXP_NAME*

# # run experiments (3 seeds each)
# cd sandbox/rocky/tf/launchers
# python algo_gym_stub.py --exp=$EXP_NAME --env_name=LunarLanderContinuous-v2 --max_episode=5000 --batch_size=200 --n_paralel=0 --restore_auto=False --overwrite=True --algo_name=trpo --seed=1
# python algo_gym_stub.py --exp=$EXP_NAME --env_name=LunarLanderContinuous-v2 --max_episode=5000 --batch_size=200 --n_paralel=0 --restore_auto=False --overwrite=True --algo_name=trpo --seed=2
# python algo_gym_stub.py --exp=$EXP_NAME --env_name=LunarLanderContinuous-v2 --max_episode=5000 --batch_size=200 --n_paralel=0 --restore_auto=False --overwrite=True --algo_name=trpo --seed=3