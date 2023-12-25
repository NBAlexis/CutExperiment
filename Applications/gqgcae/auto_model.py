import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
from tensorflow.python.keras.layers import LeakyReLU, PReLU
from tensorflow.python.keras.activations import linear
from tensorflow.keras.models import Sequential
from keras.callbacks import ModelCheckpoint
from keras.optimizers import Adam

# 取数据 X_train 40万；X_validation 10万；剩下为test 作为hist画曲线
data = np.loadtxt('../Features/SM-1500.csv', delimiter=',')
print(data)
datatrain = data[0:400000]
datavalidation = data[400000:500000]

meantrain = np.mean(datatrain, axis=0)
stdtrain = np.std(datatrain, axis=0)

datatrain = (datatrain - meantrain) / stdtrain
datavalidation = (datavalidation - meantrain) / stdtrain

print(np.shape(datatrain))
print(np.shape(datavalidation))

# datatest = data[500000:]
# print(datatrain,datavalidation,datatest)
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
num_epoch = 800
batch_size = 32
checkpointer = ModelCheckpoint(filepath="autoencoder1.h5",
                               verbose=0,
                               save_best_only=True)
autoencoder1 = autoencoder.fit(datatrain, datatrain,
                               epochs=num_epoch,
                               batch_size=batch_size,
                               shuffle=True,
                               validation_data=(datavalidation, datavalidation),
                               verbose=1,
                               callbacks=[checkpointer]).history
# 可视化
plt.figure(figsize=(14, 5))
plt.plot(autoencoder1["loss"], c='dodgerblue', lw=3)
plt.plot(autoencoder1["val_loss"], c='coral', lw=3)
plt.title('model loss')
plt.ylabel('mse');
plt.xlabel('epoch')
plt.legend(['train', 'validation'], loc='upper right')
plt.show()

print(autoencoder1["loss"])
print(autoencoder1["val_loss"])