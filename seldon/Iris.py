import numpy as np
import pandas as pd
import os
from typing import Dict, List
import joblib
from sklearn.neighbors import KNeighborsClassifier as KNN
from sklearn.neighbors import NearestNeighbors


class Iris(object):

    def __init__(self):
        self.knn_model = joblib.load('iris_model1.pkl')
        
    def predict(self,X,features_names):
    
        x_score = np.array(X)
        
        output1 = self.knn_model.predict(x_score)[0]

        return np.array(output1)

