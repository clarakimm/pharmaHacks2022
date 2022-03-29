import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
#from sklearn.externals import joblib

mm_data = pd.read_csv("MM-DataSet_Complied_UnhealthyAndUnhealthy.csv", sep = ",")
X = mm_data.drop(columns = ["CLASS"])
y = mm_data['CLASS']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2)

model = DecisionTreeClassifier()
model = model.fit(X_train,y_train)

test = model.predict(X_test)
test

#testing accuracy
score = accuracy_score(y_test, test)

