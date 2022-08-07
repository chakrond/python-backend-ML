import os
from .image import transform_image
from torchvision import models
import json

# Create pre-trained model and prediction

# use the pretrained weights
model = models.densenet121(pretrained=True)
# using our model only for inference, switch to `eval` mode:
model.eval()


# Get prediction result g
dir = os.path.abspath(os.path.dirname(__file__))
imagenet_folder = os.path.join(dir, './image_net_class/imagenet_class_index.json')
imagenet_class_index = json.load(open(imagenet_folder))

def get_prediction(image_bytes):
    tensor = transform_image(image_bytes=image_bytes)
    outputs = model.forward(tensor)
    _, y_hat = outputs.max(1)
    predicted_idx = str(y_hat.item())
    return imagenet_class_index[predicted_idx]