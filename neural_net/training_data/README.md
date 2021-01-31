# Neural Network Training Data

These demand files are designed to explore a wide range of flows on the network for the purposes of training a neural network to predict traffic counts on the traffic network.

Each run is built from a latin hypercube sampling of relative flows between each possible origin-destination TAZ pair.

To generate the origin-destination files, run `generate_trainig_matrices.py`.  Once the matrices are generated, create the trips with `generate_training_trips.py`.