from tensorflow.keras.layers import GlobalAveragePooling2D
from tensorflow.keras.layers import GlobalMaxPooling2D
from tensorflow.keras.layers import Concatenate
from tensorflow.keras.layers import Activation
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.metrics import binary_crossentropy, categorical_crossentropy
from sklearn.metrics import confusion_matrix, accuracy_score
from tensorflow.keras import backend as K
from tqdm import tqdm
import efficientnet.tfkeras as efn
import tensorflow as tf
import pandas as pd
import numpy as np
import logging
import cv2
import os

#load the model
import glob
import cv2 

model = tf.keras.models.load_model("C:/Users/Rajesh.Mandal/Downloads/ML_Practice/ML_Project/fake_logo/Fake_logo_classification.h5",compile = False)
class_name = ['Adidas','Puma','Samsung','Twitter','fake_adidas','fake_puma','fake_samsung','fake_twitter']

# dest_path = 'C:\Users\Rajesh.Mandal\Downloads\ML_Practice\ML_Project\fake_logo\result'
dest_path = 'C:/Users/Rajesh.Mandal/Downloads/ML_Practice/ML_Project/fake_logo/result/'

#load all the images
for i in glob.glob("C:/Users/Rajesh.Mandal/Downloads/ML_Practice/ML_Project/fake_logo/data/test/*"):
  file_name = i.split('\\')[-1]
  img1 = cv2.imread(i)
  img = cv2.resize(img1, (224,224))

  # convert the image to a tensor for inference
  img = np.expand_dims(img, 0).astype(np.float32) / 255.0
  preds = np.squeeze(model.predict(img)[0]) 
  index = np.argmax(preds)
  cls_name =class_name[index]
  print(file_name," : ",cls_name)
  cv2.putText(img1, cls_name, (50,50), cv2.FONT_HERSHEY_SIMPLEX, 
                   1, (255, 0, 0), 3, cv2.LINE_AA)
  
  cv2.imwrite(dest_path+file_name,img1)
#   cv2.imshow()
  cv2.imshow(cls_name, cv2.resize(img1,(224,224)))

    # Wait for a key press and close the window
  cv2.waitKey(0)
  cv2.destroyAllWindows()

  print(f"Image saved to: {dest_path}")
  if 'f' in class_name:
    print("The uploaded image belongs to ",class_name ,"class." + ", and " + "it is a fake logo of", class_name.replace('fake_','').capitalize())
  else:
    print("The uploaded image belongs to ",class_name ,"class." + ", and " + "it is not a fake logo of", class_name)

print("prediction done!!!!")
 