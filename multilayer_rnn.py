import tensorflow as tf
import pandas as pd
import numpy as np
import os
import matplotlib as plt
import random
import csv
from sklearn.utils import shuffle
import sys
from sklearn import preprocessing

'''hyper parameter'''
seq_length = 10
data_dim = 20
# hidden_dim = 10
output_dim = 2
learning_rate = 0.001
training_epochs = 1000
batch_size = 256

directory = 'data/'

# '091990','215600','035760','084990','003670','086900','028300',
#                '253450','263750','025980','068760','034230','036490','078340',
#                '145020','095700','056190','046890','041960','028150','003380',
#                '098460','041510','042000','192080','035900','178920','022100',
#                '036830','038540','048260','240810','102940',
# '000250','066970',
#                '122870','183490',

jongmoklist = ['140410','058470','086520','036420','092040',
               '083790','069080','200230','030190','073070','007390','267980']

# global_step = tf.Variable(0, trainable=False, name='global_step')

X_pre = tf.placeholder(tf.float32, [None, 200],name='X_pre')
X = tf.reshape(X_pre, [-1, data_dim, seq_length],name='X')
# X_BN = tf.layers.batch_normalization(X) #batch_norm
Y = tf.placeholder(tf.float32, [None, output_dim],name='Y')

"""multi layer rnn"""
cells = []
cell_1 = tf.nn.rnn_cell.GRUCell(num_units=16,activation=tf.nn.softsign)
# cell_1 = tf.nn.rnn_cell.BasicLSTMCell(num_units=16, state_is_tuple=True,name='rnn_layer_1')
cells.append(cell_1)
cell_2 = tf.nn.rnn_cell.GRUCell(num_units=8,activation=tf.nn.softsign)
# cell_2 = tf.nn.rnn_cell.BasicLSTMCell(num_units=8, state_is_tuple=True,name='rnn_layer_2')
cells.append(cell_2)
# cell_3 = tf.nn.rnn_cell.BasicLSTMCell(num_units=4, state_is_tuple='rnn_layer_3')
# cells.append(cell_3)

cell = tf.nn.rnn_cell.MultiRNNCell(cells)

outputs, _states = tf.nn.dynamic_rnn(cell, X, dtype=tf.float32) #X_BN
Y_pred = tf.contrib.layers.fully_connected(outputs[:, -1], output_dim, activation_fn=tf.nn.sigmoid)  # We use the last cell's output

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=Y_pred, labels=Y))
train = tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)


for jongmok in jongmoklist:
    '''data preprocessing'''
    print(jongmok,'_processing')
    train_file = directory + jongmok + '_10_5_train.csv'
    test_file = directory + jongmok + '_10_5_test.csv'

    x_data = pd.read_csv(train_file)
    x_data2 = np.array(x_data) #numpy로 변환
    x_data2 = preprocessing.minmax_scale(x_data2.T).T
    x_data2 = np.ravel(x_data2,order='C') #데이터 1줄로 변환

    train_input = np.reshape(x_data2, (-1, 200))
    train_input = np.array(train_input).astype(np.float32)


    t_0 = np.repeat(0,int(len(x_data)/20))
    t_1 = np.repeat(1,int(len(x_data)/20))

    train_label = np.concatenate((t_0,t_1),axis=None)
    train_label = pd.DataFrame(train_label).astype(str)
    train_label = pd.get_dummies(train_label)
    train_label = np.array(train_label)



    x_data_test = pd.read_csv(test_file)
    x_data_test2 = np.array(x_data_test)
    x_data_test2 = np.ravel(x_data_test2,order='C')

    test_input = np.reshape(x_data_test2, (-1, 200))
    test_input = np.array(test_input).astype(np.float32)

    t_0_test = np.repeat(0,int(len(x_data_test)/20))
    t_1_test = np.repeat(1,int(len(x_data_test)/20))

    test_label = np.concatenate((t_0_test,t_1_test),axis=None)
    test_label = pd.DataFrame(test_label).astype(str)
    test_label = pd.get_dummies(test_label)
    test_label = np.array(test_label)

    train_input, train_label = shuffle(train_input, train_label)  # shuffle
    test_input, test_label = shuffle(test_input, test_label)  # shuffle

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())


        merged = tf.summary.merge_all()
        writer = tf.summary.FileWriter('./logs', sess.graph)

        # tensorboard --logdir=./logs
        # http://localhost:6006

        print('Learning started. It takes sometime.')
        for epoch in range(training_epochs):
            avg_cost = 0
            total_batch = int(len(train_input) / batch_size)

            train_input, train_label = shuffle(train_input, train_label)  # shuffle
            # print(train_input[:1])

            for i in range(total_batch):
                start = ((i + 1) * batch_size) - batch_size
                end = ((i + 1) * batch_size)
                batch_xs = train_input[start:end]
                batch_ys = train_label[start:end]
                feed_dict = {X_pre: batch_xs, Y: batch_ys}
                c, _ = sess.run([cost, train], feed_dict=feed_dict)
                avg_cost += c / total_batch

                # summary = sess.run(merged, feed_dict=feed_dict)
                # writer.add_summary(summary, global_step=sess.run(global_step))
                writer.add_graph(sess.graph)

            print('Epoch:', '%04d' % (epoch + 1), 'cost =', '{:.9f}'.format(avg_cost))

        print('Learning Finished!')

        correct_prediction = tf.equal(tf.argmax(Y_pred, 1), tf.argmax(Y, 1))
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
        train_accuracy = sess.run(accuracy, feed_dict={X_pre: train_input, Y: train_label})
        train_accuracy = np.array(train_accuracy)
        test_accuracy = sess.run(accuracy, feed_dict={X_pre: test_input, Y: test_label})
        test_accuracy = np.array(test_accuracy)
        print('train_accuracy', train_accuracy)
        print('----------------')
        print('test_accuaracy', test_accuracy)
        save_path = './accuracy/'+ jongmok + '_accuracy.csv'
        df = pd.DataFrame({'train_Accuracy':train_accuracy, 'test_accuracy':test_accuracy},index=[0])
        df.to_csv(save_path, index=False)
        # print("Train Accuracy:", sess.run(accuracy, feed_dict={X_pre: train_input, Y: train_label}))
        # print("Test Accuracy:", sess.run(accuracy, feed_dict={X_pre: test_input, Y: test_label}))
        # print(sess.run(tf.nn.softmax(Y_pred),feed_dict={X_pre: test_input}))
        # print(test_label)

        saver = tf.train.Saver()
        save_path = saver.save(sess, "./model/" + jongmok + "/" + jongmok + "_" + "GRU-model.ckpt") #


        # np.savetxt(jongmok + "_accuracy.csv", train_accuracy, delimiter=",")
        # np.savetxt("prediction.csv", test_accuracy, delimiter=",")