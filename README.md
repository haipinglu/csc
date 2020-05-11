# Convolutional Sparse Coding
This is an implementation of convolutional sparse coding paper in PyTorch. Iterative Shrinkage/Thresholding Algorithm 
(ISTA) is used to fit neuronal responses for the input. Gradients for receptive fields are calculated through PyTorch's autograd
feature. 

## Run
To run the program:
```python
cd src/scripts
python train.py 
```
To see a list of available hyperparameters to change:
```python
python train.py -h
```
A checkpoint of the model is saved every 10 epochs to `trained_models`. To see the tensorboard logs:
```python
tensorboard --logdir=runs
```

## Will be added soon
* Fast-ISTA

## References
* `IMAGES.mat` is downloaded from Olshausen's original Matlab implementation website: http://www.rctn.org/bruno/sparsenet/
