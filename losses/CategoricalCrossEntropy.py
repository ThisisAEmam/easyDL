import numpy as np

class CategoricalCrossEntropy:
    def __init__(self, pred= None, real= None, num_classes= None):
        super().__init__()
        self.type = 'Categorical Cross-Entropy'
        self.predicted = np.transpose(pred)
        self.real = real
        self.num_classes = num_classes
        
    def one_hot_encoding(self, y, K):
        N = len(y)
        ind = np.zeros((N, K))
        for i in range(N):
            ind[i, y[i]] = 1
        return ind
     
    def forward(self):
        return -np.mean(self.one_hot_encoding(self.real, self.num_classes) * np.log(self.predicted+1e-8))
     
    def backward(self):
        return self.predicted - self.one_hot_encoding(self.real, self.num_classes)