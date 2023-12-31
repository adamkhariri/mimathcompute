# -*- coding: utf-8 -*-
"""svm-soybean-leaf-disease.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/adamkhariri/84429d723375c1b736ab9823c52fcde8/svm-soybean-leaf-disease.ipynb
"""

import cv2
import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt
from PIL import Image
# from skimage import data
from google.colab import drive, files
drive.mount('/content/drive')

from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from skimage.feature import greycomatrix, greycoprops
from sklearn.model_selection import train_test_split
import os

# Define the path to the folders containing the images
caterpillar_folder = "/content/drive/MyDrive/Archive_SVM/Caterpillar"
diabrotica_folder = "/content/drive/MyDrive/Archive_SVM/Diabrotica_speciosa"
healthy_folder = "/content/drive/MyDrive/Archive_SVM/Healthy"

# Initialize an empty list to store the dataset
dataset = []

# Function to process images in a folder
def process_folder(folder, label):
    for filename in os.listdir(folder):
        if filename.endswith(".jpg"):
            image_path = os.path.join(folder, filename)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            # Calculate GLCM properties for the entire image
            glcm = greycomatrix(image, distances=[5], angles=[0], levels=256, symmetric=True, normed=True)
            dissimilarity = greycoprops(glcm, 'dissimilarity')[0, 0]
            correlation = greycoprops(glcm, 'correlation')[0, 0]

            dataset.append([dissimilarity, correlation, label])

# Process images in the "caterpillar" folder (label 0)
process_folder(caterpillar_folder, 0)

# Process images in the "diabrotica" folder (label 1)
process_folder(diabrotica_folder, 1)

# Process images in the "healthy" folder (label 2)
process_folder(healthy_folder, 2)

# Create a DataFrame for the dataset
column_names = ["Dissimilarity", "Correlation", "Label"]
df = pd.DataFrame(dataset, columns=column_names)

# Split the dataset into features (X) and the target variable (y)
X = df[["Dissimilarity", "Correlation"]]
y = df["Label"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=45)

# Create an SVM classifier
svm_classifier = SVC(kernel='rbf', C=1.0)

# Train the classifier on the training data
svm_classifier.fit(X_train, y_train)

# Make predictions on the test data
y_pred = svm_classifier.predict(X_test)

# Evaluate the classifier's performance
accuracy = accuracy_score(y_test, y_pred)
confusion_mat = confusion_matrix(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

# Plot and display the confusion matrix
plt.figure(figsize=(6, 5))
sns.heatmap(confusion_mat, annot=True, fmt='d', cmap='Blues', xticklabels=["Caterpillar", "Diabrotica", "Healthy"], yticklabels=["Caterpillar", "Diabrotica", "Healthy"])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()

# print("Confusion Matrix:")
# print("TN (True Negative):", confusion_mat[0, 0])
# print("FP (False Positive):", confusion_mat[0, 1])
# print("FN (False Negative):", confusion_mat[1, 0])
# print("TP (True Positive):", confusion_mat[1, 1])

print(f"Accuracy: {accuracy:.2f}")
print("\nClassification Report:\n", classification_rep)