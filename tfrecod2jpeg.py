import tensorflow as tf

import numpy as np

record_iterator = tf.python_io.tf_record_iterator(path="tfrecords/tfrecords_train_frontal-00004-of-00012.tfrecord")

for string_record in record_iterator:
    example = tf.train.Example()
    example.ParseFromString(string_record)
    image_feature=example.features.feature['jpg_bytes'].bytes_list.value[0]
    
    patient_num=example.features.feature['patient'].int64_list.value[0]
    
    with open('jpg_format/'+str(patient_num)+'.jpg', 'wb') as fd:
        fd.write(image_feature)
