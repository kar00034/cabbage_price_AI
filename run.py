import tensorflow as tf
import numpy as np

def run(save_path):
    X = tf.placeholder(tf.float32, shape=[None, 4])
    Y = tf.placeholder(tf.float32, shape=[None, 1])
    W = tf.Variable(tf.random_normal([4, 1]), name="weight")
    b = tf.Variable(tf.random_normal([1]), name="bias")

    hypothesis = tf.matmul(X, W) + b
    saver = tf.train.Saver()
    model = tf.global_variables_initializer()

    avg_temp = float(input('평균 온도:'))
    min_temp = float(input('최저 온도:'))
    max_temp = float(input('최고 온도:'))
    rain_fall = float(input('강수량:'))

    with tf.Session() as sess:
        sess.run(model)


        saver.restore(sess, save_path)

        data = ((avg_temp, min_temp, max_temp, rain_fall), )
        arr = np.array(data, dtype=np.float32)

        x_data = arr[:4]
        dict = sess.run(hypothesis, feed_dict={X: x_data})
        print(dict[0])

# 15.5 3.5 20.5 5

#
# if __name__ == "__main__":
#     save_path = "./data/saved.cpkt"
#     run(save_path)