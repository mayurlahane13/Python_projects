import pandas as pd
import sklearn
from sklearn import svm , preprocessing


df = pd.read_csv('/Users/makarandsubhashlahane/Downloads/diamonds.csv', index_col = 0)
cut_class_dict = {'Fair': 1, 'Good': 2,'Very Good': 3, 'Premium':4, 'Ideal': 5}
clarity_dict = {"I3": 1, "I2": 2, "I1": 3, "SI2": 4, "SI1": 5, "VS2": 6, "VS1": 7, "VVS2": 8, "VVS1": 9, "IF": 10, "FL": 11}
color_dict = {"J": 1,"I": 2,"H": 3,"G": 4,"F": 5,"E": 6,"D": 7}

df['cut'] = df['cut'].map(cut_class_dict)
df['clarity'] = df['clarity'].map(clarity_dict)
df['color'] = df['color'].map(color_dict)

df = sklearn.utils.shuffle(df)
x = df.drop('price',axis = 1).values
x = preprocessing.scale(x)
y = df['price'].values

test_size = 200

x_train = x[:-test_size]
y_train = y[:-test_size]

x_test = x[-test_size:]
y_test = y[-test_size:]

clf = svm.SVR(kernel = 'rbf')
print(clf.fit(x_train,y_train))
print(clf.score(x_test,y_test))

for x,y in zip(x_test,y_test) :
    print(f'Model: {clf.predict([x])[0]}, Actual : {y}')