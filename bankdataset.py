import  numpy as np
import pandas as pd
data=pd.read_csv(r"C:\Users\UJJWAL KUMAR\Downloads\bank_note_data (2).csv")

X=data.iloc[:,0:4]
Y=data.iloc[:,-1]
print(X.shape)
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X=sc.fit_transform(X)
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=.25,random_state=0)
from keras.models import Sequential
from keras.layers import Dense
model= Sequential()
model.add(Dense(7,input_dim=4,activation='relu'))
model.add(Dense(10,activation='relu'))
model.add(Dense(1,activation='sigmoid'))
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
model.fit(x_train,y_train,epochs=150,batch_size=20)
_,accuracy=model.evaluate(x_test,y_test)
print("accuracy: %.2f"%(accuracy*100))