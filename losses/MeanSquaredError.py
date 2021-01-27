import numpy as np

class MeanSquaredError:
    def __init__(self, pred= None, real= None):
        super().__init__()
        self.type = 'Mean Squared Error'  
        self.predicted = pred
        self.real = real
     
    def forward(self):
        return np.power(self.predicted - self.real, 2).mean()
 
    def backward(self):
        return 2 * (self.predicted - self.real).mean()