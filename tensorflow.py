import tensorflow as tf
import numpy as np

input_data = np.array([[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0],
[2.0,3.0,4.0,5.0,1.0]])




model = tf.keras.Sequential()
model.add(tf.keras.Input((5,)))
# tf.keras.layers.Dense格式
# tf.keras.layers.Dense(
#     units, activation=None, use_bias=True,
#     kernel_initializer='glorot_uniform',
#     bias_initializer='zeros', kernel_regularizer=None,
#     bias_regularizer=None, activity_regularizer=None, kernel_constraint=None,
#     bias_constraint=None, **kwargs
# )
model.add(tf.keras.layers.Dense(1000,activation="softmax"))
model.add(tf.keras.layers.Dense(1000,activation="softmax"))
model.add(tf.keras.layers.Dense(1000,activation="softmax"))
model.add(tf.keras.layers.Dense(2,activation="softmax"))
# model.compile裡面的metrics要放專有名詞，像是"acc"是專用的
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.01),\
              loss=tf.keras.losses.CategoricalCrossentropy(),\
              metrics=["acc"])
y_train = np.eye(80)
# model.fit(x=輸入的data，
# y=答案，batch_size調高，算較少梯度，調低則算較多梯度，
# epochs算一個檔案:計算多少次，可以算降低loss_fuction，也可以算更精準，
# verbose是代表顯示的模式)
# batch_size調高，建議epochs也跟著調高
his = model.fit(x = input_data, y = y_train, batch_size=1, epochs=10, verbose=2)
