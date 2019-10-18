import io
record_iterator = tf.python_io.tf_record_iterator(path="tfrecords/tfrecords_valid_frontal-00000-of-00003.tfrecord")
record_file='new.tfrecord'      

with tf.io.TFRecordWriter(record_file) as writer:
        
    for string_record in record_iterator:
        example = tf.train.Example()
        example.ParseFromString(string_record)
        image_feature=example.features.feature['jpg_bytes'].bytes_list.value[0]

        imageStream = io.BytesIO(image_feature)
        imageOrigin = Image.open(imageStream)
        
        #Replace your function here
        image_moire=moire_pattern(imageOrigin)
        
        imgByteArr = io.BytesIO()
        image_moire.save(imgByteArr, format='JPEG')
        imgByteArr = imgByteArr.getvalue()       
        
        example.features.feature['jpg_bytes'].bytes_list.value[0]=imgByteArr
        
        patient_num=example.features.feature['patient'].int64_list.value[0]
        writer.write(example.SerializeToString())
