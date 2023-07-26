import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
# get the data 
data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]

print(data)
print(target)

#initialize the model
reg_model = linear_model.LinearRegression()

# split the test and train data
x_train, x_test, y_train, y_test = train_test_split(data, target, test_size=0.33, random_state=42)

#Train our model with the training data
reg_model.fit(x_train, y_train)

#Print the coefecients/weights for each feature/column of our model
print(reg_model.coef_)

# get the predected values for prices
y_pred = reg_model.predict(x_test)
print(y_pred)

# get the accuracy using the mean squared error 
print(np.mean((y_pred-y_test)**2),'%')
