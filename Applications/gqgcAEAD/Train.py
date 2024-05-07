import numpy as np
from tensorflow import keras
import matplotlib.pyplot as plt
from keras.callbacks import ModelCheckpoint
from keras.models import Sequential

batch_size = 32
adamlr = 0.0005
num_epoch = 2000

for latent in [2, 3, 4]:
    for energy in ["1500", "5000", "7000", "15000"]:
        train = np.loadtxt('../datas/SMTrain-{}.csv'.format(energy), delimiter=',')
        validation = np.loadtxt('../datas/SMValidation-{}.csv'.format(energy), delimiter=',')
        encoder = keras.Sequential([
            keras.layers.Dense(8, activation='LeakyReLU', input_shape=[8]),
            keras.layers.Dense(4, activation='LeakyReLU'),
            keras.layers.Dense(latent, activation='linear')
        ])
        decoder = keras.Sequential([
            keras.layers.Dense(4, activation='LeakyReLU', input_shape=[latent]),
            keras.layers.Dense(8, activation='LeakyReLU'),
            keras.layers.Dense(8, activation='linear')
        ])
        adamoptimizer = keras.optimizers.Adam(lr=adamlr)
        autoencoder = Sequential()
        autoencoder.add(encoder)
        autoencoder.add(decoder)
        autoencoder.compile(loss='mse', optimizer=adamoptimizer, metrics=['mae'])
        checkpointer = ModelCheckpoint(filepath="../networks/s32ae{}-{}-{}.h5".format(latent, energy, num_epoch),
                                       verbose=0,
                                       save_best_only=True)
        autoencoder3 = autoencoder.fit(train, train,
                                       epochs=num_epoch,
                                       batch_size=batch_size,
                                       shuffle=True,
                                       validation_data=(validation, validation),
                                       verbose=1,
                                       callbacks=[checkpointer]).history
        encoder.save('../networks/s32encoder{}-{}-{}.h5'.format(latent, energy, num_epoch))
        list1 = autoencoder3["loss"]
        list2 = autoencoder3["val_loss"]
        list3 = autoencoder3["mae"]
        list4 = autoencoder3["val_mae"]
        np.savetxt('../results/s32history{}-{}-{}.csv'.format(latent, energy, num_epoch), np.array([list1, list2, list3, list4]), delimiter=',')
        plt.plot(range(num_epoch), list1)
        plt.plot(range(num_epoch), list2)
        plt.plot(range(num_epoch), list3)
        plt.plot(range(num_epoch), list4)
        plt.show()
