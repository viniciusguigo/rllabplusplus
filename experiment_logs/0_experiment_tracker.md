# 0. Experiment Tracker

This document tracks experiment identification numbers, log names, goals, and summary of results.

| Experiment ID | Log Name | Goals and Outcomes | Note |
| :-: | :-: | :-: | :-: |
| 1-0 | data/local/lander-trpo | 1_progress_report.md | TRPO on LunarLanderContinuous-v2 (1000 episodes, batch size 1000), 3 seeds |
| 1-1 | data/local/lander-qprop | 1_progress_report.md | Q-Prop on LunarLanderContinuous-v2 (1000 episodes, batch size 1000), 3 seeds |
| 1-2 | data/local/lander-ipg | 1_progress_report.md | IPG on LunarLanderContinuous-v2 (1000 episodes, batch size 1000), 3 seeds |
| 1-3 | data/local/lander-trpo1 | 1_progress_report.md | TRPO on LunarLanderContinuous-v2 (1000 episodes, batch size 2000), 3 seeds |
| 1-4 | data/local/lander-qprop1 | 1_progress_report.md | Q-Prop on LunarLanderContinuous-v2 (1000 episodes, batch size 2000), 3 seeds |
| 1-5 | data/local/lander-ipg1 | 1_progress_report.md | IPG on LunarLanderContinuous-v2 (1000 episodes, batch size 2000), 3 seeds |
| 1-6 | data/human/human_lunarlander0_log.csv | 1_progress_report.md | Human performance (50 episdoes) |

## Convert Markdown to PDF

### Option 1: Google Chrome

Install Markdown Viewer extension. Open file using Chrome and save as PDF. Handles better the HTML marks.

### Option 2: NPM Package

Using the npm package markdown-pdf. Install using "sudo npm install -g markdown-pdf". If there is any permission errors while installing it, please take a look at https://github.com/Microsoft/WSL/issues/14

Usage:

markdown-pdf [options] **markdown-file-path**

# Report Releases

| Name | File | Period |
| :-: | :-: | :-: |
| 1. Baselines: Cycle-of-Learning (Phase II) | 1_progress_report.md | November 17-30, 2018 |
