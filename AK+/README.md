# Andrej Karpathy Code Repositories which I will deep dive.

## micrograd
---

A tiny Autograd engine (with a bite!:)). Implements backgpropagation (reverse-mode autodiff) over a dynamically built DAG and a small neural networks library on top of it with a PyTorch-like API. Both are tiny, with about 100 and 50 lines of code respectively. 

The DAG only operates over scalar values, so e.g. we chop up each neuron into all of its individual tiney adds and multiplies. However, this is enough to build up entire deep neural nets doing binary classification, as the demo notebook shows. Potentially useful for educational purposes.



