# 1. Pretraining RL Policies with Human Data

This document presents results achieved during the weeks of June 17 and June 24, 2018.

## Starting Point

The main goal of this set of experiments was to evaluate if initializing a reinforcement learning algorithm with a pretrained policy would lead to better performance when compared to random initializing the reinforcement learning policy. In this case, the pretrained policy is a *behavior cloning* deep neural network trained on human demonstration of the task, and *policy gradient* (PG) algorithm is used for reinforcement learning.

The proposed approach was evaluated in the HRI_AirSim_Landing-v0 environment (landing task, simple map), with reward given only by the end of episode based on the negative Euclidean distance of the vehicle and center of the landing pad (zero reward means the vehicle landed at the center of the landing pad). Figure 1 shows that simply initializing a PG algorithm with a pretrained policy leads to initial better results, but the pretrained weights are quickly overwritten and performance decays.

<center>
    <img width="432" alt="Picture" src="./media/1/1_human_init.png">
    <img width="432" alt="Picture" src="./media/1/1_human_init_detail.png">
    <p>
    <b>Figure 1.</b> Performance comparison between policy gradient reinforcement learning algorithm initialize with a random policy (not_pretrained_v0) and behavior cloning policy (pretrained_v0).
    </p>
</center>


Since the results were not satisfactory, a couple of different solutions were suggested after a conference call on June 15, 2018:

1. **Change the reward function:** instead of using a sparse reward signal (reward given only at the end of the episode), it was suggested to use a dense reward signal by computing the negative of the Euclidean distance at every simulation step.

2. **Train for more episodes:** train using the PG RL algorithm for more episodes to confirm that the algorithm is able to learn the task.

3. **Limit initial gradient updates:** limiting the initial gradient updates would theoretically prevent quick overwriting of the pretrained weights.


## Week of June 17, 2018

Previous results were lacking comparison to human performance. To address this issue, the human demonstration data was parsed in order to extract a performance metric. Figure 2 shows the final distance to the landing pad (in the XY plane) when a human performed the landing task 19 times and vehicle data for a sample episode. The minimum distance to the center of the landing pad was 0.042 meters and the maximum distance was 0.249 meters. These values will be used as baseline for the learning agent's performance.

<center>
    <img width="432" alt="Picture" src="./media/1/1_human_performance.png">
    <img width="432" alt="Picture" src="./media/1/1_human_sample_pos.png">
    <img width="432" alt="Picture" src="./media/1/1_human_sample_att.png">
    <img width="432" alt="Picture" src="./media/1/1_human_sample_u.png">
    <p>
    <b>Figure 2.</b> Human-level performance while demonstrating the landing task.
    </p>
</center>

The address the proposed solutions discussed in the "Starting Point", the learning experiment was changed in different ways:

1. Used a dense reward signal (negative of the Euclidean distance), rewarding the agent at every training step.

2. Ran the experiment for 1500 episodes, instead of just 100.

3. Used the Proximal Policy Optimization (PPO) instead of pure Policy Gradient (PG) as the reinforcement learning algorithm.

After training for 1500 episodes, that's the performance achieve by the agent:

<center>
    <img width="432" alt="Picture" src="./media/1/1-0_ppo_dense_reward.png">
    <img width="432" alt="Picture" src="./media/1/1-0_ppo_dense_reward_steps.png">
    <img width="432" alt="Picture" src="./media/1/1-0_human_comparison.png">
    <p>
    <b>Figure 3.</b> Performance achieved by the PPO agent after 1500 episodes (Experiment ID 1-0).
    </p>
</center>

Here are two videos for comparison of the initial performance of a randomly initialized policy (video on the left) and final trained policy (video on the right).

