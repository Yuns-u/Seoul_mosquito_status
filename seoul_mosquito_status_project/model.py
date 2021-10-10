import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

#훈련데이터 가져오기
df = pd.read_csv('seoul_mosquito_status_project/data/seoul_mosquito_status.csv')

#test, train data split
train, test= train_test_split(df, random_state=42)

#target지정
target = 'mosquito_value_house'
features = df.drop(columns=[target]).columns

# test, train data target split
X_train = train[features]
y_train = train[target]

X_test = test[features]
y_test = test[target]

#modeling and training
model = LinearRegression()
model.fit(X_train, y_train)

#evaluate by prediction of test data
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred) ##6.70
r2 = r2_score(y_test, y_pred) ##0.74


#prediction model save
with open('seoul_mosquito_status_project/model/model_211007.pickle','wb') as fw:
  pickle.dump(model,fw)