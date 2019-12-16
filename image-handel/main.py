# image process for ml
# functions: recognize person by yolo and then classify attributes
import os
import sys
import argparse
import codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())
from tqdm import tqdm
from toolbox.loader import *
from toolbox.cv_tools import *
from net import *
from config import AttributeConfig
attribute_config = AttributeConfig()

# load model
os.environ['CUDA_VISIBLE_DEVICES'] = str("7")
network = ResNet50_nFC(attribute_config.network_classes)
model = load_network(network, attribute_config.network_path)

# get attributes and labels
label_list, classes_num = load_lable_list(attribute_config.labels_path)
attribute_dict = load_attribute_dict(attribute_config.attributes_path)

def predict_one_img(model, img, original_img, classes_num, attribute_dict, img_name=None):
    # predict
    out = model.forward(img)
    pred = torch.gt(out, torch.ones_like(out)/2 )  # threshold=0.5

    # get labels
    pred = pred.squeeze(dim=0)
    lable_words = []
    for idx in range(classes_num):
        name, chooce = attribute_dict[label_list[idx]]
        if chooce[pred[idx]]:
            print('{}: {}'.format(name, chooce[pred[idx]]))
            _word = '{}: {}'.format(name, chooce[pred[idx]])
            lable_words.append(_word)
    write_words_in_img(lable_words, original_img, save_name=img_name)
'''
if "__name__" == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('model_path', help='* 模型文件路径', default='models', type=str)
    parser.add_argument('input_image_path', help='* 待检测图片路径', default='test_sample/test.jpg', type=str)
    parser.add_argument('output_image_path', help='* 输出图片保存路径', default='output_sample/detected_test.jpg', type=str)
    parser.add_argument('gpu_num', help='* 选择gpu下标（多gpu时）', default='7', type=str)
'''

# load image(s)
if os.path.isdir(attribute_config.img_path):
    image_path_list = os.listdir(attribute_config.img_path)
    for img_name in tqdm(image_path_list):
        image_path = os.path.join(attribute_config.img_path, img_name)
        original_img, img = load_image(image_path)
        predict_one_img(model, img, original_img, classes_num, attribute_dict, img_name)
else:
    original_img, img = load_image(attribute_config.img_path)
    predict_one_img(model, img, original_img, classes_num, attribute_dict)


