import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv('training_set.csv')

print(df.head())
df_dict = {}
for index,row in df.iterrows():
    temp = [ord(row[i]) for i in range(18)]
    temp.append(row[18])
    df_dict[index] = temp
    del temp

new_df = pd.DataFrame.from_dict(df_dict, orient='index')
#print(new_df.columns)
new_df.dropna(axis=0,inplace=True)
#print(df.head())

X = new_df.drop([18],axis=1)
Y = new_df[18]

x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size=0.3)
clf = DecisionTreeClassifier()
clf.fit(x_train, y_train)
accuracy = clf.score(x_test,y_test)
y_predict = clf.predict(x_test)
matrix = confusion_matrix(y_test,y_predict)
print(matrix)
print(accuracy)

