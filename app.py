import torch
from src.load_img_transform import transform_image
from src.LungCovNet import LungCovNet

# Support to GPU and CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

input = transform_image('/home/brianadit24/Downloads/AI_Research/LungCovid/COVID-190.png')

model = LungCovNet(output_size=2)
model.load_state_dict(torch.load('model/weights_best.pth', map_location=device))

preds = model.predict(input)
print(preds)