import io
record_iterator = tf.python_io.tf_record_iterator(path="tfrecords/tfrecords_valid_frontal-00000-of-00003.tfrecord")
record_file='new.tfrecord'      

with tf.io.TFRecordWriter(record_file) as writer:
        
    for string_record in record_iterator:
        example = tf.train.Example()
        example.ParseFromString(string_record)
        image_feature=example.features.feature['jpg_bytes'].bytes_list.value[0]

        # from Byte to Img
        imageStream = io.BytesIO(image_feature)
        imageOrigin = Image.open(imageStream)
        
        #Replace your function here
        image_moire=moire_pattern(imageOrigin)
        
        # from Img to Byte
        imgByteArr = io.BytesIO()
        image_moire.save(imgByteArr, format='JPEG')
        imgByteArr = imgByteArr.getvalue()       
        
        # Put it back to tf_record
        example.features.feature['jpg_bytes'].bytes_list.value[0]=imgByteArr        
        writer.write(example.SerializeToString())
