import tensorflow as tf

with tf.device("/job:local/task:1"):
    c = tf.constant("Hello from server2!")

# 和第一个程序一样的集群配置。集群中的每一个任务需要采用相同的配置。
cluster = tf.train.ClusterSpec(
    {"local": ["localhost:2222", "localhost: 2223", "localhost: 2224"]})
# 指定task_index为1，所以这个程序将在localhost:2223启动服务。
server = tf.train.Server(cluster, job_name="local", task_index=1)
# 剩下的代码都和第一个任务的代码一致。
sess = tf.Session(
    server.target, config=tf.ConfigProto(log_device_placement=True))
print(sess.run(c))
server.join()