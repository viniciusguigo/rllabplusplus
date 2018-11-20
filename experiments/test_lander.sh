#!/usr/bin/env bash
cd sandbox/rocky/tf/launchers
python algo_gym_stub.py --exp=test_exp --env_name=LunarLanderContinuous-v2 --max_episode=1 --batch_size=1
