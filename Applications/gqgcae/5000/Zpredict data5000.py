import pandas as pd
#忽略
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'#取消提示信息
import numpy as np
from keras.models import load_model
dataoriginal = pd.read_csv('G:\科研\检测异常度\data\Features\SM-5000.csv')
datatrainoriginal = dataoriginal[0:400000]
datatrainarrange = np.mean(datatrainoriginal,axis=0)
datatrainstd = np.std(datatrainoriginal,axis=0)
print("平均数：", np.mean(datatrainoriginal,axis=0))
print("标准差 ", np.std(datatrainoriginal,axis=0))
data = (dataoriginal - datatrainarrange)/datatrainstd
autoencoder10 = load_model("autoencoder10.h5")
datatrain = data[0:400000]
datavalidation = data[400000:500000]
datatest = data[500000:]
pred_test = autoencoder10.predict(datatest)
print('datatest')
print(datatest)
print('pred_test')
print(pred_test)
mse_test = np.array(np.mean(np.power(datatest - pred_test, 2), axis=1))

dataFgT0originall = pd.read_csv('G:\科研\检测异常度\data\Features\FgT0-5000.csv')
datatrainarrange = np.array(datatrainarrange)
datatrainstd = np.array(datatrainstd)
print(dataFgT0originall)
print(datatrainarrange)
print(datatrainstd)
dataFgT0 = (dataFgT0originall - datatrainarrange)/datatrainstd
print(dataFgT0)
pred_FgT0 = autoencoder10.predict(dataFgT0)
print(pred_FgT0)
mse_test_pred_FgT0 = np.array(np.mean(np.power(dataFgT0 - pred_FgT0, 2), axis=1))
print(mse_test_pred_FgT0)

dataFgT1originall = pd.read_csv('G:\科研\检测异常度\data\Features\FgT1-5000.csv')
dataFgT1 = (dataFgT1originall - datatrainarrange)/datatrainstd
pred_FgT1 = autoencoder10.predict(dataFgT1)
mse_test_pred_FgT1 = np.array(np.mean(np.power(dataFgT1 - pred_FgT1, 2), axis=1))

dataFgT2originall = pd.read_csv('G:\科研\检测异常度\data\Features\FgT2-5000.csv')
dataFgT2 = (dataFgT2originall - datatrainarrange)/datatrainstd
pred_FgT2 = autoencoder10.predict(dataFgT2)
mse_test_pred_FgT2 = np.array(np.mean(np.power(dataFgT2 - pred_FgT2, 2), axis=1))

dataFgT3originall = pd.read_csv('G:\科研\检测异常度\data\Features\FgT3-5000.csv')
dataFgT3 = (dataFgT3originall - datatrainarrange)/datatrainstd
pred_FgT3 = autoencoder10.predict(dataFgT3)
mse_test_pred_FgT3 = np.array(np.mean(np.power(dataFgT3 - pred_FgT3, 2), axis=1))
length = len(data)+len(dataFgT0)+len(dataFgT1)+len(dataFgT2)+len(dataFgT3)

mse_n =56
n_mse_datatest=np.sum(mse_test>=mse_n)
print(n_mse_datatest)#406
n_mse_dataFgT0=np.sum(mse_test_pred_FgT0>=mse_n)
print(n_mse_dataFgT0)#224315
n_mse_dataFgT1=np.sum(mse_test_pred_FgT1>=mse_n)
print(n_mse_dataFgT1)#211238
n_mse_dataFgT2=np.sum(mse_test_pred_FgT2>=mse_n)
print(n_mse_dataFgT2)#219805
n_mse_dataFgT3=np.sum(mse_test_pred_FgT3>=mse_n)
print(n_mse_dataFgT3)#217762
ε_test = n_mse_datatest/(319281*1000000/819281)
ε_FgT0 = n_mse_dataFgT0/300000
ε_FgT1 = n_mse_dataFgT1/300000
ε_FgT2 = n_mse_dataFgT2/300000
ε_FgT3 = n_mse_dataFgT3/300000
print(mse_n,n_mse_datatest,ε_test,ε_FgT0,ε_FgT1,ε_FgT2,ε_FgT3)

sigma_SM = 1.4548
a = ε_test * sigma_SM
f_Fgt0 = 0.012
f_Fgt1 = 0.02
f_Fgt2 = f_Fgt3 = 0.03
sigma_Fgt0 = 0.00115
sigma_Fgt1 = 0.00138
sigma_Fgt2 = 0.000956
sigma_Fgt3 = 0.000924
b0 = ε_FgT0 * sigma_Fgt0 / (f_Fgt0**2)
b1 = ε_FgT0 * sigma_Fgt1 / (f_Fgt1**2)
b2 = ε_FgT2 * sigma_Fgt2 / (f_Fgt2**2)
b3 = ε_FgT0 * sigma_Fgt3 / (f_Fgt3**2)
print(a, b0, b1, b2, b3)

xsm=np.linspace(0,30,61)#0-30取51个数
s = pd.cut(mse_test, bins=xsm)
print(s.value_counts())
values = s.value_counts().values
print(values)
print(np.sum(values))
xT0 = np.linspace(0,30,61)
sT0 = pd.cut(mse_test_pred_FgT0, bins=xT0)
sT1 = pd.cut(mse_test_pred_FgT1, bins=xT0)
sT2 = pd.cut(mse_test_pred_FgT2, bins=xT0)
sT3 = pd.cut(mse_test_pred_FgT3, bins=xT0)
print(sT0.value_counts())
print(sT1.value_counts())
print(sT2.value_counts())
print(sT3.value_counts())
valuesT0 = sT0.value_counts().values
valuesT1 = sT1.value_counts().values
valuesT2 = sT2.value_counts().values
valuesT3 = sT3.value_counts().values
print(valuesT0)
print(np.sum(valuesT0))
print(valuesT1)
print(np.sum(valuesT1))
print(valuesT2)
print(np.sum(valuesT2))
print(valuesT3)
print(np.sum(valuesT3))

sigma_SM = 1.4548
a0 = ε_test * sigma_SM
f_Fgt0 = 0.012
f_Fgt1 = 0.02
f_Fgt2 = f_Fgt3 = 0.03
sigma_Fgt0 = 0.00115
sigma_Fgt1 = 0.00138
sigma_Fgt2 = 0.000956
sigma_Fgt3 = 0.000924
b0dth = ε_FgT0 * sigma_Fgt0
b0=ε_FgT0 * sigma_Fgt0 / (f_Fgt0**2)
b1dth = ε_FgT0 * sigma_Fgt1
b2dth = ε_FgT2 * sigma_Fgt2
b3dth = ε_FgT0 * sigma_Fgt3
print(mse_n,n_mse_datatest,a0,b0dth, b1dth, b2dth, b3dth)



