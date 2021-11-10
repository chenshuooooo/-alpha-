#����������
import numpy as np
import time
import tensorflow as tf
import matplotlib.pyplot as plt

#ʵʱ������ǿ����
from tensorflow.keras.preprocessing.image import ImageDataGenerator
#�����Կ��ڴ����ָ����Ҫ�İ�
from tensorflow.compat.v1 import ConfigProto
from tensorflow.compat.v1 import InteractiveSession
#�Կ��ڴ����ָ��������
config = ConfigProto()
config.gpu_options.allow_growth = True
session = InteractiveSession(config=config)
#������ȡ
(x_img_train,y_label_train), (x_img_test, y_label_test)=tf.keras.datasets.cifar100.load_data()
#z-score��׼��
mean = np.mean(x_img_train, axis=(0, 1, 2, 3))#�ĸ�ά�� ���� ����x���� ͨ����
std = np.std(x_img_train, axis=(0, 1, 2, 3))

x_img_train = (x_img_train - mean) / (std + 1e-7)#trick ��С���� �����������
x_img_test = (x_img_test - mean) / (std + 1e-7)

#one-hot����ӳ��
y_label_train = tf.keras.utils.to_categorical(y_label_train, 100)
y_label_test = tf.keras.utils.to_categorical(y_label_test, 100)
model = tf.keras.Sequential()

#conv1
model.add(tf.keras.layers.Conv2D(filters=64, kernel_size=[3, 3], input_shape=(32, 32, 3), strides=1,activation='relu',
                                        padding='SAME', kernel_regularizer=tf.keras.regularizers.l2(0.0005)))
model.add(tf.keras.layers.BatchNormalization()) #����׼��
model.add(tf.keras.layers.Dropout(0.3)) #���������Ԫ����ֹ�����
#conv2
model.add(tf.keras.layers.Conv2D(filters=64, kernel_size=[3, 3], strides=1,activation='relu',
                                        padding='SAME', kernel_regularizer=tf.keras.regularizers.l2(0.0005)))
model.add(tf.keras.layers.BatchNormalization())
#���ػ�1
model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))


#conv3
model.add(tf.keras.layers.Conv2D(filters=128, kernel_size=[3, 3], strides=1,activation='relu',
                                        padding='SAME', kernel_regularizer=tf.keras.regularizers.l2(0.0005)))
model.add(tf.keras.layers.BatchNormalization())
model.add(tf.keras.layers.Dropout(0.4))
#conv4
model.add(tf.keras.layers.Conv2D(filters=128, kernel_size=[3, 3], strides=1,activation='relu',
                                        padding='SAME', kernel_regularizer=tf.keras.regularizers.l2(0.0005)))
model.add(tf.keras.layers.BatchNormalization())
#���ػ�2
model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))



#conv5
model.add(tf.keras.layers.Conv2D(filters=256, kernel_size=[3, 3], strides=1,activation='relu',
                                        padding='SAME', kernel_regularizer=tf.keras.regularizers.l2(0.0005)))
model.add(tf.keras.layers.BatchNormalization())
model.add(tf.keras.layers.Dropout(0.4))
#conv6
model.add(tf.keras.layers.Conv2D(filters=256, kernel_size=[3, 3], strides=1,activation='relu',
                                        padding='SAME', kernel_regularizer=tf.keras.regularizers.l2(0.0005)))
model.add(tf.keras.layers.BatchNormalization())
model.add(tf.keras.layers.Dropout(0.4))
#conv7
model.add(tf.keras.layers.Conv2D(filters=256, kernel_size=[3, 3], strides=1,activation='relu',
                                        padding='SAME', kernel_regularizer=tf.keras.regularizers.l2(0.0005)))
model.add(tf.keras.layers.BatchNormalization())
#���ػ�3
model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))


#conv8
model.add(tf.keras.layers.Conv2D(filters=512, kernel_size=[3, 3], strides=1,activation='relu',
                                        padding='SAME', kernel_regularizer=tf.keras.regularizers.l2(0.0005)))
model.add(tf.keras.layers.BatchNormalization())
model.add(tf.keras.layers.Dropout(0.4))
#conv9
model.add(tf.keras.layers.Conv2D(filters=512, kernel_size=[3, 3], strides=1,activation='relu',
                                        padding='SAME', kernel_regularizer=tf.keras.regularizers.l2(0.0005)))
