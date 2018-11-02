#!/usr/bin/env bash
cd sandbox/rocky/tf/launchers
python algo_gym_stub.py --exp=test_exp --env_name=HRI_AirSim_Landing-v0 --restore_auto=False --overwrite=True --policy_batch_size=1
