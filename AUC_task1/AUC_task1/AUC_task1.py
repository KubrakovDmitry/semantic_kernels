import pandas as pd
import numpy as np
import re 
from sklearn.model_selection import train_test_split
from keras import backend as K
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from gensim.models import Word2Vec
from keras.layers import Input
from keras.layers.embeddings import Embedding
from keras import optimizers
from keras.layers import Dense, concatenate, Activation, Dropout
from keras.models import Model
from keras.layers.convolutional import Conv1D
from keras.layers.pooling import GlobalAveragePooling1D
from keras.callbacks import ModelCheckpoint
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
import tensorflow as tf


# загрузка данных для обучения и проверки
print('загрузка данных для обучения и проверки') 
n = ['id', 'date', 'name', 'text', 'typr', 'rep', 'rtw', 'faw', 'stcount', 'foll', 'frien', 'listcount']
data_positive = pd.read_csv('..\\..\\..\\tasks\\sentiment-analysis-of-tweets-in-russian\\sentiment data\\positive.csv', sep=';', error_bad_lines=False, names=n, usecols=['text'])
data_negative = pd.read_csv('..\\..\\..\\tasks\\sentiment-analysis-of-tweets-in-russian\\sentiment data\\negative.csv', sep=';', error_bad_lines=False, names=n, usecols=['text'])

sample_size = min(data_positive.shape[0], data_negative.shape[0])
raw_data = np.concatenate((data_positive['text'].values[:sample_size],
                           data_negative['text'].values[:sample_size]), axis=0)
labels = [1] * sample_size + [0] * sample_size

def preprocess_text(text):
    text = text.lower().replace('ё', 'е')
    text = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', 'URL', text)
    text = re.sub('@[^\s]+', 'USER', text)
    text = re.sub('[^a-zA-Zа-яА-Я1-9]+', ' ', text)
    text = re.sub(' +', ' ', text)
    return text.strip()

data = [preprocess_text(t) for t in raw_data]

x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=2)

# подготовка весов для векторизации слоя
print('подготовка весов для векторизации слоя')
SENTENCE_LENGHT = 26
NUM = 100000

def get_sequences(tokenizer, x):
    sequences = tokenizer.texts_to_sequences(x)
    return pad_sequences(sequences, maxlen=SENTENCE_LENGHT)


tokenizer = Tokenizer(num_words = NUM)
tokenizer.fit_on_texts(x_train)

x_train_seq = get_sequences(tokenizer, x_train)
x_test_seq = get_sequences(tokenizer, x_test)

plt.style.use('ggplot')


def plot_metrix(ax, x1, x2, title):
    ax.plot(range(1, len(x1) + 1), x1, label='train')
    ax.plot(range(1, len(x2) + 1), x2, label='val')
    ax.set_ylabel(title)
    ax.set_xlabel('Epoch')
    ax.legend()
    ax.margins(0)


def plot_history(history):
    fig, axes = plt.subplots(ncols=2, nrows=2, figsize=(16, 9))
    ax1, ax2, ax3, ax4 = axes.ravel()

    plot_metrix(ax1, history.history['precision'], history.history['val_precision'], 'Precision')
    plot_metrix(ax2, history.history['recall'], history.history['val_recall'], 'Recall')
    plot_metrix(ax3, history.history['f1'], history.history['val_f1'], "$F_1$")
    plot_metrix(ax4, history.history['loss'], history.history['val_loss'], 'Loss')

    plt.show()


print('запуск модели заморозки')
model.load_weights('models\\cnn\\cnn-frozen-embeddings-09-0.77.hdf5')


predicted = np.round(model.predict(np.array(x_test_seq)))
print(classification_report(np.array(y_test), predicted, digits=5))

model.layers[1].trainable = True
adam = tf.optimizers.Adam(learning_rate=0.0001)
model.compile(loss='binary_crossentropy', optimizer=adam, metrics=[precision, recall, f1])
model.summary()

checkpoint = ModelCheckpoint("models\\cnn\\cnn-trainable-{epoch:02d}-{val_f1:.2f}.hdf5", 
                             monitor='val_f1', save_best_only=True, mode='max', period=1)

history_trainable = model.fit(np.array(x_train_seq), np.array(y_train), batch_size=32, epochs=5, validation_split=0.25, callbacks = [checkpoint])

plot_history(history_trainable)

model.load_weights('models\\cnn\\cnn-trainable-03-0.78.hdf5')
predicted = np.round(model.predict(np.array(x_test_seq)))
print(classification_report(np.array(y_test), predicted, digits=5))



print('Работа программы успешно завершена!')
