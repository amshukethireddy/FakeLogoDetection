import pandas as pd
import numpy as np
import cv2
import efficientnet.tfkeras as efn
from keras.models import load_model
import tensorflow as tf
import warnings

warnings.filterwarnings("ignore")

def pred_result(img_path, model_path):
    # model_path = os.path.join(settings.BASE_DIR, 'fake_logo', 'Fake_logo_classification.h5')
    class_name = ['Adidas', 'Puma', 'Samsung', 'Twitter', 'fake_adidas', 'fake_puma', 'fake_samsung', 'fake_twitter']

    model = load_model(model_path, compile=False)
    file_name = img_path.split('/')[-1]
    print("file name: ", file_name)
    img1 = cv2.imread(img_path)
    img = cv2.resize(img1, (224, 224))
    # convert the image to a tensor for inference
    img = np.expand_dims(img, 0).astype(np.float32) / 255.0
    preds = np.squeeze(model.predict(img)[0])
    # preds will give the probability score of
    index = np.argmax(preds)
    max_prob = np.amax(preds)
    cls_name = class_name[index]
    print(file_name, " : ", cls_name)
    # cv2.putText(img1, cls_name, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3, cv2.LINE_AA)

    # cv2.imwrite(dest_path + file_name, img1)
    # print(f"Image saved to: {dest_path}")

    return img1, preds, max_prob, class_name[index]
