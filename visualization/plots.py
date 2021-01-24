import matplotlib.pyplot as plt
import numpy as np

def plot_losses(model):
    plt.figure(figsize=(10, 8))
    plt.xticks(np.arange(0, len(model.losses), 1))
    plt.plot(model.losses, label = 'train loss')
    plt.plot(model.losses_val, label = 'validation loss')
    plt.legend()
    plt.show()
    

def plot_accuracy(model):
    plt.figure(figsize=(10, 8))
    plt.xticks(np.arange(0, len(model.losses), 1))
    plt.plot(model.acc, label = 'train accuracy')
    plt.plot(model.acc_val, label = 'validation accuracy')
    plt.legend()
    plt.show()
    

    
    

    

