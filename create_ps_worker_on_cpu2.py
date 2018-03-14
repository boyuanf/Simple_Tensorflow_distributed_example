import tensorflow as tf

cluster_spec = {
    "ps": ["localhost:2222"],
    "worker": ["localhost:2223", "localhost:2224"]}
server = tf.train.Server(cluster_spec, job_name="worker", task_index=0)

server.join()