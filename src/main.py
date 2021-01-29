

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

"""
1. Using X_train, Y_train to train model. 

2. Then using X_test, Y_test to predict new dataset called Y_predict

3. Compare Y_predict with Y_test

If Y_test is statistically significant, your model is accurate. 



Using two models, RandomForest & ExtremeTree
Which ever has lower Y_test is better.
"""




train_data = pd.read_csv("../data/titanic/train.csv")
test_data = pd.read_csv("../data/titanic/test.csv")
#print(train_data.head())



woman = train_data.loc[train_data.Sex == "female"][['Survived']]

# print(len(woman), sum(woman.Survived), type(woman))
ws_rate = sum(woman.Survived) / len(woman)

print(f'% women survived {ws_rate} - which is good')




ax = sns.countplot(x = "Sex", hue = "Survived", data = train_data)
#plt.show()



# dt = DecisionTree()
# dt.train()
# dt.pred(test)