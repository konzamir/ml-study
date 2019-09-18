from __future__ import absolute_import, division, print_function, unicode_literals

# TensorFlow и tf.keras
import tensorflow as tf
import pandas as pd
from tensorflow import keras
from tensorflow.keras import layers


# Вспомогательные библиотеки
import numpy as np
import matplotlib.pyplot as plt

# print(tf.__version__)

dataset_path = keras.utils.get_file(
    "auto-mpg.data", "http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data")
dataset_path
