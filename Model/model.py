import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC

data = pd.read_csv("dataa.csv",sep=";")

labels = data.iloc[:,-1]
data = data.iloc[:,0:-1]

# Splitting the data to some to train and some to test
X_train, X_test, y_train, y_test = train_test_split(data,labels,test_size=0.2,random_state=42)



## Training the model
clf.fit(X_train, y_train)

print(clf.score(X_test,y_test))

print (clf.predict([[61,33,33,0,7,19,27,25]]))


clf.predict([[31,20,27,0,21,20,23,12]])

from joblib import dump, load
dump(clf, 'model.joblib') 