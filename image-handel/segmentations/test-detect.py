from detectron2.config import get_cfg
import os
from detectron2.engine import DefaultPredictor
from detectron2.data import MetadataCatalog
from detectron2.utils.visualizer import Visualizer
import cv2

os.environ['CUDA_VISIBLE_DEVICES'] = "2"

cfg = get_cfg()
cfg.merge_from_file('./configs/COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml')
cfg.MODEL.WEIGHTS = './model_final_280758.pkl'
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5
predictor = DefaultPredictor(cfg)

im = cv2.imread('./input.jpg')
outputs = predictor(im)

v = Visualizer(im[:, :, ::-1], MetadataCatalog.get(cfg.DATASETS.TRAIN[0]), scale=1.2)
print(v.metadata)
v = v.draw_instance_predictions(outputs["instances"].to("cpu"))
save_name = './detected_frame.jpg'
cv2.imwrite(save_name, v.get_image()[:, :, ::-1])
