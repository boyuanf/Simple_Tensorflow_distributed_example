import tensorflow as tf

cluster_spec = {
    "ps": ["localhost:2222"],
    "worker": ["localhost:2223", "localhost:2224"]}
server = tf.train.Server(cluster_spec, job_name="ps", task_index=0)

c = tf.constant("Hello from server1!")
with tf.device(tf.train.replica_device_setter(cluster=cluster_spec)):
  v = tf.get_variable("v", shape=[20, 20])  # this variable is placed
                                            # in the parameter server
                                            # by the replica_device_setter

sess = tf.Session(
    server.target, config=tf.ConfigProto(log_device_placement=True))
print(sess.run(c))
sess.run(v.initializer)
sess.run(v)
server.join()