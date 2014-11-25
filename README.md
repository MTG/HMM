HMM : Original
===

A numpy/python-only Hidden Markov Models framework. No other dependencies are required.

This implementation (like many others) is based on the paper:
"A Tutorial on Hidden Markov Models and Selected Applications in Speech Recognition, LR RABINER 1989"

Major supported features:

* Discrete HMMs
* Continuous HMMs - Gaussian Mixtures
* Supports a variable number of features
* Easily extendable with other types of probablistic models (simply override the PDF. Refer to 'GMHMM.py' for more information)
* Non-linear weighing functions - can be useful when working with a time-series

Open concerns:
* Examples are somewhat out-dated
* Convergence isn't guaranteed when using certain weighing functions 

----------

HMM : Fork
===

Original reposotory has been forked to add a method for optimizes Viterbi forced alignment

Further more: 

* Underflow issues have been resolved by normalizing probs for each time t at deoding
* Backtracking logic is in a separate class Path to improve readability