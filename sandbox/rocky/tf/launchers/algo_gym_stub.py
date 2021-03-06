from sandbox.rocky.tf.launchers.launcher_utils import FLAGS, get_env_info, get_annotations_string
from sandbox.rocky.tf.launchers.launcher_stub_utils import get_env, get_policy, get_baseline, get_qf, get_es, get_algo
from rllab.misc.instrument import run_experiment_lite
from rllab import config
import os.path as osp
import sys
import tensorflow as tf
from copy import deepcopy
import numpy as np


def set_experiment(mode="local", keys=None, params=dict()):
    flags = FLAGS.__flags
    # VGG: fix error handling flags after Tensorflow 1.4
    for name in flags.keys():
        flags[name] = flags[name].value
        print('{}: {}'.format(name, flags[name]))
    flags = deepcopy(flags)

    for k, v in params.items():
        print('Modifying flags.%s from %r to %r'%(
            k, flags[k], v))
        flags[k] = v

    n_episodes = flags["max_episode"] # max episodes before termination
    info, _ = get_env_info(**flags)
    max_path_length = 200 #info['horizon'] #200 **VGG: TODO: fix Gym env to include this

    print('n_episodes: ', n_episodes)
    print('max_path_length: ', max_path_length)
    print('flags[batch_size]: ', flags['batch_size'])
    print('flags[obs_space]: ', info['obs_space'])

    n_itr = int(np.ceil(float(n_episodes*max_path_length)/flags['batch_size']))

    exp_prefix='%s'%(flags["exp"])
    exp_name=get_annotations_string(keys=keys, **flags)
    if flags["normalize_obs"]: flags["env_name"] += 'norm'
    exp_name = '%s-%d--'%(flags["env_name"], flags["batch_size"]) + exp_name
    log_dir = config.LOG_DIR + "/local/" + exp_prefix.replace("_", "-") + "/" + exp_name
    if flags["seed"] is not None:
        log_dir += '--s-%d'%flags["seed"]
    if not flags["overwrite"] and osp.exists(log_dir):
        ans = input("Overwrite %s?: (yes/no)"%log_dir)
        if ans != 'yes': sys.exit(0)

    env = get_env(record_video=False, record_log=False, **flags)
    policy = get_policy(env=env, info=info, **flags)
    baseline = get_baseline(env=env, **flags)
    qf = get_qf(env=env, info=info, **flags)
    es = get_es(env=env, info=info, **flags)

    algo = get_algo(n_itr=n_itr, env=env, policy=policy, baseline=baseline,
            qf=qf, es=es, max_path_length=max_path_length, plot=True,**flags)
    return algo, dict(
            exp_prefix=exp_prefix,
            exp_name=exp_name,
            mode=mode,
            seed=flags["seed"],
            )

def run_experiment(**kwargs):
    algo, run_kwargs = set_experiment(**kwargs)
    run_experiment_lite(
        algo.train(),
        n_parallel=0,
        **run_kwargs,
        plot=True
    )

def main(argv=None):
    run_experiment(mode="local")

if __name__ == '__main__':
    tf.app.run()
