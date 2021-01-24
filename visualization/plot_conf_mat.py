import  numpy as np
import matplotlib.pyplot as plt
import seaborn as sn
import pandas as pd

labels=np.array([[1,2,3,4,1,2,3,1,1,2,5]])
preds=np.array([[1,2,3,4,1,2,3,1,2,2,5]])
def plot_conf_matrix(true_labels,preds):
    true_labels=true_labels.squeeze()
    preds=preds.squeeze()
    print(true_labels.shape)
    print(preds.shape)
    classes=np.unique(true_labels)
    conf_matrix=np.zeros((len(classes),len(classes)),dtype='int32')
    for i in range(len(classes)):
        indices_of_class= np.where(labels == classes[i])
        print(indices_of_class)
        for j in range(len(classes)):
            class_predictions = preds[indices_of_class[1]]
            appearnce_count=np.count_nonzero(class_predictions==classes[j])
            if appearnce_count>0:
                conf_matrix[i, j] = np.count_nonzero(class_predictions == classes[j])
    confusion= pd.DataFrame(conf_matrix, range(len(classes)), range(len(classes)))
    sn.set(font_scale=1)  # for label size
    sn.heatmap(confusion,annot=True,cmap='Blues')  # font size
    plt.xlabel('predicted label')
    plt.ylabel('true label')
    plt.show()
