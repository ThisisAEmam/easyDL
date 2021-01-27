import numpy as np

class SparseCategoricalCrossEntropy:
    def __init__(self, pred= None, real= None):
        super().__init__()
        self.type = 'Sparse Categorical Cross-Entropy'   
        self.predicted = np.transpose(pred)
        self.real = real
     
    def forward(self, pred, real):
        return -np.mean(self.real*np.log(self.predicted))
     
    def backward(self):
        return self.predicted - self.real