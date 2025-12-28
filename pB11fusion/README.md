# pB11FusionSim

A simple Python package for modeling p-B11 aneutronic fusion physics, focusing on bremsstrahlung losses and direct alpha energy capture.

## Installation

pip install git+https://github.com/duraymontague/pB11FusionSim.git

For Usage:
from pB11fusion.core import loss_fraction

print(loss_fraction(1e20, 1e20, 1e5))  # Example at 100 keV

## Motivation

This package was built to explore realistic bremsstrahlung losses in p-B11 fusion — a key challenge in aneutronic designs. It helps illustrate why p-B11 is promising for Type 2 energy paths while highlighting the physics hurdles. Designed for quick testing and iteration.

Feedback welcome — open an issue or PR if you have improvements!
