# Code for "Addressing Hindsight Bias in Multi-Goal Reinforcement Learning" 

## Prerequisites
- Tensorflow-gpu >= 1.13
- OpenAI [Gym](http://gym.openai.com/)
- [Mujoco-py](https://github.com/openai/mujoco-py) with [license](https://www.roboti.us/license.html)

## Install

``` shell
git clone https://github.com/review-anon/BHER.git
cd BHER
pip install -e .
```

## Implemented Algorithms

- BHER
- HER from [NeurIPS 2017](https://arxiv.org/abs/1707.01495) 
- ARCHER from [ArXiv 2019](https://arxiv.org/abs/1809.02070)
- MEP from [ICML 2019](https://arxiv.org/abs/1905.08786) 
- CHER from [NeurIPS 2019](https://papers.nips.cc/paper/9425-curriculum-guided-hindsight-experience-replay)


## Structure Overview

``` tree
BHER
|-- BHER
    |-- archer
    |-- bher
    |-- her
    |-- cher
    |-- mep
```

- HER/ARCHER code from the official [link](https://github.com/openai/baselines/tree/master/baselines/her)
- MEP code from the official [link](https://github.com/ruizhaogit/mep)
- CHER code from the official [link](https://github.com/mengf1/CHER)

We collect all methods in our benchmark to facilitate experimental reproducibility and to encourage adoption by other researchers.

In all methods, we use 19 CPU cores in training, each epoch contains 50 cycles, each cycle contains 40 batches, and the batch size is set to 256.


## Environments

The environments are from OpenAI Gym [Robotics](https://gym.openai.com/envs/#robotics). They are as follows:

- FetchReach-v1
- FetchPush-v1
- FetchPickAndPlace-v1
- FetchSlide-v1
- HandReach-v0
- HandManipulateBlockRotateZ-v0
- HandManipulateBlockRotateParallel-v0
- HandManipulateBlockRotateXYZ-v0
- HandManipulateBlockFull-v0
- HandManipulateEggRotate-v0
- HandManipulateEggFull-v0
- HandManipulatePenRotate-v0
- HandManipulatePenFull-v0


## Usage

### Run BHER

The following command should train an agent on for 50 epochs.

``` shell
cd BHER/bher/experiment/
python train.py --env_name FetchReach-v1 --logdir result/FetchReach
python train.py --env_name FetchPush-v1 --logdir result/FetchPush
python train.py --env_name FetchPickAndPlace-v1 --logdir result/FetchPickAndPlace
python train.py --env_name FetchSlide-v1 --logdir result/FetchSlide
python train.py --env_name HandManipulateBlockRotateZ-v0 --logdir result/HandManipulateBlockRotateZ
python train.py --env_name HandManipulateBlockRotateParallel-v0 --logdir result/HandManipulateBlockRotateParallel
python train.py --env_name HandManipulateBlockRotateXYZ-v0 --logdir result/HandManipulateBlockRotateXYZ
python train.py --env_name HandManipulateBlockFull-v0 --logdir result/HandManipulateBlockFull
python train.py --env_name HandManipulatePenRotate-v0 --logdir result/HandManipulatePenRotate
python train.py --env_name HandManipulatePenFull-v0 --logdir result/HandManipulatePenFull
python train.py --env_name HandManipulateEggRotate-v0 --logdir result/HandManipulateEggRotate --r_bias 0.001 --bias_clip_high 5
python train.py --env_name HandManipulateEggFull-v0 --logdir result/HandManipulateEggFull --r_bias 0.001 --bias_clip_high 5
```

### Run Other Baselines

The following command should train an agent on "HandReach" for 50 epochs with other baseline methods.

#### HER

``` shell
cd BHER/her/experiment/
python train.py --env_name HandReach-v0 --logdir result-her/HandReach
```

#### ARCHER

(with factors 2.0 and 1.0)
``` shell
cd BHER/archer/experiment/
python train.py --env_name HandReach-v0 --logdir result-her/HandReach
```

#### MEP

``` shell
cd BHER/mep/experiment/
python train.py --env_name HandReach-v0 --logdir result-mep/HandReach
```

#### CHER

``` shell
cd BHER/cher/experiment/
python train.py --env_name HandReach-v0 --logdir result-cher/HandReach
```

## Execution

Each run directory contains 
- log.txt. Monitor file by using `logger` from `Openai Baselines`.
- params.json. All hyper-parameters used in training.
- progress.csv. Same data as `log.txt` but with `csv` format. Using `experiment/train.py` to plot the learning curve.
- total_rbias_mean.npy (option). Save the mean bias of each training batches in BHER.

## Licence
The MIT License