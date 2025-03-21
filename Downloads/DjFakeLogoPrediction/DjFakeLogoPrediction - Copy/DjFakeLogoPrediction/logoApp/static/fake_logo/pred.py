import pandas as pd
import numpy as np
import cv2
import efficientnet.tfkeras as efn
from keras.models import load_model
import tensorflow as tf
import warnings
warnings.filterwarnings("ignore")

class_name = ['Adidas','Puma','Samsung','Twitter','fake_adidas','fake_puma','fake_samsung','fake_twitter']
model_path = "C:/Users/Rajesh.Mandal/Downloads/ML_Practice/ML_Project/fake_logo/Fake_logo_classification.h5"
img_path = "C:/Users/Rajesh.Mandal/Downloads/ML_Practice/ML_Project/fake_logo/data/test/org_puma (1).jpg"  

#load the model
model = tf.keras.models.load_model(model_path,compile = False)

def pred_result(img_path):
    img = cv2.imread(img_path)
    img = cv2.resize(img, (224,224))
    # convert the image to a tensor for inference
    img = np.expand_dims(img, 0).astype(np.float32) / 255.0
    preds = np.squeeze(model.predict(img)[0])
    #preds will give the probability score of 
    index = np.argmax(preds)
    max_prob = np.amax(preds)
    return preds, max_prob, class_name[index], index

# preds,max_prob, class_name = pred_result(img_path,model_path)
preds,max_prob, class_name, index = pred_result(img_path)
print("prediction:",preds) 
print("highest probability:",max_prob)

if 'f' in class_name:
  print("The uploaded image belongs to ",class_name ,"class." + ", and " + "it is a fake logo of", class_name.replace('fake_','').capitalize())
else:
  print("The uploaded image belongs to ",class_name ,"class." + ", and " + "it is not a fake logo of", class_name)
   

    