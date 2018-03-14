import tensorflow as tf

a = tf.constant(1.0)
b = a + 2
c = a * 3

# set "grpc://localhost: 2224" , means the session will execute on machine3, however,
# it may not use the job on that machine (a, b, c all executed using task0),
# as Tensorflow will optimize assign the resource at the cluster level
with tf.Session("grpc://localhost: 2224", config=tf.ConfigProto(log_device_placement=True)) as sess:
    print(c.eval())