# transform image to rescaled numpy type
from torchvision import transforms as T

def transforms(width=288, height=144):
    return T.Compose([
              T.Resize(size=(width, height)),
              T.ToTensor(),
              T.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
              ])