# Adversarial Attacks Against Federated Learning Systems

## Installation

1) Create a virtualenv (Python 3.7)
2) Install dependencies inside of virtualenv (```pip install -r requirements.pip```)


## Instructions for execution

The steps required to execute different experiments are below.

### Setup

Before you can run any experiments, you must complete some setup:

1) ```python3 generate_data_distribution.py``` This downloads the dataset, as well as generates a static distribution of the training and test data to provide consistency in experiments.
2) ```python3 generate_default_models.py``` This generates an instance of all of the models used in the paper, and saves them to disk.

### General Information

Some pointers & general information:
- Most hyperparameters can be set in the ```federated_learning/arguments.py``` file
- Most specific experiment settings are located in the respective experiment files (see the following sections)

### Experiments - Label Flipping Attack Feasibility

Running an attack: ```python3 label_flipping_attack.py```

### Experiments - Attack Timing in Label Flipping Attacks

Running an attack: ```python3 attack_timing.py```

### Experiment Hyperparameters

Recommended default hyperparameters for Fashion-MNIST (using the provided CNN):
- Batch size: 4
- LR: 0.001
- Number of epochs: 200
- Momentum: 0.9
- Scheduler step size: 10
- Scheduler gamma: 0.1
- Min_lr: 1e-10

