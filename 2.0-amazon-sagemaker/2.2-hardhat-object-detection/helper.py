import cv2
import json

import conf

CLASS_MAP = conf.object_categories


def name_to_value(name):
    return CLASS_MAP.index(name)


def value_to_name(value):
    return CLASS_MAP[value]


def generate_annotation_file_dict(width, height, depth, image_id, annotations, categories, image_format='jpg'):
    
    return {
       "file": "{}.{}".format(image_id, image_format),
       "image_size": [
          {
             "width": width,
             "height": height,
             "depth": depth
          }
       ],
       "annotations": annotations,
       "categories": categories
    }


def generate_annotation(name, left, top, width, height):
    return {
         "class_id": name_to_value(name),
         "left": left,
         "top": top,
         "width": width,
         "height": height
    }


def generate_categorie(name, CLASS_MAP):
     return {
         "class_id": name_to_value(name),
         "name": name
      }

    
def dict_to_json(path, filename, data):
    with open('{}/{}.json'.format(path, filename), 'w') as file:
        x = json.dump(data, file)
    file.close()

    
def resize_image(path):
    flag = False
    img = cv2.imread(path)
    H, W, channels = img.shape
    if H > 512:
        flag = True
        H = 512
    if W > 512:
        flag = True
        W = 512
    if flag:
        img = cv2.resize(img, (H, W))
        cv2.imwrite(path, img)