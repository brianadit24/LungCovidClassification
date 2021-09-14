import torch
from src.load_img_transform import transform_image
from src.LungCovNet import LungCovNet

def predict_lung(img):
    # Support to GPU and CPU
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    input = transform_image(img)

    model = LungCovNet(output_size=2)
    model.load_state_dict(torch.load('model/weights_best.pth', map_location=device))
    labels = ['covid', 'normal']
    preds = model.predict(input)

    return labels[preds]