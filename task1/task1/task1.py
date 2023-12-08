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

# определение метрик 
print('определение метрик')
def precision(y_true, y_pred):
    """метрика точности.
    Вычисляет только пакетное среднее значение точности.

    Вычисляет точность, метрику для классификации с несколькими метками, 
    указывающую, сколько релевантных выбранных элементов.

    """

    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    precision = true_positives / (predicted_positives + K.epsilon())
    return precision

def recall(y_true, y_pred):
    """метрика полноты 
    Вычисляет только среднее значение отзыва по партиям.

    Вычисляет отзыв, метрику для классификации с несколькими метками,
    указывающую, сколько релевантных элементов выбрано.
    """
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    recall = true_positives / (possible_positives + K.epsilon())
    return recall

def f1(y_true, y_pred):
    def recall(y_true, y_pred):
        """метрика полноты 
        Вычисляет только среднее значение отзыва по партиям.

        Вычисляет отзыв, метрику для классификации с несколькими метками,
        указывающую, сколько релевантных элементов выбрано.
        """
        true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
        possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
        recall = true_positives / (possible_positives + K.epsilon())
        return recall

    def precision(y_true, y_pred):
        """метрика точности.
        Вычисляет только пакетное среднее значение точности.

        Вычисляет точность, метрику для классификации с несколькими метками, 
        указывающую, сколько релевантных выбранных элементов.

        """
        true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
        predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
        precision = true_positives / (predicted_positives + K.epsilon())
        return precision

    precision = precision(y_true, y_pred)
    recall = recall(y_true, y_pred)
    return 2 * ((precision * recall) / (precision + recall + K.epsilon()))


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

# загрузка обученной модели
print('загрузка обученной модели')
w2v_model = Word2Vec.load('..\\..\\..\\tasks\\sentiment-analysis-of-tweets-in-russian\\w2v\\tweets_model.w2v')
DIM = w2v_model.vector_size
#  инициализация нулями матрицы слоя векторизации 
print('инициализация нулями матрицы слоя векторизации ')
embedding_matrix = np.zeros((NUM, DIM))

_counter = 0 # счётчик слов из словаря

# Добавление NUM=100000 наиболее часто встречающихся слов из обучающей выборки в слое векторизации
print('Добавление NUM=100000 наиболее часто встречающихся слов из обучающей выборки в слое векторизации')
for word, i in tokenizer.word_index.items():
    _counter += 1
    if i >= NUM:
        break
    #if word in w2v_model.wv.vocab.keys():
    if word in list(w2v_model.wv.index_to_key):
        embedding_matrix[i] = w2v_model.wv[word]
        #print(f'слово - {word}')
    if _counter % 10000 == 0: 
        print(f'прочитано слов из словаря {_counter}')

# построение CNN
print('построение CNN')
tweet_input = Input(shape=(SENTENCE_LENGHT, ), dtype='int32')
tweet_encoder = Embedding(NUM, DIM, input_length=SENTENCE_LENGHT,
                          weights=[embedding_matrix], trainable=False)(tweet_input)

branches = []
x = Dropout(0.2)(tweet_encoder)

for size,  filters_count in [(2, 10), (3, 10), (4, 10), (5, 10)]:
    for i in range(filters_count):
        branch = Conv1D(filters=1, kernel_size=size, padding='valid', activation='relu')(x)
        branch = GlobalAveragePooling1D()(branch)
        branches.append(branch)

x = concatenate(branches, axis=1)
x = Dropout(0.2)(x)
x = Dense(30, activation='relu')(x)
x = Dense(1)(x)
output = Activation('sigmoid')(x)

model = Model(inputs=[tweet_input], outputs=[output])
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=[precision, recall, f1])
model.summary()

# обучение и оценивание CNN
print('обучение и оценивание CNN')
checkpoint = ModelCheckpoint('models\\cnn\\cnn-frozen-embeddings-{epoch:02d}-{val_f1:.2f}.hdf5',
                             monitor = 'val_f1', save_best_only=True, mode='max', period=1)

history = model.fit(np.array(x_train_seq), np.array(y_train), batch_size=32, epochs=10, validation_split=0.25, callbacks=[checkpoint])


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


plot_history(history)



print('запуск модели заморозки')
model.load_weights('models\\cnn\\cnn-frozen-embeddings-09-0.77.hdf5')


predicted = np.round(model.predict(np.array(x_test_seq)))
print(classification_report(np.array(y_test), predicted, digits=5))

model.layers[1].trainable = True
#adam = optimizers.Adam(lr=0.0001)
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



print('Работа программы успешно завершена')

