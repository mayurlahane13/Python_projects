import pandas as pd
import quandl, math
import numpy as np
from sklearn import preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression

df = quandl.get("EOD/BA", authtoken="Mw7-sfy4caCmhjzEiQ3k")
df = df[['Adj_Open', 'Adj_High', 'Adj_Low', 'Adj_Close', 'Adj_Volume']]
df['hl_pct'] = ((df['Adj_High']-df['Adj_Close'])/df['Adj_Close'] *100)
df['pct_change'] = ((df['Adj_Close']-df['Adj_Open'])/df['Adj_Open'] *100)
df = df[['Adj_Close','hl_pct','pct_change','Adj_Volume']]
forecast_col = 'Adj_Close'
forecast_out = int(math.ceil(0.01*len(df)))
df['label'] = df[forecast_col].shift(-forecast_out)

X = np.array(df.drop(['label'],1))
X = preprocessing.scale(X)
X = X[:-forecast_out]
X_lately = X[-forecast_out:]
df.dropna(inplace = True)
y = np.array(df['label'])


train_X , test_X , train_y, test_y = model_selection.train_test_split(X, y, test_size=  0.2)
clf = LinearRegression()
clf.fit(train_X, train_y)
accuracy  = clf.score(test_X,test_y)

forecast_set = clf.predict(X_lately)
print(forecast_set)