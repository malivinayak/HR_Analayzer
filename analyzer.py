# All Libraries

import numpy as np
import pandas as pd
import scipy.stats as stats

from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


def HR_analyzer(userData):
    dataset = pd.read_csv('train_LZdllcl.csv',low_memory=False)

    def dataPreProcessing(dataset):
        
        # Creating Age Range
        dataset['age']=np.where( dataset['age'] < 25, 1, dataset['age'])
        dataset['age']=np.where((dataset['age'] >= 25) & (dataset['age'] < 33), 2, dataset['age'])
        dataset['age']=np.where((dataset['age'] >= 33) & (dataset['age'] < 42), 3, dataset['age'])
        dataset['age']=np.where(dataset['age'] >= 42 , 4, dataset['age'])

        # Creating length_of_service Range
        dataset['length_of_service']=np.where( dataset['length_of_service'] < 11, 0, dataset['length_of_service'])
        dataset['length_of_service']=np.where(dataset['length_of_service'] >= 11 , 1, dataset['length_of_service'])
        
        dataset['previous_year_rating'] = dataset['previous_year_rating'].fillna(dataset['previous_year_rating'].mode()[0])
        
        return dataset
        
    dataset = dataPreProcessing(dataset)

    # Model
    X = dataset.drop("is_promoted",axis=1)
    Y = dataset["is_promoted"]
    model = LogisticRegression(solver='lbfgs', max_iter=100000)
    model.fit(X,Y)

    userDataset = pd.DataFrame(data=userData)
    return model.predict(userDataset)
