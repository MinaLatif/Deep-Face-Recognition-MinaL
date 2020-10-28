import tensorflow as tf
import numpy as np
from tensorflow import keras
from tensorflow import lite

model = tf.keras.models.load_model('Emotion_Voice_Detection_Model.h5')
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_model)

