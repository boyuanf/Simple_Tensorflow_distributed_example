import tensorflow as tf

cluster_spec = {
    "ps": ["localhost:2221", "localhost:2222"],
    "worker": ["localhost:2223", "localhost:2224"]}

with tf.device(tf.train.replica_device_setter(cluster=cluster_spec)):  # the same as ps_tasks=2
    # with tf.device(tf.train.replica_device_setter(ps_tasks=2)):
    v1 = tf.Variable(1.0)  # use ps
    v2 = tf.Variable(2.0)  # use ps
    s = v1 + v2  # default use task 0
    t = tf.get_variable("t", shape=[20, 20])  # this variable is placed
    # in the parameter server
    # by the replica_device_setter

init = tf.global_variables_initializer()

with tf.Session("grpc://localhost: 2222", config=tf.ConfigProto(log_device_placement=True)) as sess:
    sess.run(init)
    print(s.eval())
    print("v1 device: ", v1.device)
    print("v2 device: ", v2.device)
    print("s device: ", s.device)
    print("t device: ", t.device)
