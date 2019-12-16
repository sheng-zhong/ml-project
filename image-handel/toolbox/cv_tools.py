from PIL import Image
import cv2
import numpy as np
import os
import uuid

def write_words_in_img(words, img, save_name=None, blank_size=200, img_save_path='./detected_frame'):
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    img = cv2.copyMakeBorder(img, 0, 0, 0, blank_size, cv2.BORDER_CONSTANT, value=[255,255,255])
    space_line = int(img.shape[0] / len(words))
    for i in range(len(words)):
        img_save = cv2.putText(img, words[i], (img.shape[1] - blank_size + 10, (i)*space_line + 13), \
            cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 0), 1)
    format_path(img_save_path)
    save_file_path = os.path.join(img_save_path, '{}.jpg'.format(uuid.uuid1()))
    if save_name:
        save_file_path = os.path.join(img_save_path, 'detected-{}'.format(save_name))
    cv2.imwrite(save_file_path, img_save)
    print('[+] Saved detected image on {}'.format(save_file_path))
    return 0

def format_path(_path):
    if not os.path.exists(_path):
        os.mkdir(_path)
    return 0