model.add(tf.keras.layers.BatchNormalization())
model.add(tf.keras.layers.Dropout(0.4))
#conv10
model.add(tf.keras.layers.Conv2D(filters=512, kernel_size=[3, 3], strides=1,activation='relu',
                                        padding='SAME', kernel_regularizer=tf.keras.regularizers.l2(0.0005)))
model.add(tf.keras.layers.BatchNormalization())
#���ػ�4
model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))


#conv11
model.add(tf.keras.layers.Conv2D(filters=512, kernel_size=[3, 3], strides=1,activation='relu',
                                        padding='SAME', kernel_regularizer=tf.keras.regularizers.l2(0.0005)))
model.add(tf.keras.layers.BatchNormalization())
model.add(tf.keras.layers.Dropout(0.4))
#conv12
model.add(tf.keras.layers.Conv2D(filters=512, kernel_size=[3, 3], strides=1,activation='relu',
                                        padding='SAME', kernel_regularizer=tf.keras.regularizers.l2(0.0005)))
model.add(tf.keras.layers.BatchNormalization())
model.add(tf.keras.layers.Dropout(0.4))
#conv13
model.add(tf.keras.layers.Conv2D(filters=512, kernel_size=[3, 3], strides=1,activation='relu',
                                        padding='SAME', kernel_regularizer=tf.keras.regularizers.l2(0.0005)))
model.add(tf.keras.layers.BatchNormalization())
#���ػ�5
model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))

#ȫ���� MLP����
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dropout(rate=0.5))


model.add(tf.keras.layers.Dense(units=512,activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.0005)))
model.add(tf.keras.layers.BatchNormalization())
model.add(tf.keras.layers.Dense(units=100))
model.add(tf.keras.layers.Activation('softmax'))
#�鿴ժҪ
model.summary()
#������
training_epochs = 60
batch_size = 128
learning_rate = 0.1
momentum = 0.9 #SGD���ٶ���
lr_decay = 1e-6 #ѧϰ˥��
lr_drop = 20 #˥������

tf.random.set_seed(777)#�ɸ���
def lr_scheduler(epoch):
    return learning_rate * (0.5 ** (epoch // lr_drop))

reduce_lr = tf.keras.callbacks.LearningRateScheduler(lr_scheduler)
datagen = ImageDataGenerator(
    featurewise_center=False,  # ����ֵ�����������ݵľ�ֵ����Ϊ 0�����������С�
    samplewise_center=False,  # ����ֵ����ÿ�������ľ�ֵ����Ϊ 0��
    featurewise_std_normalization=False,  # ����ֵ��������������ݱ�׼����������С�
    samplewise_std_normalization=False,  # ����ֵ����ÿ������������׼�
    zca_whitening=False,  # ����ֵ���Ƿ�Ӧ�� ZCA �׻���
    #zca_epsilon  ZCA �׻��� epsilon ֵ��Ĭ��Ϊ 1e-6��
    rotation_range=15,  # �����������ת�Ķ�����Χ (degrees, 0 to 180)
    width_shift_range=0.1,  # randomly shift images horizontally (fraction of total width)
    height_shift_range=0.1,  # randomly shift images vertically (fraction of total height)
    horizontal_flip=True,  # ����ֵ�����ˮƽ��ת��
    vertical_flip=False)  # ����ֵ�������ֱ��ת��

datagen.fit(x_img_train)
#�����Ż���
optimizer = tf.keras.optimizers.SGD(learning_rate=learning_rate,
                                    decay=1e-6, momentum=momentum, nesterov=True)
#�����ء��Զ����Ż��������۱�׼��
model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])


t1=time.time()
model.fit(datagen.flow(x_img_train, y_label_train,
                                 batch_size=batch_size), epochs=training_epochs, verbose=2, callbacks=[reduce_lr],
                    steps_per_epoch=x_img_train.shape[0] // batch_size, validation_data=(x_img_test, y_label_test))
t2=time.time()
CNNfit = float(t2-t1)
print("Time taken: {} seconds".format(CNNfit))
scores = model.evaluate(x_img_test,
                        y_label_test, verbose=0)
scores[1]