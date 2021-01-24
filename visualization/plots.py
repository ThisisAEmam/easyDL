

import matplotlib.pyplot as plt
import numpy as np

def plot_losses(model):
    plt.figure(figsize=(10, 8))
    plt.xticks(np.arange(1, len(model.losses)+1, 1))
    plt.plot(model.losses)
    xmin, xmax = plt.xlim()
    ymin, ymax = plt.ylim()
    plt.axis([0, len(model.losses),ymin, ymax])
    
    
    

def plot_accurcy(model):
    plt.figure(figsize=(10, 8))
    plt.xticks(np.arange(1, len(model.acc)+1, 1))
    plt.plot(model.acc)
    xmin, xmax = plt.xlim()
    ymin, ymax = plt.ylim()
    plt.axis([0, len(model.acc),ymin, ymax])
    
    

    
    
