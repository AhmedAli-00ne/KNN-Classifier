import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
from sklearn import preprocessing
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import make_classification
import joblib

def KNNTrain():
    df = pd.read_csv('diabetes_binary_health_indicators_BRFSS2015.csv')
    X = df.drop(['Diabetes_binary','Education','Income'] , axis = 1)
    y = np.array(df['Diabetes_binary'])
    X , y = make_classification(n_samples=10000, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split (X, y, test_size=0.2)
    
    knn=KNeighborsClassifier(n_neighbors=13)
    
    knn.fit(X_train,y_train)
    
    joblib.dump(knn, 'knn_model.pkl')
    
    y_pred=knn.predict(X_test)
    return y_pred, y_test

def evaluate(y_pred, y_test):
    accuracy = accuracy_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    return accuracy, recall, precision, f1

acc , recall, precision, f1 = evaluate(*KNNTrain())
print('Accuracy: ', acc)
print('Recall: ', recall)
print('Precision: ', precision)
print('F1: ', f1)
