import tensorflow as tf

# 和第一个程序一样的集群配置。集群中的每一个任务需要采用相同的配置。
cluster = tf.train.ClusterSpec(
    {"local": ["localhost:2222", "localhost: 2223", "localhost: 2224"]})
# 指定task_index为2，所以这个程序将在localhost:2224启动服务。
server = tf.train.Server(cluster, job_name="local", task_index=2)

server.join()