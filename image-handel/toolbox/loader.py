# load image or load pretrained network
from PIL import Image
from toolbox.transforms import transforms
import torch
import json

def load_lable_list(lable_list_path):
    with open(lable_list_path, 'r') as f:
        label_list = json.load(f)[dataset]
    classes_num = len(label_list)
    return label_list, classes_num

def load_attribute_dict(attribute_dict_path):
    with open(attribute_dict_path, 'r') as f:
        attribute_dict = json.load(f)[dataset]
    return attribute_dict

def load_image(path, img_width=288, img_height=144):
    original_img = Image.open(path)
    transforms = transforms(img_width, img_height)
    src = transforms(original_img)
    src = src.unsqueeze(dim=0)
    return original_img, src

def load_network(network, network_path):
    network.load_state_dict(torch.load(network_path))
    return network.eval()

