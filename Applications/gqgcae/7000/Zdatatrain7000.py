import numpy as np
from tensorflow import keras
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from keras.callbacks import ModelCheckpoint
import pandas as pd #用于数据输出
# 取数据 X_train 40万；X_validation 10万；剩下为test 作为hist画曲线
dataoriginal = np.loadtxt('G:\科研\检测异常度\data\Features\SM-7000.csv', delimiter=',')
print(dataoriginal)
datatrain = dataoriginal[0:400000]
datavalidation = dataoriginal[400000:500000]
meantrain = np.mean(datatrain, axis=0)
stdtrain = np.std(datatrain, axis=0)
datatrain = (datatrain - meantrain) / stdtrain
datavalidation = (datavalidation - meantrain) / stdtrain
print(np.shape(datatrain))
print(np.shape(datavalidation))
# 构建autoencoder
encoder = keras.Sequential([
    keras.layers.Dense(8, activation='LeakyReLU', input_shape=[8]),
    keras.layers.Dense(4, activation='LeakyReLU'),
    keras.layers.Dense(2, activation='linear')
])
decoder = keras.Sequential([
    keras.layers.Dense(4, activation='LeakyReLU', input_shape=[2]),
    keras.layers.Dense(8, activation='LeakyReLU'),
    keras.layers.Dense(8, activation='linear')
])

adamoptimizer = keras.optimizers.Adam(lr=0.0005)

autoencoder = Sequential()
autoencoder.add(encoder)
autoencoder.add(decoder)
autoencoder.compile(loss='mse', optimizer=adamoptimizer, metrics=['mae'])
autoencoder.summary()
# 训练
num_epoch = 500
batch_size = 32
checkpointer = ModelCheckpoint(filepath="autoencoder14.h5",
                               verbose=0,
                               save_best_only=True)
autoencoder14 = autoencoder.fit(datatrain, datatrain,
                               epochs=num_epoch,
                               batch_size=batch_size,
                               shuffle=True,
                               validation_data=(datavalidation, datavalidation),
                               verbose=1,
                               callbacks=[checkpointer]).history

encoder.save('encoder.h5')
# 可视化
plt.figure(figsize=(14, 5))
plt.plot(autoencoder14["loss"], c='dodgerblue', lw=3)
plt.plot(autoencoder14["val_loss"], c='coral', lw=3)
plt.title('model loss')
plt.ylabel('mse');
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='upper right')
plt.show()
print(autoencoder14["loss"])
print(autoencoder14["val_loss"])

#输出数据到CSV文件
list1=autoencoder14["loss"]
list2=autoencoder14["val_loss"]
list=[]
list.append(list1)
list.append(list2)
print(list)
test=pd.DataFrame(data=list)#将数据放进表格
test.to_csv('14TeVautoencoder1loss.csv') #数据存入csv,存储位置及文件名称


