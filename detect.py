from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import io
import re
import time
import cv2
import json
# import tensorflow as tf

import numpy as np
# import picamera
import datetime
from PIL import Image
from pandas import MultiIndex
from tflite_runtime.interpreter import Interpreter

import winsound # 匯入此模組實現聲音播放功能
import time # 匯入此模組，獲取當前時間

DELAY_TIME = 0.5
CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480


def load_labels(path):
  """Loads the labels file. Supports files with or without index numbers."""
  with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    labels = {}
    for row_number, content in enumerate(lines):
      pair = re.split(r'[:\s]+', content.strip(), maxsplit=1)
      if len(pair) == 2 and pair[0].strip().isdigit():
        labels[int(pair[0])] = pair[1].strip()
      else:
        labels[row_number] = pair[0].strip()
  return labels


def set_input_tensor(interpreter, image):
  """Sets the input tensor."""
  tensor_index = interpreter.get_input_details()[0]['index']
  input_tensor = interpreter.tensor(tensor_index)()[0]
  input_tensor[:, :] = image


def get_output_tensor(interpreter, index):
  """Returns the output tensor at the given index."""
  output_details = interpreter.get_output_details()[index]
  tensor = np.squeeze(interpreter.get_tensor(output_details['index']))
  return tensor


def detect_objects(interpreter, image, threshold):
  """Returns a list of detection results, each a dictionary of object info."""
  set_input_tensor(interpreter, image)
  interpreter.invoke()

  # Get all output details
  boxes = get_output_tensor(interpreter, 0)
  classes = get_output_tensor(interpreter, 1)
  scores = get_output_tensor(interpreter, 2)
  count = int(get_output_tensor(interpreter, 3))

  results = []
  for i in range(count):
    if scores[i] >= threshold:
      result = {
          'bounding_box': boxes[i],
          'class_id': classes[i],
          'score': scores[i]
      }
      results.append(result)
  return results

def nothing():
  pass


def object_set_arg(cap):
  CAMERA_WIDTH = 640
  CAMERA_HEIGHT = 480
  labels = load_labels("coco_labels.txt")
  interpreter = Interpreter('model.tflite')
  interpreter.allocate_tensors()
  _, input_height, input_width, _ = interpreter.get_input_details()[0]['shape']
  cap.set(cv2.CAP_PROP_FRAME_WIDTH,CAMERA_WIDTH)
  cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_HEIGHT)

  times=1
  check_wakeup = False
  
  return labels,input_height,input_width,times,interpreter,check_wakeup

def object_main(labels,input_height,input_width,times,interpreter,check_wakeup,cap,my_sec,ring_time,frame_counter):
   
  ret,image_src =cap.read()
  image_size=image_src.shape
  CAMERA_HEIGHT=image_size[0]
  CAMERA_WIDTH=image_size[1]
  
  image = cv2.resize(image_src, (input_width, input_height))

 #取現在的時間
  t = time.localtime() 
  fmt = "%Y %m %d %H %M"
  now = time.strftime(fmt, t) 
  now = now.split(' ') 
  year, month, day, hour, minute = now[:]
  now = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), 0)
  now = time.mktime(now.timetuple())
  
  #print("現在時間:",hour,":",minute)
  #比對現在時刻與鬧鐘的時間，並設置delay與檢查起床與否

  if (now >= my_sec and now - my_sec < ring_time * 60 and frame_counter==7 and check_wakeup==False):
    PRE_TIME = time.time()
    music = 'music.wav'
    winsound.PlaySound(music, winsound.SND_ALIAS)

  if (times==1):
    results = detect_objects(interpreter, image, 0.4)
   
  if (my_sec - now < 3600 and my_sec - now >= 0 ):
    for num in range(len(results)) :
      label_id=int(results[num]['class_id'])
      box_top=int(results[num]['bounding_box'][0] * CAMERA_HEIGHT)
      box_left=int(results[num]['bounding_box'][1] * CAMERA_WIDTH)
      box_bottom=int(results[num]['bounding_box'][2] * CAMERA_HEIGHT)
      box_right=int(results[num]['bounding_box'][3] * CAMERA_WIDTH)
      label_score = round(results[num]['score'],2)
      frame_counter
      if((labels[label_id] == "person") and (label_score >= 0.4)
              and (box_top < int(0.3 * CAMERA_HEIGHT))):
        cv2.rectangle(image_src,(box_left,box_top),
                        (box_right,box_bottom),
                        (0,0,255),2)

        cv2.putText(image_src,
                    labels[label_id] +' score=' +str(label_score),
                    (box_left,box_top+20),
                    cv2.FONT_HERSHEY_SIMPLEX,0.6,
                    (0,0,255),1,cv2.LINE_AA)
        check_wakeup = True
        
      elif(labels[label_id] == "person"):
        cv2.rectangle(image_src,(box_left,box_top),
                        (box_right,box_bottom),
                        (0,255,0),2)

        cv2.putText(image_src,
                    labels[label_id] +' score=' +str(label_score),
                    (box_left,box_top+20),
                    cv2.FONT_HERSHEY_SIMPLEX,0.6,
                    (0,0,255),1,cv2.LINE_AA)

      times = times+1
      if (times>10) :
        times=1
    cv2.line(image_src, (0, int(0.3 * CAMERA_HEIGHT)), (CAMERA_WIDTH, int(0.3 * CAMERA_HEIGHT)), (0, 0, 0), 3)
  
  return image_src,check_wakeup

  
  



