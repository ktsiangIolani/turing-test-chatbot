# Run this cell to import libraries and check that tensorflow is properly installed
import pandas as pd
import numpy as np
import math
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import plotly.express as px
import tensorflow as tf

# TODO Load penguins.csv
data = pd.read_csv("classifcation_and_seqs_aln.csv")

#TODO Handle NA Values

# TODO encode string data using LabelEncoder
encoder = LabelEncoder()
encoded = []

data["species"] = encoder.fit_transform(data["species"])

for sequence in data["sequence"].tolist():
    mini_encoded = []
    for char in sequence:
        if char == "-":
            mini_encoded.append(0)
        if char == "A":
            mini_encoded.append(1)
        if char == "T":
            mini_encoded.append(2)
        if char == "C":
            mini_encoded.append(3)
        if char == "G":
            mini_encoded.append(4)
    encoded.append(mini_encoded)

    
#TODO Select your features. Select body_mass_g as your "target" (y) and everything else as X
y = data["species"]
X = np.array(encoded)

print(np.unique(data['species']))

# TODO : Split the data into testing and training data. Use a 20% split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.8, random_state = 42)


# TODO create a neural network with tensorflow
model = tf.keras.models.Sequential([
    tf.keras.layers.Input(shape=(4795,)),
    tf.keras.layers.Dense(272, activation='relu'),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dense(136, activation='relu'),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dense(68, activation='relu'),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dense(34, activation='softmax')
])

# TODO set your learning rate
lr = 0.0004

#TODO Compile your model with a selected optimizer and loss function
model.compile(
    loss=tf.keras.losses.SparseCategoricalCrossentropy(),
    optimizer=tf.keras.optimizers.Adam(learning_rate=lr),
    metrics=['accuracy']
)

# TODO: fit your model with X_train and Y_train
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=200)

#Run this cell to graph your loss
df = pd.DataFrame(history.history)['loss']
px.scatter(df).show()