import tensorflow as tf

with tf.device("/job:local/task:1/cpu:0"):
    a = tf.constant(1.0)

with tf.device("/job:local/task:2/cpu:0"):
    b = a + 2

c = a * 3

# set "grpc://localhost: 2223" , means the session will execute on machine2, however,
# it runs on the device that we specific above: a on task0, b on task12, c on task1(auto assigned)
with tf.Session("grpc://localhost: 2223", config=tf.ConfigProto(log_device_placement=True)) as sess:
    print(c.eval())

