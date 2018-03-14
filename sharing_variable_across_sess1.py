# simple_client.py
import tensorflow as tf
import sys

#x = tf.Variable(0.0, name="x")
x = tf.get_variable("x", dtype=tf.float32, initializer=0.0)
increment_x = tf.assign(x, x+1)

with tf.Session(sys.argv[1], config=tf.ConfigProto(log_device_placement=True)) as sess:
    if sys.argv[2:] == ["init"]:
        sess.run(x.initializer)
    sess.run(increment_x)
    print(x.eval())