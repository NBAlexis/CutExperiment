from keras.models import load_model
import numpy as np
import pandas as pd
from numpy.random import seed
seed(1)
import matplotlib.pyplot as plt
#读取数据
data = pd.read_csv('E:\Autoencoder\Features\SM-1500.csv')
datatest = data[500000:]
datafgt0 = pd.read_csv('E:\Autoencoder\Features\FgT0-1500.csv')
datafgt1 = pd.read_csv('E:\Autoencoder\Features\FgT1-1500.csv')
datafgt2 = pd.read_csv('E:\Autoencoder\Features\FgT2-1500.csv')
datafgt3 = pd.read_csv('E:\Autoencoder\Features\FgT3-1500.csv')
#读取autoencoder1
autoencoder1 = load_model('autoencoder1.h5')
#datatest
pred_datatest = autoencoder1.predict(datatest)
print(pred_datatest)
print(datatest)
mse_test = np.array(np.mean(np.power(datatest - pred_datatest, 2), axis=1))
print(mse_test)
print(len(mse_test))
plt.figure(figsize=(7,5))
plt.hist(mse_test, bins=50, range=(0, 13000))
plt.ylim(0, 90000)
plt.title('mse_test')
plt.xlabel('mse')
plt.savefig("E:\Autoencoder/fig1_test")
#data_fgt0
pred_datafgt0 = autoencoder1.predict(datafgt0)
mse_fgt0 = np.array(np.mean(np.power(datafgt0 - pred_datafgt0, 2), axis=1))
plt.figure(figsize=(7,5))
plt.hist(mse_fgt0, bins=50, range=(0, 500000))
plt.ylim(0, 20000)
plt.title('mse_fgt0')
plt.xlabel('mse')
plt.savefig("E:\Autoencoder/fig2_fgt0")
#data_fgt1
pred_datafgt1 = autoencoder1.predict(datafgt1)
mse_fgt1 = np.array(np.mean(np.power(datafgt1 - pred_datafgt1, 2), axis=1))
plt.figure(figsize=(7,5))
plt.hist(mse_fgt1, bins=50, range=(0, 500000))
plt.ylim(0, 20000)
plt.title('mse_fgt1')
plt.xlabel('mse')
plt.savefig("E:\Autoencoder/fig3_fgt1")
#data_fgt2
pred_datafgt2 = autoencoder1.predict(datafgt2)
mse_fgt2 = np.array(np.mean(np.power(datafgt2 - pred_datafgt2, 2), axis=1))
plt.figure(figsize=(7,5))
plt.hist(mse_fgt2, bins=50, range=(0, 500000))
plt.ylim(0, 20000)
plt.title('mse_fgt2')
plt.xlabel('mse')
plt.savefig("E:\Autoencoder/fig4_fgt2")
#data_fgt3
pred_datafgt3 = autoencoder1.predict(datafgt3)
mse_fgt3 = np.array(np.mean(np.power(datafgt3 - pred_datafgt3, 2), axis=1))
plt.figure(figsize=(7,5))
plt.hist(mse_fgt3, bins=50, range=(0, 500000))
plt.ylim(0, 20000)
plt.title('mse_fgt3')
plt.xlabel('mse')
plt.savefig("E:\Autoencoder/fig5_fgt3")