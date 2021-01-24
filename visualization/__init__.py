from .plot_losses import plot_losses

# import matplotlib
# import numpy as np
# import pandas as pd
 
# import matplotlib.pyplot as plt
# from sklearn.datasets import make_moons, make_circles 

# from process import get_data

# def generate_data(samples, shape_type='circles', noise=0.05):
#     # We import in the method for the shake of simplicity
#     if shape_type == 'moons':
#         X, Y = make_moons(n_samples=samples, noise=noise)
#     elif shape_type == 'circles':
#         X, Y = make_circles(n_samples=samples, noise=noise)
#     else:
#         raise ValueError(f"The introduced shape {shape_type} is not valid. Please use 'moons' or 'circles' ")
     
#     data = pd.DataFrame(dict(x=X[:,0], y=X[:,1], label=Y))
#     X = data.iloc[:, :-1].values
#     Y = data.iloc[:, -1].values
#     return X, Y

# def generate_multi_class_data(samples_per_class, one_hot= False, plot= False):
#     np.random.seed(42)

#     cat_images = np.random.randn(samples_per_class, 2) + np.array([0, -3])
#     mouse_images = np.random.randn(samples_per_class, 2) + np.array([3, 3])
#     dog_images = np.random.randn(samples_per_class, 2) + np.array([-3, 3])
    
#     feature_set = np.vstack([cat_images, mouse_images, dog_images])
#     labels = np.array([0]*samples_per_class + [1]*samples_per_class + [2]*samples_per_class)
#     one_hot_labels = np.zeros((3 * samples_per_class, 3))

#     for i in range(3*samples_per_class):
#         one_hot_labels[i, labels[i]] = 1
    
#     if plot:
#         plt.scatter(feature_set[:,0], feature_set[:,1], c=labels, cmap='plasma', s=100, alpha=0.5)
#         plt.show()
    
#     if one_hot:
#         return feature_set, one_hot_labels
#     else:
#         return feature_set, labels

# def plot_generated_data(data):
#     ax = data.plot.scatter(x='x', y='y', figsize=(10, 8), color=data['label'], 
#                            cmap=matplotlib.colors.ListedColormap(['skyblue', 'salmon']), grid=True);
     
#     return ax