<center>
    <img width="432" alt="Picture" src="./media/1/1-0_epi0_vehicle_pos.png">
    <img width="432" alt="Picture" src="./media/1/1-0_epi1100_vehicle_pos.png">
    <img width="432" alt="Picture" src="./media/1/1-0_epi0_vehicle_att.png">
    <img width="432" alt="Picture" src="./media/1/1-0_epi1100_vehicle_att.png">
    <img width="432" alt="Picture" src="./media/1/1-0_epi0_vehicle_u.png">
    <img width="432" alt="Picture" src="./media/1/1-0_epi1100_vehicle_u.png">
    <a href="https://youtu.be/AYXLGjXNSKw"><img width="432" alt="Picture" src="https://img.youtube.com/vi/AYXLGjXNSKw/0.jpg"></a>
    <a href="https://youtu.be/DcusYAYM2-w"><img width="432" alt="Picture" src="https://img.youtube.com/vi/DcusYAYM2-w/0.jpg"></a>
    <p>
    <b>Figure 4.</b> Performance comparison between episode 0 (left images, link to video: https://youtu.be/AYXLGjXNSKw) and episode 1000+ (right images, link to video: https://youtu.be/DcusYAYM2-w). <i>Experiment ID: 1-0.</i>
    </p>
</center>


## Week of June 24, 2018

After running Experiment 1-0, it was noticed that the policy was running at low frequencies. Investigating the configuration files, it was identified that the policy was set to hold the same action for 6 frames. This configuration was used in previous experiments with discrete action-space (similar to the Atari DQN work). The configuration was changed to allow the policy to pick an action at every frame, increasing its frequency by 6 times. Figures 5, 6, and 7 show the results of these experiments.

As an interesting fact, it can be noticed that there a jump in performance after episode 1000. Since about episode 250 the agent is able to land the vehicle correctly at the landing pad (reward of -800), but after 1000 it somehow exploits the vehicle dynamics to make the landing faster (even though it is set to be constant throttle). This result is confirmed by the plot the shows the number of steps taken per episode.

<center>
    <img width="432" alt="Picture" src="./media/1/1-1_ppo_dense_reward_no_hold.png">
    <img width="432" alt="Picture" src="./media/1/1-1_ppo_dense_reward_no_hold_steps.png">
    <img width="432" alt="Picture" src="./media/1/1-1_human_comparison.png">
    <p>
    <b>Figure 5.</b> Performance achieved by the PPO agent after 2500 episodes, without holding the same action for 6 frames. <i>Experiment ID: 1-1.</i>
    </p>
</center>

<center>
    <img width="432" alt="Picture" src="./media/1/1-1_epi0_vehicle_pos.png">
    <img width="432" alt="Picture" src="./media/1/1-1_epi400_vehicle_pos.png">
    <img width="432" alt="Picture" src="./media/1/1-1_epi0_vehicle_att.png">
    <img width="432" alt="Picture" src="./media/1/1-1_epi400_vehicle_att.png">
    <img width="432" alt="Picture" src="./media/1/1-1_epi0_vehicle_u.png">
    <img width="432" alt="Picture" src="./media/1/1-1_epi400_vehicle_u.png">
    <a href="https://youtu.be/_d68pbZKuM4"><img width="432" alt="Picture" src="https://img.youtube.com/vi/_d68pbZKuM4/0.jpg"></a>
    <a href="https://youtu.be/dMfbho7wSrk"><img width="432" alt="Picture" src="https://img.youtube.com/vi/dMfbho7wSrk/0.jpg"></a>
    <p>
    <b>Figure 6.</b> Performance comparison between episode 0 (left images, link to video: https://youtu.be/_d68pbZKuM4) and episode 400 (right images, link to video: https://youtu.be/dMfbho7wSrk). <i>Experiment ID: 1-1.</i>
    </p>
</center>

<center>
    <img width="432" alt="Picture" src="./media/1/1-1_epi1200_vehicle_pos.png">
    <img width="432" alt="Picture" src="./media/1/1-1_epi2360_vehicle_pos.png">
    <img width="432" alt="Picture" src="./media/1/1-1_epi1200_vehicle_att.png">
    <img width="432" alt="Picture" src="./media/1/1-1_epi2360_vehicle_att.png">
    <img width="432" alt="Picture" src="./media/1/1-1_epi1200_vehicle_u.png">
    <img width="432" alt="Picture" src="./media/1/1-1_epi2360_vehicle_u.png">
    <a href="https://youtu.be/3GyluFA8pmY"><img width="432" alt="Picture" src="https://img.youtube.com/vi/3GyluFA8pmY/0.jpg"></a>
    <a href="https://youtu.be/cnHAc1zFv3c"><img width="432" alt="Picture" src="https://img.youtube.com/vi/cnHAc1zFv3c/0.jpg"></a>
    <p>
    <b>Figure 7.</b> Performance comparison between episode 1200 (left images, link to video: https://youtu.be/3GyluFA8pmY) and episode 2360 (right images, link to video: https://youtu.be/cnHAc1zFv3c). <i>Experiment ID: 1-1.</i>
    </p>
</center>

Figure 8 shows a comparison between Experiment ID 1-0 and ID 1-1 (the two cases above).

<center>
    <img width="432" alt="Picture" src="./media/1/1-0_1-1_comparison.png">
    <img width="432" alt="Picture" src="./media/1/1-0_1-1_comparison_steps.png">
    <p>
    <b>Figure 8.</b> Performance comparison between Experiment ID 1-0 and 1-1.
    </p>
</center>

After running Experiment 1-1 using a dense reward signal (negative of the Euclidean distance given at every step), it was desire to explore the agent's performance using sparse rewards (negative of the Euclidean distance given only at the end of the episode). Figures 9, 10, and 11 show the results of the experiment.

<center>
    <img width="432" alt="Picture" src="./media/1/1-2_sparse.png">
    <img width="432" alt="Picture" src="./media/1/1-2_sparse_steps.png">
    <img width="432" alt="Picture" src="./media/1/1-2_human_comparison.png">
    <p>
    <b>Figure 9.</b> Performance achieved by the PPO agent after 2500 episodes driven by sparse reward signal. <i>Experiment ID: 1-2.</i>
    </p>
</center>

<center>
    <img width="432" alt="Picture" src="./media/1/1-2_epi0_vehicle_pos.png">
    <img width="432" alt="Picture" src="./media/1/1-2_epi240_vehicle_pos.png">
    <img width="432" alt="Picture" src="./media/1/1-2_epi0_vehicle_att.png">
    <img width="432" alt="Picture" src="./media/1/1-2_epi240_vehicle_att.png">
    <img width="432" alt="Picture" src="./media/1/1-2_epi0_vehicle_u.png">
    <img width="432" alt="Picture" src="./media/1/1-2_epi240_vehicle_u.png">
    <a href="https://youtu.be/hel5pWpsfgc"><img width="432" alt="Picture" src="https://img.youtube.com/vi/hel5pWpsfgc/0.jpg"></a>
    <a href="https://youtu.be/TslL3bATkqI"><img width="432" alt="Picture" src="https://img.youtube.com/vi/TslL3bATkqI/0.jpg"></a>
    <p>
    <b>Figure 10.</b> Performance comparison between episode 0 (left images, link to video: https://youtu.be/hel5pWpsfgc) and episode 240 (right images, link to video: https://youtu.be/TslL3bATkqI). <i>Experiment ID: 1-2.</i>
    </p>
</center>

<center>
    <img width="432" alt="Picture" src="./media/1/1-2_epi1040_vehicle_pos.png">
    <img width="432" alt="Picture" src="./media/1/1-2_epi2460_vehicle_pos.png">
    <img width="432" alt="Picture" src="./media/1/1-2_epi1040_vehicle_att.png">
    <img width="432" alt="Picture" src="./media/1/1-2_epi2460_vehicle_att.png">
    <img width="432" alt="Picture" src="./media/1/1-2_epi1040_vehicle_u.png">
    <img width="432" alt="Picture" src="./media/1/1-2_epi2460_vehicle_u.png">
    <a href="https://youtu.be/U0CYpPH1U8U"><img width="432" alt="Picture" src="https://img.youtube.com/vi/U0CYpPH1U8U/0.jpg"></a>
    <a href="https://youtu.be/cJUjoYBJ71M"><img width="432" alt="Picture" src="https://img.youtube.com/vi/cJUjoYBJ71M/0.jpg"></a>
    <p>
    <b>Figure 11.</b> Performance comparison between episode 1040 (left images, link to video: https://youtu.be/U0CYpPH1U8U) and episode 2460 (right images, link to video: https://youtu.be/cJUjoYBJ71M). <i>Experiment ID: 1-2.</i>
    </p>
</center>


## Additional Results

### Realistic Maps and Assets with Unreal Engine

All the learning tasks have been using simplified maps, which abstracts computer vision challenges such as object detection. For a compelling demo, we are preparing a more realistic scenario that simulates a desert village where different learning tasks can be evaluated. The video bellow shows the current version of the scenario:


<center>
<a href="https://www.youtube.com/embed/Pfmp4vviAqA"><img width="432" alt="Picture" src="https://img.youtube.com/vi/Pfmp4vviAqA/0.jpg"></a>
    <p>
    <b>Figure 4.</b> Overview of the desert village map.
    </p>
</center>

All learning maps and latest assets can be downloaded at:  
https://drive.google.com/open?id=1-3tPUeyAslwD-q9kZDzxS6eT5QcTjr5v
