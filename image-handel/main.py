# image process for ml
# functions: recognize person by yolo and then classify attributes
from toolbox.loader import *
from net import *
from config import AttributeConfig
attribute_config = AttributeConfig()

# load model
network = ResNet50_nFC(attribute_config.network_classes)
model = load_network(network, attribute_config.network_path)

# load image
original_img, img = load_image(attribute_config.img_path)

# get attributes and labels
label_list, classes_num = load_lable_list(attribute_config.labels_path)
attribute_dict = load_attribute_dict(attribute_config.attributes_path)

# predict
out = model.forward(img)
pred = torch.gt(out, torch.ones_like(out)/2 )  # threshold=0.5

# get labels
pred = pred.squeeze(dim=0)
for idx in range(num_label):
    name, chooce = attribute_dict[label_list[idx]]
    if chooce[pred[idx]]:
        print('{}: {}'.format(name, chooce[pred[idx]]))