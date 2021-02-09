import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder


dataset = pd.read_csv("../data/titanic/train.csv")
productionDataset = pd.read_csv("../data/titanic/test.csv")


dataset_train = dataset[["Pclass", "Sex", "SibSp", "Parch"]]
dataset_test = dataset[["Survived"]]

le = preprocessing.LabelEncoder()
label = le.fit_transform(dataset_train["Sex"])

"""
#dataset_train.loc[:, "Sex"] = le.fit_transform(dataset_train['Sex'])
#dataset_train["Sex"] = le.fit_transform(dataset_train["Sex"].copy(deep=True))
#print(dataset_train)
"""


ohe = OneHotEncoder(handle_unknown='ignore', sparse=False)
array = ohe.fit_transform(dataset_train["Sex"].to_numpy().reshape(-1,1))


