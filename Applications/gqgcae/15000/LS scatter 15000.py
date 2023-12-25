import pandas as pd
#忽略
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'#取消提示信息
import numpy as np
from keras.models import load_model

dataoriginal = pd.read_csv('G:\科研\检测异常度\data\Features\SM-15000.csv')
print(dataoriginal)
print(type(dataoriginal))
datatrain = dataoriginal[0:400000]
datatrainarrange = np.mean(datatrain,axis=0)
datatrainstd = np.std(datatrain,axis=0)
print("平均数：", np.mean(datatrain,axis=0))
print("标准差 ", np.std(datatrain,axis=0))
data = (dataoriginal - datatrainarrange)/datatrainstd #对数据进行标准化
print(data)
datatrain = data[0:400000]
datavalidation = data[400000:500000]
datatest = data[500000:]
print(datatrain,datavalidation,datatest)

dataFgT0originall = pd.read_csv('G:\科研\检测异常度\data\Features\FgT0-15000.csv')
datatrainarrange = np.array(datatrainarrange)
datatrainstd = np.array(datatrainstd)
print(dataFgT0originall)
print(datatrainarrange)
print(datatrainstd)
dataFgT0 = (dataFgT0originall - datatrainarrange)/datatrainstd
print('dataFgT0')
print(dataFgT0)
dataFgT1originall = pd.read_csv('G:\科研\检测异常度\data\Features\FgT1-15000.csv')
dataFgT1 = (dataFgT1originall - datatrainarrange)/datatrainstd

dataFgT2originall = pd.read_csv('G:\科研\检测异常度\data\Features\FgT2-15000.csv')
dataFgT2 = (dataFgT2originall - datatrainarrange)/datatrainstd

dataFgT3originall = pd.read_csv('G:\科研\检测异常度\data\Features\FgT3-15000.csv')
dataFgT3 = (dataFgT3originall - datatrainarrange)/datatrainstd

encoder = load_model("encoder.h5")
#from tensorflow import keras
#encoder = keras.models.load_model('path/to/location')
pred_test =encoder.predict(datatest)
pred_FgT0 =encoder.predict(dataFgT0)
pred_FgT1 =encoder.predict(dataFgT1)
pred_FgT2 =encoder.predict(dataFgT2)
pred_FgT3 =encoder.predict(dataFgT3)
print(pred_test)
list1=pred_test[:,0]
list2= pred_test[:,1]
list=[]
list.append(list1)
list.append(list2)
print(list)
test=pd.DataFrame(data=list)#将数据放进表格
test.to_csv('30TeVsmLS.csv')
xFgT0 = pred_FgT0[:,0]
yFgT0 = pred_FgT0[:,1]
xFgT1 = pred_FgT1[:,0]
yFgT1 = pred_FgT1[:,1]
xFgT2 = pred_FgT2[:,0]
yFgT2 = pred_FgT2[:,1]
xFgT3 = pred_FgT3[:,0]
yFgT3 = pred_FgT3[:,1]
listnp=[]
x=np.concatenate((xFgT0,xFgT1,xFgT2,xFgT3),axis=0)
y=np.concatenate((yFgT0,yFgT1,yFgT2,yFgT3),axis=0)
listnp.append(x)
listnp.append(y)
test=pd.DataFrame(data=listnp)#将数据放进表格
test.to_csv('30TeVnpLS.csv') #数据存入csv,存储位置及文件名称
print(x,y)