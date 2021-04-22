import pandas as pd
from sklearn.model_selection import train_test_split

# Using python train_test_split to split dataset into training and testing dataset.

dataset = pd.read_csv("../data/titanic/train.csv")
productionDataset = pd.read_csv("../data/titanic/test.csv")

dataset_train = dataset[["Pclass", "Sex", "SibSp", "Parch"]]
dataset_test = dataset[["Pclass", "Sex", "SibSp", "Parch"]]
# Separate dataset to categories

dataset_train_arr = dataset_train.to_numpy()
dataset_test_arr = dataset_test.to_numpy()
X_train, X_test, Y_train, Y_test = train_test_split(dataset_train_arr, dataset_test_arr, test_size=0.33, random_state=30)


print("this is a test text")